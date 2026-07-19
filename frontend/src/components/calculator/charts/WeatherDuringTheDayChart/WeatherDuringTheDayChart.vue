<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<script setup lang="ts">
import { computed } from 'vue';
import { Line } from 'vue-chartjs';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Filler
} from 'chart.js';
import { storeToRefs } from "pinia";
import {useOpenMeteoForecastStore} from "../../../../../store/useOpenMeteoForecastStore";

const solarForecastStore = useOpenMeteoForecastStore();
const { forecast } = storeToRefs(solarForecastStore);

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Filler);

const chartData = computed(() => {
  if (!forecast.value || !forecast.value.hourly_forecast_wh) {
    console.warn("Forecast data is missing");
    return { labels: [], datasets: [] };
  }

  const sunrise = forecast.value.daily?.sunrise?.[0] || null;
  const sunset = forecast.value.daily?.sunset?.[0] || null;

  const sunriseHour = sunrise ? new Date(sunrise).getHours() : 6;
  const sunsetHour = sunset ? new Date(sunset).getHours() : 20;

  const filteredLabels = [];
  const filteredData = [];

  for (let i = 0; i < 24; i++) {
    if (i >= sunriseHour - 1 && i <= sunsetHour + 1) {
      filteredLabels.push(`${i}:00`);
      filteredData.push(forecast.value.hourly_forecast_wh[i]);
    }
  }

  return {
    labels: filteredLabels,
    datasets: [{
      label: 'Wh per hour',
      data: filteredData,
      borderColor: '#a855f7',
      backgroundColor: 'rgba(168, 85, 247, 0.1)',
      tension: 0.4,
      fill: true,
      borderWidth: 3,
      pointRadius: 0,
      pointHoverRadius: 5,
    }]
  };
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    tooltip: {
      backgroundColor: '#1f2937',
      padding: 10,
      displayColors: false
    }
  },
  scales: {
    x: { grid: { display: false }, ticks: { color: '#6b7280', maxRotation: 0 } },
    y: { beginAtZero: true, grid: { color: 'rgba(0,0,0,0.05)' }, ticks: { color: '#6b7280' } }
  }
};
</script>

<template>
  <div class="chart-container h-100">
    <Line v-if="forecast" :data="chartData" :options="chartOptions" />
    <div v-else class="text-muted small text-center py-5 my-auto">Loading Hourly Generation Chart...</div>
  </div>
</template>

<style scoped>
.chart-container {
  position: relative;
  height: 200px;
  width: 100%;
}
</style>