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
  power: Array,
});

const chartData = computed(() => ({
  labels: props.labels,
  datasets: [
    {
      label: "Power generation (Wh)",
      backgroundColor: "rgba(52, 86, 173, 0.1)",
      borderColor: "#3456AD",
      data: props.power,
      fill: true,
      tension: 0.4,
      borderWidth: 3,
      pointRadius: 4,
      pointBackgroundColor: "#3456AD",
      pointBorderColor: "#fff",
      pointHoverRadius: 6,
    },
  ],
}));

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false,
    },
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
  <div class="chart-container">
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<style scoped>
.chart-container {
  height: 452px;
  background: transparent;
  padding: 20px;
  border-radius: 12px;
}
</style>
