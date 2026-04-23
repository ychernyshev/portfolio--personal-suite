<script setup>
import {onMounted, ref} from "vue";
import backendApi from "../../../services/calculator/backendApi.js";

const forecast_details = ref([]);
const loading = ref(true);
const errorMsg = ref("");

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

console.log()

onMounted(() => {
  forecastDetails();
});
</script>

<template>
  <div v-if="loading" class="text-center p-3">Loading forecast...</div>
  <div v-else-if="errorMsg" class="alert alert-danger">{{ errorMsg }}</div>
  <div v-if="!loading && forecast_details" class="w-100" style=" word-wrap: anywhere;">
    <span v-for="item in forecast_details" :key="item.id">{{ item.hour || item.time }}</span>
    <span v-for="item in forecast_details" :key="item.id">{{ item.temperature }}°C; </span>
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

</style>