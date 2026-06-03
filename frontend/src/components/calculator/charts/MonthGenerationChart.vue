<script setup lang="ts">
import { computed } from 'vue';
import { Line } from 'vue-chartjs';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

interface ChartDataProps {
  monthName: string;
  labels: number[];
  actualPower: (number | null)[];
  forecastPower: (number | null)[];
}

const props = withDefaults(defineProps<ChartDataProps>(), {
  monthName: 'Current Month',
  labels: () => [],
  actualPower: () => [],
  forecastPower: () => []
});

const chartData = computed(() => ({
  labels: props.labels,
  datasets: [
    {
      label: 'Actual output (kWh)',
      data: props.actualPower,
      borderColor: '#a855f7',
      backgroundColor: '#a855f7',
      tension: 0.4,
      borderWidth: 4,
      pointRadius: 4,
      pointHoverRadius: 7,
      spanGaps: false
    },
    {
      label: 'Weather Forecast (kWh)',
      data: props.forecastPower,
      borderColor: '#9ca3af',
      backgroundColor: '#9ca3af',
      tension: 0,
      borderWidth: 3,
      borderDash: [6, 6],
      pointRadius: 0,
      spanGaps: true
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
      titleColor: '#ffffff',
      bodyColor: '#9ca3af',
      callbacks: {
        label: (context: any) => {
          const label = context.dataset.label || '';
          const value = context.parsed.y;
          return value !== null ? ` ${label}: ${value.toFixed(2)} kWh` : ` ${label}: no data`;
        }
      }
    }
  },
  scales: {
    x: {
      title: {
        display: true,
        text: `Month days (${props.monthName})`,
        color: '#6b7280',
        font: { size: 12, weight: 'bold' }
      },
      grid: { display: false },
      ticks: { color: '#6b7280' }
    },
    y: {
      min: 0,
      title: {
        display: true,
        text: 'Energy (kWh)',
        color: '#6b7280',
        font: { size: 12, weight: 'bold' }
      },
      grid: { color: '#f3f4f6' },
      ticks: { color: '#6b7280' }
    }
  }
}));
</script>

<template>
  <div class="solar-chart-card text-end p-0">
    <div class="chart-container p-0">
      <Line :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<style scoped>
.solar-chart-card {
  border-radius: 20px;
  padding: 20px;
  margin: 20px 0;
}

.chart-header h3 {
  color: #4b5563;
  margin-top: 0;
  margin-bottom: 15px;
  font-size: 1.1rem;
  font-weight: 600;
}

.chart-container {
  position: relative;
  height: 350px;
  width: 100%;
  border-radius: 12px;
  padding: 10px;
}
</style>