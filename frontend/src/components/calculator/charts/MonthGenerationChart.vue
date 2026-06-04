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

const todayDay = computed(() => new Date().getDate());

const chartData = computed(() => ({
  labels: props.labels,
  datasets: [
    {
      label: 'Actual generation (kWh)',
      data: props.actualPower,
      borderColor: '#a855f7',
      backgroundColor: '#a855f7',
      tension: 0.4,
      borderWidth: 4,
      pointRadius: (context: any) => context.dataIndex + 1 === todayDay.value ? 6 : 3,
      pointBackgroundColor: '#a855f7',
      spanGaps: true
    },
    {
      label: 'Forecast generation (kWh)',
      data: props.forecastPower,
      borderColor: '#9ca3af',
      backgroundColor: '#9ca3af',
      tension: 0.4,
      borderWidth: 3,
      borderDash: [6, 4],
      pointRadius: 0,
      spanGaps: true
    }
  ]
}));

const todayLinePlugin = {
  id: 'todayLine',
  afterDatasetsDraw(chart: any) {
    const { ctx, chartArea: { top, bottom }, scales: { x } } = chart;

    const todayIndex = props.labels.indexOf(todayDay.value);

    if (todayIndex !== -1) {
      const xPos = x.getPixelForValue(todayIndex);

      ctx.save();
      ctx.beginPath();
      ctx.lineWidth = 2;
      ctx.strokeStyle = '#4b5563';
      ctx.setLineDash([4, 4]);
      ctx.moveTo(xPos, top);
      ctx.lineTo(xPos, bottom);
      ctx.stroke();

      ctx.fillStyle = '#4b5563';
      ctx.font = 'bold 10px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('TODAY', xPos, top - 8);

      ctx.restore();
    }
  }
};

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
      backgroundColor: '#1f2937'
    }
  },
  scales: {
    x: {
      grid: { display: false },
      ticks: { color: '#6b7280' }
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
      <Line :data="chartData" :options="chartOptions" :plugins="[todayLinePlugin]" />
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