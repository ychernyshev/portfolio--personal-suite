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

const props = defineProps({
  labels: Array,
  cost: Array,
});

const chartData = computed(() => ({
  labels: props.labels,
  datasets: [
    {
      label: "Power generation (Wh)",
      backgroundColor: "rgba(75, 192, 192, 0.2)",
      borderColor: "#4bc0c0",
      data: props.cost,
      fill: true,
      tension: 0.4,
    },
  ],
}));

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: true,
      labels: { color: "#ffffff" },
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      grid: { color: "rgba(255, 255, 255, 0.1)" },
      ticks: { color: "#ffffff" },
    },
    x: {
      grid: { display: false },
      ticks: { color: "#ffffff" },
    },
  },
};
</script>

<template>
  <div class="chart-container">
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<style scoped>
.chart-container {
  height: 400px;
  background: #1a1a2e;
  padding: 20px;
  border-radius: 12px;
}
</style>
