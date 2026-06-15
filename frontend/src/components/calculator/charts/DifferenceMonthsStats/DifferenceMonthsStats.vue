<script setup lang="ts">
import backendApi from "@/services/backendApi.js";
import {onMounted, ref} from "vue";
import DifferenceMonthsChart from "@/components/calculator/charts/DifferenceMonthsStats/DifferenceMonthsChart.vue";

const monthsDifferenceGenerationGraphicData = ref();
const errorMsg = ref("");
const errorClass = ref("");

const getMonthGeneration = async () => {
  try {
    const response = await backendApi('calculator/difference_months_stats/');
    const data = response.data;

    if (data && !data.is_empty) {
      monthsDifferenceGenerationGraphicData.value = {
        labels: data.months_data.map((item: any) => item.month),
        actual_power: data.months_data.map((item: any) => item.total_power),
        total_cost: data.months_data.map((item: any) => item.total_cost)
      };
    } else {
      monthsDifferenceGenerationGraphicData.value = {labels: [], actual_power: [], total_cost: []};
    }
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
  <div class="modal fade" id="PowerGenerationByMonthModal" data-bs-backdrop="false" aria-hidden="true"
       aria-labelledby="PowerGenerationByMonthLabel" tabindex="-1">
    <div class="modal-dialog modal-xxl modal-dialog-centered">
      <div class="modal-content neomorphic p-0">
        <div class="modal-body ps-2 pe-2 pb-0">
          <div class="row pt-1 pe-2">
            <div class="d-flex flex-row justify-content-end">
              <p class="small text-purple my-auto">Analytics of power generation forecasts and actual power generation
                by months</p>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
          </div>
          <difference-months-chart
              v-if="monthsDifferenceGenerationGraphicData"
              :labels=monthsDifferenceGenerationGraphicData.labels
              :actual-power=monthsDifferenceGenerationGraphicData.actual_power
              :total-cost=monthsDifferenceGenerationGraphicData.total_cost
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