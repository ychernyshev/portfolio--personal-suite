// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
  import MonthGenerationChart from "@/components/calculator/charts/CurrentMonthStats/MonthGenerationChart.vue";
  import backendApi from "@/services/backendApi.js";
  import {onMounted, ref} from "vue";
  import ChooseMonth from "@/components/calculator/timemachine/ChooseMonth.vue";

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
  <div class="modal fade" id="CurrentMonthStatsModal" data-bs-backdrop="false" aria-hidden="true" aria-labelledby="CurrentMonthStatsModalLabel" tabindex="-1">
    <div class="modal-dialog modal-xxl modal-dialog-centered">
      <div class="modal-content neomorphic p-0">
        <div class="modal-body ps-2 pe-2 pb-0">
          <div class="row pt-1 pe-2">
            <div class="d-flex flex-row justify-content-between">
              <div class="display-flex flex-row justify-content-center align-items-center ml-3">
                <choose-month />
              </div>
              <div class="display-flex flex-row">
                <p class="small text-purple my-auto mr-5">Analytics for the current month with a generation power forecast and actual power generation</p>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
            </div>
          </div>
          <month-generation-chart
              v-if="monthGenerationGraphiData"
              month-name="Current Month"
              :labels="monthGenerationGraphiData.labels"
              :actual-power="monthGenerationGraphiData.actual_power"
              :forecast-power="monthGenerationGraphiData.forecast_power"
          />

          <div v-else-if="!errorMsg" class="text-center p-5 text-secondary">
            Analytics loading...
          </div>

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