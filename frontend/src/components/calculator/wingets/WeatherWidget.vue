<script setup>
import { ref, onMounted } from 'vue';
import backendApi from "../../../services/calculator/backendApi.js";

const forecast = ref(null);
const loading = ref(true);

const fetchForecast = async () => {
  try {
    const response = await backendApi.get('solar-forecast/');
    forecast.value = response.data;
  } catch (error) {
    console.error("Error retrieving forecast:", error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchForecast();
});
</script>

<template>
  <div v-if="!loading && forecast">
    <h5 class="text-purple">Forecast: Today</h5>
    <div class="d-flex justify-content-between align-items-center">
      <div>
        <h2 class="text-sky-blue-4">{{ forecast.predicted_total_kwh }} kWh</h2>
        <p class="text-success mb-0">+{{ forecast.predicted_savings }} UAH savings</p>
      </div>
      <div class="text-muted small">
        <div class="text-end">
          Peak: {{ forecast.peak_hour }}:00
        </div>
        <h2 class="mb-0">{{ forecast.current_temp }}°C</h2>
        <p class="text-muted small mb-1 text-end">{{ forecast.weather_condition }}</p>
      </div>
    </div>
    <div class="text-end">
      <!--      <i :class="getWeatherIcon(forecast.weather_code)" class="fs-1 text-warning"></i>-->
    </div>
  </div>
  <div v-else-if="loading" class="text-center p-3">
    <span>Loading forecast...</span>
  </div>
</template>