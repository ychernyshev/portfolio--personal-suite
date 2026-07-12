// SPDX-License-Identifier: AGPL-3.0-or-later
import {defineStore} from 'pinia';
import {ref} from 'vue';
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

    const dbLat = ref(null);
    const dbLon = ref(null);

    const detectedTimezone = ref('');

    const detectTimezone = async (lat, lon) => {
        try {
            const response = await backendApi.get(`calculator/get_timezone/?lat=${lat}&lon=${lon}`);
            console.log(response.data);
            const data = await response.data;
            detectedTimezone.value = data.timezone;
        } catch (err) {
            console.error("Timezone detect error:", err);
        }
    };

    const fetchDbCoordinates = async () => {
        try {
            const response = await backendApi.get('calculator/station_coordinates/');
            const data = response.data.results || response.data;
            if (data && data.length > 0) {
                const coords = Array.isArray(data) ? data[0] : data;
                dbLat.value = Number(coords.latitude).toFixed(4);
                dbLon.value = Number(coords.longitude).toFixed(4);
            }
        } catch (err) {
            console.error("Error fetching from DB:", err);
        }
    };

    const saveCoordinates = async (lat, lon) => {
        try {
            loading.value = true;
            await backendApi.post('calculator/station_coordinates/', {
                latitude: parseFloat(lat),
                longitude: parseFloat(lon)
            });
            dbLat.value = Number(lat);
            dbLon.value = Number(lon);
        } catch (err) {
            console.error("Error saving to DB:", err);
            throw err;
        } finally {
            loading.value = false;
        }
    };

    const getUserCoordinates = () => {
        return new Promise((resolve) => {
            if (!navigator.geolocation) {
                console.warn("Geolocation is not supported by this browser.");
                isLocationDenied.value = true;
                return resolve(null);
            }

            navigator.geolocation.getCurrentPosition(
                (position) => {
                    isLocationDenied.value = false;
                    resolve({
                        lat: position.coords.latitude,
                        lon: position.coords.longitude
                    });
                },
                (geoError) => {
                    console.warn("Geolocation error code:", geoError.code, geoError.message);

                    if (geoError.code === 1) {
                        isLocationDenied.value = true;
                    }

                    resolve(null);
                },
                {timeout: 4000}
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
                browserLat.value = null;
                browserLon.value = null;
                forecast.value = null;
                return;
            }

            if (coords) {
                browserLat.value = coords.lat.toFixed(4);
                browserLon.value = coords.lon.toFixed(4);
            } else {
                browserLat.value = STABLE_LAT.toFixed(4);
                browserLon.value = STABLE_LON.toFixed(4);
            }

            const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone || "Europe/Kyiv";

            const openMeteoUrl = `https://api.open-meteo.com/v1/forecast?latitude=${browserLat.value}&longitude=${browserLon.value}&hourly=shortwave_radiation,temperature_2m,weather_code,cloud_cover,relative_humidity_2m,surface_pressure,wind_speed_10m,wind_gusts_10m,wind_direction_10m&daily=sunrise,sunset&wind_speed_unit=ms&timezone=${encodeURIComponent(userTimezone)}&forecast_days=1`;

            const openMeteoResponse = await fetch(openMeteoUrl);
            if (!openMeteoResponse.ok) throw new Error(`Open-Meteo API error: ${openMeteoResponse.status}`);

            const weatherData = await openMeteoResponse.json();
            const response = await backendApi.post('calculator/process_weather/', weatherData);

            forecast.value = response.data.data;
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
        isLocationDenied,
        browserLat,
        browserLon,
        dbLat,
        dbLon,
        fetchForecast,
        fetchDbCoordinates,
        saveCoordinates,
        detectTimezone,
        detectedTimezone,
        getUserCoordinates,
    };
});