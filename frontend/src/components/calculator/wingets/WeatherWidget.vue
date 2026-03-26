<script setup>
import { ref, onMounted } from 'vue';
import backendApi from "../../../services/calculator/backendApi.js";
import IconsMap from "../IconsMap.vue";
import Productivity from "./Productivity.vue";

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
    <div class="d-flex justify-content-between align-items-center mt-2">
      <!--        MODAL-->
      <div class="d-flex justify-content-start">
        <button type="button" class="btn btn-light btn-c-light btn-sm d-flex align-items-center justify-content-center text-purple" data-bs-toggle="modal" data-bs-target="#exampleModal">
          <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-table pr-2" viewBox="0 0 16 16">
            <path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 2h-4v3h4zm0 4h-4v3h4zm0 4h-4v3h3a1 1 0 0 0 1-1zm-5 3v-3H6v3zm-5 0v-3H1v2a1 1 0 0 0 1 1zm-4-4h4V8H1zm0-4h4V4H1zm5-3v3h4V4zm4 4H6v3h4z"/>
          </svg> comparison table
        </button>
      </div>

      <!-- Modal -->
      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">Comparison table of actual and real solar energy production rates</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <productivity/>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>

      <!--        END MODAL-->
      <icons-map
          v-if="forecast"
          :wmoCode="forecast.weather_code"
      />
    </div>
  </div>
  <div v-else-if="loading" class="text-center p-3">
    <span>Loading forecast...</span>
  </div>
</template>