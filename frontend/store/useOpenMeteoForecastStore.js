// SPDX-License-Identifier: AGPL-3.0-or-later
import { defineStore } from 'pinia';
import { ref } from 'vue';
import backendApi from "@/services/backendApi.ts";

export const useOpenMeteoForecastStore = defineStore('solarForecast', () => {
  const forecast = ref(null);
  const loading = ref(false);
  const error = ref(null);
  const isLocationDenied = ref(false);

  const browserLat = ref(null);
  const browserLon = ref(null);

  const STABLE_LAT = 49.84;
  const STABLE_LON = 24.03;

  const getUserCoordinates = () => {
    return new Promise((resolve) => {
      if (!navigator.geolocation) {
        console.warn("Geolocation is not supported by this browser.");
        return resolve({ lat: STABLE_LAT, lon: STABLE_LON });
      }

      navigator.geolocation.getCurrentPosition(
        (position) => {
          isLocationDenied.value = false;
          resolve({
            lat: position.coords.latitude,
            lon: position.coords.longitude
          });
        },
        (error) => {
          console.warn("Geolocation denied or error. Falling back to default coordinates.", error);
          isLocationDenied.value = true;
          resolve({ lat: STABLE_LAT, lon: STABLE_LON });
        },
        { timeout: 5000 }
      );
    });
  };

  const fetchForecast = async () => {
    if (forecast.value) return;

    try {
      loading.value = true;
      error.value = null;

      const coords = await getUserCoordinates();

      if (isLocationDenied.value) {
        forecast.value = null;
        return;
      }

      browserLat.value = coords.lat.toFixed(4);
      browserLon.value = coords.lon.toFixed(4);

      const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone || "Europe/Kyiv";

      const openMeteoUrl = `https://api.open-meteo.com/v1/forecast?latitude=${STABLE_LAT}&longitude=${STABLE_LON}&hourly=shortwave_radiation,temperature_2m,weather_code,cloud_cover,relative_humidity_2m,surface_pressure,wind_speed_10m,wind_gusts_10m,wind_direction_10m&daily=sunrise,sunset&wind_speed_unit=ms&timezone=${encodeURIComponent(userTimezone)}&forecast_days=1`;

      const openMeteoResponse = await fetch(openMeteoUrl);
      if (!openMeteoResponse.ok) throw new Error(`Open-Meteo API error: ${openMeteoResponse.status}`);

      const weatherData = await openMeteoResponse.json();

      const response = await backendApi.post('calculator/process-weather/', weatherData);

      forecast.value = response.data;
    } catch (err) {
      console.error("Error retrieving or processing solar forecast:", err);
      error.value = err.message;
    } finally {
      loading.value = false;
    }
  };

  return {
    forecast,
    loading,
    error,
    browserLat,
    browserLon,
    fetchForecast
  };
});