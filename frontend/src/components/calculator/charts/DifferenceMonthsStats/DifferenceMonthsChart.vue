// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup lang="ts">
import { computed } from 'vue';
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

interface MonthlyChartProps {
  labels: string[];
  actualPower: number[];
  totalCost?: number[];
}

const props = withDefaults(defineProps<MonthlyChartProps>(), {
  labels: () => [],
  actualPower: () => [],
  totalCost: () => []
});

const chartData = computed(() => ({
  labels: props.labels,
  datasets: [
    {
      label: 'Monthly generation',
      data: props.actualPower,
      backgroundColor: '#a855f7',
      hoverBackgroundColor: '#9333ea',
      borderRadius: {
        topLeft: 10,
        topRight: 10,
        bottomLeft: 0,
        bottomRight: 0
      },
      borderSkipped: false,
      maxBarThickness: 40,
      categoryPercentage: 0.6,
      barPercentage: 0.8
    }
  ]
}));

const chartOptions = computed(() => ({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'top' as const,
      labels: {
        color: '#4b5563',
        font: { family: 'inherit', weight: 'bold' }
      }
    },
    tooltip: {
      mode: 'index' as const,
      intersect: false,
      padding: 12,
      backgroundColor: '#1f2937',
      titleFont: { weight: 'bold' },
      callbacks: {
        label: (context: any) => {
          const index = context.dataIndex;
          const cost = props.totalCost && props.totalCost[index] !== undefined ? props.totalCost[index] : 0;

          return ` Generation: ${context.raw} kWh, Cost: ${cost} UAH`;
        }
      }
    }
  },
  scales: {
    x: {
      grid: { display: false },
      ticks: {
        color: '#6b7280',
        font: { family: 'inherit' },
        maxRotation: 45,
        minRotation: 0
      }
    },
    y: {
      min: 0,
      grid: { color: 'rgba(0, 0, 0, 0.05)' },
      ticks: { color: '#6b7280' }
    }
  }
}));
</script>

<template>
  <div class="solar-chart-card p-0">
    <div class="chart-container p-0">
      <Bar :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<style scoped>
.solar-chart-card {
  border-radius: 20px;
  margin: 20px 0;
}
.chart-container {
  position: relative;
  height: 380px;
  width: 100%;
  padding: 15px 10px 10px 10px;
}
</style>