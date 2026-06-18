// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
import { computed } from "vue";
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler,
} from "chart.js";
import { useCalculatorStore } from "../../../../store/useCalculatorStore.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler,
);

const store = useCalculatorStore();

const chartData = computed(() => {
  const dates = store.entries.map(entry => entry.date);

  const powerValues = store.entries.map(entry => entry.full_day_power || 0);

  return {
    labels: dates,
    datasets: [
      {
        label: "Power generation (Wh)",
        backgroundColor: "rgba(52, 86, 173, 0.1)",
        borderColor: "#3456AD",
        data: powerValues,
        fill: true,
        tension: 0.4,
        borderWidth: 3,
        pointRadius: 4,
        pointBackgroundColor: "#3456AD",
        pointBorderColor: "#fff",
        pointHoverRadius: 6,
      },
        {
        label: "Cost savings (UAH)",
        backgroundColor: "rgba(52, 86, 173, 0.15)",
        borderColor: "#3456AD",
        data: powerValues,
        fill: true,
        tension: 0.4,
        borderWidth: 3,
        pointRadius: 4,
        pointBackgroundColor: "#3456AD",
        pointBorderColor: "#fff",
        pointHoverRadius: 6,
      },
    ],
  };
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
    tooltip: {
      backgroundColor: "rgba(255, 255, 255, 0.8)",
      titleColor: "#3456AD",
      bodyColor: "#3456AD",
      borderColor: "rgba(52, 86, 173, 0.2)",
      borderWidth: 1,
      padding: 10,
      displayColors: false,
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        color: "rgba(52, 86, 173, 0.05)",
        drawBorder: false
      },
      ticks: {
        color: "rgba(52, 86, 173, 0.7)",
        font: { size: 11 }
      },
    },
    x: {
      grid: { display: false },
      ticks: {
        color: "rgba(52, 86, 173, 0.7)",
        font: { size: 11 }
      },
    },
  },
};
</script>

<template>
  <div class="chart-container p-1">
    <Line v-if="store.entries.length > 0" :data="chartData" :options="chartOptions" />
    <div v-else class="text-center text-muted pt-5">
      No data available for chart
    </div>
  </div>
</template>

<style scoped>
.chart-container {
  height: 388px;
  background: transparent;
  padding: 20px;
  border-radius: 12px;
}
</style>