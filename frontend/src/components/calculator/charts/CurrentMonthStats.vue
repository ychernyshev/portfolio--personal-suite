<script setup lang="ts">
  import MonthGenerationChart from "@/components/calculator/charts/MonthGenerationChart.vue";
  import backendApi from "@/services/backendApi.ts";
  import {onMounted, ref} from "vue";
  import MontGenerationStats from "@/components/calculator/MontGenerationStats.vue";

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
            <div class="d-flex flex-row justify-content-end">
              <p class="small text-purple my-auto">Analytics for the current month with a generation power forecast and actual power generation</p>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
          </div>
<!--          <button class="btn btn-blue-1 text-light" data-bs-target="#exampleModalToggle" data-bs-toggle="modal">Close stats window</button>-->
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
<!--          <div class="row">-->
<!--            <div class="col-12">-->
<!--              <mont-generation-stats />-->
<!--            </div>-->
<!--          </div>-->
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>