<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<script setup>
  import YearGenerationChart from "@/components/calculator/charts/CurrentYearStats/YearGenerationChart.vue";
  import backendApi from "@/services/backendApi.js";
  import { onMounted, ref } from "vue";

  const yearGenerationChartData = ref(null);
  const chartColors = ref(null);
  const errorMsg = ref("");
  const errorClass = ref("");

  const handleChartReady = (colors) => {
    chartColors.value = colors;
  };

  const getYearGeneration = async () => {
    try {
      errorMsg.value = "";
      const response = await backendApi('calculator/power_generation_year_analytics/');
      yearGenerationChartData.value = response.data;
    } catch (error) {
      console.log(error);
      errorMsg.value = "No data is being received from the server.";
      errorClass.value = "alert-warning";
    }
  }

  onMounted(() => {
    getYearGeneration();
  })
</script>

<template>
  <div class="modal fade" id="CurrentYearStatsModal" data-bs-backdrop="false" aria-hidden="true" aria-labelledby="CurrentYearStatsModalLabel" tabindex="-1">
    <div class="modal-dialog modal-xxl modal-dialog-centered">
      <div class="modal-content neomorphic p-0">
        <div class="modal-body p-4">

          <div class="d-flex flex-row align-items-center justify-content-between mb-3">
            <p class="small text-secondary my-auto fw-bold">
              Analytics for the current year with actual power generation
            </p>
            <button type="button" class="btn-close ms-3" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <div v-if="yearGenerationChartData" class="year-analytics-wrapper position-relative py-3">

            <year-generation-chart
                :analytics-data="yearGenerationChartData"
                @ready="handleChartReady"
            />

            <div v-if="chartColors" class="custom-legend-grid mt-5 mx-auto">
              <div class="legend-item">
                <span class="legend-box" :style="{ backgroundColor: chartColors.sunny.bg, borderColor: chartColors.sunny.border }"></span>
                <span class="legend-label">Sunny Days</span>
              </div>
              <div class="legend-item">
                <span class="legend-box" :style="{ backgroundColor: chartColors.cloudy.bg, borderColor: chartColors.cloudy.border }"></span>
                <span class="legend-label">Cloudy Days</span>
              </div>
              <div class="legend-item">
                <span class="legend-box" :style="{ backgroundColor: chartColors.rain_snow.bg, borderColor: chartColors.rain_snow.border }"></span>
                <span class="legend-label">Rain / Snow</span>
              </div>
              <div class="legend-item">
                <span class="legend-box" :style="{ backgroundColor: chartColors.other.bg, borderColor: chartColors.other.border }"></span>
                <span class="legend-label">Other Weather</span>
              </div>
            </div>

          </div>

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
.year-analytics-wrapper {
  width: 100%;
  min-height: 450px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.custom-legend-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(140px, max-content));
  gap: 20px 40px;
  justify-content: center;
}

.legend-item {
  display: flex;
  align-items: center;
  font-family: inherit;
  font-weight: bold;
  font-size: 16px;
  color: #4b5563;
}

.legend-box {
  display: inline-block;
  width: 40px;
  height: 20px;
  border-width: 2px;
  border-style: solid;
  border-radius: 4px;
  margin-right: 12px;
  flex-shrink: 0;
}

.legend-label {
  white-space: nowrap;
}
</style>