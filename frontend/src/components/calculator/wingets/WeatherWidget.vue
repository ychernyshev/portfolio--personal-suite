<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<script setup>
import {onMounted, ref} from 'vue';
import {storeToRefs} from "pinia";
import IconsMap from "../IconsMap/IconsMap.vue";
import {useMovementOfTheSunStore} from "../../../../store/useMovementOfTheSunStore.js";
import {useOpenMeteoForecastStore} from "../../../../store/useOpenMeteoForecastStore.js";
import LocationRequiredPlaceholder from "@/components/calculator/wingets/LocationRequiredPlaceholder.vue";
import WeatherDuringTheDayChart from "@/components/calculator/charts/WeatherDuringTheDayChart/WeatherDuringTheDayChart.vue";

const sunMovementStore = useMovementOfTheSunStore();
const {windSpeedAlert} = storeToRefs(sunMovementStore);

const solarForecastStore = useOpenMeteoForecastStore();
const {forecast, loading, browserLat, browserLon, isLocationDenied} = storeToRefs(solarForecastStore);

// Mini calendar
const showCalendar = ref(false);
const showDetailChart = ref(false);
const activeDate = ref(null);

const onDatePicked = (day) => {
  activeDate.value = day;
  showDetailChart.value = true;
};

const getWindDirectionData = (degrees) => {
  const directions = [
    { label: 'North', arrow: '↑', style: 'text-primary' },
    { label: 'North-East', arrow: '↗', style: 'text-primary-emphasis' },
    { label: 'East', arrow: '→', style: 'text-success' },
    { label: 'South-East', arrow: '↘', style: 'text-warning-emphasis' },
    { label: 'South', arrow: '↓', style: 'text-warning' },
    { label: 'South-West', arrow: '↙', style: 'text-warning-emphasis' },
    { label: 'West', arrow: '←', style: 'text-success' },
    { label: 'North-West', arrow: '↖', style: 'text-primary-emphasis' }
  ];

  const index = Math.round((degrees % 360) / 45) % 8;
  return directions[index];
};

onMounted(() => {
  solarForecastStore.fetchForecast();
});
</script>

<template>
  <div class="card neomorphic p-3 border-0">
    <div class="row">
      <div class="col-sm-12 col-md-6 col-xl-6 border-sm-end-0 border-md-end-1 d-flex flex-column justify-content-center">

        <div v-if="isLocationDenied" class="w-100">
          <p class="title-text my-auto text-start text-purple d-flex flex-row justify-content-between align-items-center mb-3">
            Forecast: Today
          </p>
          <LocationRequiredPlaceholder/>
        </div>

        <div v-else-if="!loading && forecast" class="w-100">
          <p class="title-text my-auto text-start text-purple d-flex flex-row justify-content-between align-items-center">
            Forecast: Today
            <span>
              <icons-map
                  v-if="forecast"
                  :wmoCode="forecast.weather_code"
                  class="weather-icon mr-1"
              />
              <span class="text-muted small mb-1 text-end sky-condition">{{ forecast.weather_condition }}</span>
            </span>
          </p>
          <div class="d-flex justify-content-between align-items-center">
            <div class="energy-block">
              <p class="text-sky-blue-4 huge-number">{{ forecast.predicted_total_kwh }} <span class="unit-text">kWh</span></p>
              <p class="text-success mb-0 savings-text">+{{ forecast.predicted_savings }} UAH savings</p>
            </div>

            <div class="text-muted small temp-block">
              <div class="text-end peak-time">
                Peak: {{ forecast.peak_hour }}:00
              </div>
              <h2 class="mb-0 temperature">{{ forecast.current_temp }}°C</h2>

              <div class="sky-condition"
                   :class="{'badge bg-danger-subtle text-danger border border-danger-subtle p-1 rounded-3 text-end animation-pulse': windSpeedAlert.isDangerous}">
                <div
                    class="d-flex flex-column align-items-end"
                    :class="{ 'text-danger fw-bold': windSpeedAlert.isDangerous, 'text-muted': !windSpeedAlert.isDangerous }"
                    style="line-height: 1.3rem">
                  <span v-if="windSpeedAlert.isDangerous">⚠ Strong wind! </span>
                  <span>
                    <span class="fw-medium">
                      Wind:
                      <span class="fw-bold">{{ windSpeedAlert.speed }}</span>
                      m/s
                    </span>
                  </span>
                  <span class="fw-medium">
                    Gusts:
                    <span class="fw-bold">{{ windSpeedAlert.maxGust }}</span>
                    m/s
                  </span>

                  <div class="wind-direction">
                    <span
                        class="arrow fw-bold mr-1"
                        :class="getWindDirectionData(forecast.wind_direction).style"
                        :style="{ transform: `rotate(${forecast.wind_direction}deg)`, display: 'inline-block', transition: 'transform 0.5s ease' }"
                    >
                      ↑
                    </span>
                    <span>{{ getWindDirectionData(forecast.wind_direction).label }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div v-else class="h-100 d-flex justify-content-center align-items-center py-4">
          <span class="text-muted">Loading forecast...</span>
        </div>
      </div>

      <div class="col-sm-12 col-md-6 col-xl-6">
        <weather-during-the-day-chart />
      </div>
    </div>
  </div>
</template>

<style scoped>
.forecast-content {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.title-text {
  font-size: clamp(1.2rem, 2.8vw, 1.35rem);
  font-weight: 500;
}

.energy-block {
  display: flex;
  flex-direction: column;
  align-items: baseline;
  line-height: 1rem;
}

.huge-number {
  font-size: clamp(3rem, 7vw, 2.9rem);
  font-weight: 300;
}

.unit-text {
  font-size: clamp(1.1rem, 3vw, 1.2rem);
  font-weight: 400;
}

.savings-text {
  font-size: clamp(1.2rem, 2vw, 1.32rem);
  margin: 0;
  margin-top: -0.2rem;
}

.temperature {
  margin: 0;
  margin-bottom: 2px;
  text-align: right;
  font-size: clamp(1.5rem, 5vw, 1.5rem);
  font-weight: 500;
}

.peak-time {
  font-size: 0.9rem;
  margin: 0;
}

.sky-condition {
  font-size: 0.9rem;
  margin: 0;
}

.weather-icon {
  width: clamp(2rem, 1vw, 4.5rem);
  height: clamp(2rem, 1vw, 4.5rem);
  opacity: 0.8;
}

@keyframes pulse {
  0% { opacity: 0.8; }
  50% { opacity: 1; }
  100% { opacity: 0.8; }
}
</style>