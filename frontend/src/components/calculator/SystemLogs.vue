// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
import MonthGenerationChart from "@/components/calculator/charts/CurrentMonthStats/MonthGenerationChart.vue";
import backendApi from "@/services/backendApi.js";
import {onMounted, ref} from "vue";

const monthGenerationGraphiData = ref();
const errorMsg = ref("");
const errorClass = ref("");

const getMonthGeneration = async () => {
  try {
    const response = await backendApi('calculator/power_generation_month_analytics/');
    monthGenerationGraphiData.value = response.data;
  } catch (error) {
    console.log(error);
    errorMsg.value = "No data is being received from the server.";
    errorClass.value = "alert-warning";
  }
}

onMounted(() => {
  getMonthGeneration();
})
</script>

<template>
  <div class="modal fade" id="SystemLogsModal" data-bs-backdrop="false" aria-hidden="true" aria-labelledby="SystemLogsLabel" tabindex="-1">
    <div class="modal-dialog modal-xxl modal-dialog-centered">
      <div class="modal-content neomorphic p-0">
        <div class="modal-body ps-2 pe-2 pb-0">
          <div class="row pt-1 pe-2">
            <div class="d-flex flex-row justify-content-end">
              <p class="small text-purple my-auto">The log of system events, warnings, or notifications</p>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
          </div>

          <table class="table">
            <thead>
            <tr>
              <th scope="col">Date</th>
              <th scope="col">Message description</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <th scope="row">11.11.1111</th>
              <td>Message</td>
            </tr>
            </tbody>
          </table>

          <div v-if="errorMsg" :class="['alert', errorClass, 'text-center']">
            {{ errorMsg }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>