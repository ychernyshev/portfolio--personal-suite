// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
import {computed} from "vue";
import {Line} from "vue-chartjs";
import {
  CategoryScale,
  Chart as ChartJS,
  Filler,
  Legend,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
} from "chart.js";
import {useCalculatorStore} from "../../../../store/useCalculatorStore.js";

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
  const dates = store.entries.map((entry) => (entry.date));
  const powerValues = store.entries.map(entry => entry.full_day_power || 0);

  return {
    labels: dates,
    datasets: [
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
  }
});

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
        font: {size: 11},
        callback: (value) => `${value} ₴` // Символ гривні на осі
      },
    },
    x: {
      grid: {display: false},
      ticks: {
        color: "rgba(52, 86, 173, 0.8)",
        font: {size: 11}
      },
    },
  },
};
</script>

<template>
  <div class="chart-container">
    <Line v-if="store.entries.length > 0" :data="chartData" :options="chartOptions"/>
    <div v-else class="text-center text-muted pt-5">
      No data available for chart
    </div>
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
