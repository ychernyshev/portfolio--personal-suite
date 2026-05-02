<script setup>
import {onMounted, ref} from "vue";
import backendApi from "../../../services/calculator/backendApi.js";

const forecast_details = ref([]);
const loading = ref(true);
const errorMsg = ref("");

const date = new Date();
const currentMonthName = date.toLocaleString('en-US', {month: 'long'});

// Last month
const lastMonthDate = new Date(date);
lastMonthDate.setMonth(date.getMonth() - 1);
const lastMonthName = lastMonthDate.toLocaleString('en-US', {month: 'long'});

const forecastDetails = async () => {
  try {
    loading.value = true;
    const response = await backendApi.get('calculator/forecast/details/');
    console.log(`Response: ${response}`)
    forecast_details.value = response.data.results || response.data;
  } catch (error) {
    errorMsg.value = "Failed to load forecast";
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  forecastDetails();
});
</script>

<template>
  <div v-if="loading" class="text-center p-3">Loading forecast...</div>
  <div v-else-if="errorMsg" class="alert alert-danger">{{ errorMsg }}</div>
  <div class="row text-start">
    <p data-v-80000e9e="" class="text-purple widget-title">
      The {{ currentMonthName }} stats
    </p>
    <div class="col-6 d-inline-flex flex-column align-items-start widget-item">
      <div v-if="!loading && forecast_details" class="w-100 d-flex flex-column small align-items-start text-purple">
        <span class="fw-bold"></span>
        <span class="small">Sun days: <span class="fw-bold">2</span></span>
        <span class="small">Average temperature: <span class="fw-bold">36.6</span></span>
        <span class="small">Average power: <span class="fw-bold text-success-1">897Wh</span></span>
        <span class="small">Total power: <span class="fw-bold text-success-1">28597Wh</span></span>
        <span class="small">Total savings: <span class="fw-bold text-sky-blue-4">897UAH</span></span>
      </div>
    </div>
    <div class="col-6 d-flex flex-column w-100 align-items-start text-purple">
      <div class="text-success-1 d-flex flex-row">
          <span class="d-flex flex-column align-items-start">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-up-right" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M14 2.5a.5.5 0 0 0-.5-.5h-6a.5.5 0 0 0 0 1h4.793L2.146 13.146a.5.5 0 0 0 .708.708L13 3.707V8.5a.5.5 0 0 0 1 0z"/>
            </svg>
            <span style="font-size: 1.5rem; font-weight: 300">+</span>
          </span>
        <div class="widget-huge-number text-success-1 mt-2">29%</div>
      </div>
      <span class="">compare to <span class="text-lowercase text-warning-2">{{ lastMonthName }}</span></span>
    </div>
  </div>

<!--  <div class="table-responsive" v-if="!loading && forecast_details">-->
<!--    <table class="table">-->
<!--      <thead>-->
<!--        <th scope="col" v-for="item in forecast_details" :key="item.id">-->
<!--          {{ item.hour || item.time }}-->
<!--        </th>-->
<!--      </thead>-->
<!--      <tbody>-->
<!--      <tr>-->
<!--        <td v-for="item in forecast_details" :key="item.id">-->
<!--          <span>{{ item.temperature }}°C</span>-->
<!--        </td>-->
<!--      </tr>-->
<!--      </tbody>-->
<!--    </table>-->
<!--  </div>-->
</template>

<style scoped>
.widget-title {
  font-size: clamp(1.2rem, 2.8vw, 1.5rem);
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.widget-huge-number {
  font-size: clamp(3rem, 10vw, 3.5rem);
  font-weight: 200;
  line-height: 0.5;
}
</style>