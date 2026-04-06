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
      label: "Cost savings (UAH)",
      // Використовуємо трохи насиченіший синій для фону, щоб підкреслити "фінансову" частину
      backgroundColor: "rgba(52, 86, 173, 0.15)",
      borderColor: "#3456AD",
      data: props.cost,
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
      display: false, // Рекомендую приховати, оскільки назва зазвичай є в заголовку картки
    },
    tooltip: {
      backgroundColor: "rgba(255, 255, 255, 0.9)",
      titleColor: "#3456AD",
      bodyColor: "#3456AD",
      borderColor: "rgba(52, 86, 173, 0.2)",
      borderWidth: 1,
      padding: 12,
      displayColors: false,
      callbacks: {
        // Додаємо символ валюти у підказку
        label: (context) => ` ${context.parsed.y} UAH`,
      },
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        color: "rgba(52, 86, 173, 0.08)", // Тонка сітка в тон основного синього
        drawBorder: false
      },
      ticks: {
        color: "rgba(52, 86, 173, 0.8)", // Темно-синій, але напівпрозорий
        font: { size: 11 },
        callback: (value) => `${value} ₴` // Символ гривні на осі
      },
    },
    x: {
      grid: { display: false },
      ticks: {
        color: "rgba(52, 86, 173, 0.8)",
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
  height: 430px;
  background: transparent;
  padding: 20px;
  border-radius: 12px;
}
</style>
