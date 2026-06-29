<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<script setup lang="ts">
import { computed, onMounted } from 'vue';
import { Doughnut } from 'vue-chartjs';
import { ArcElement, Chart as ChartJS, Legend, Plugin, Tooltip } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

interface CategoryData {
  label: string;
  days_count: number;
  total_power: number;
  total_cost: number;
}

interface BackendResponse {
  year: number;
  categories: {
    sunny: CategoryData;
    cloudy: CategoryData;
    rain_snow: CategoryData;
    other: CategoryData;
  };
}

const props = defineProps<{
  analyticsData: BackendResponse
}>();

const emit = defineEmits<{
  (e: 'ready', colors: typeof categoryColors): void
}>();

const categoryColors = {
  sunny: { border: '#f59e0b', bg: 'rgba(245, 158, 11, 0.8)' },
  cloudy: { border: '#9ca3af', bg: 'rgba(156, 163, 175, 0.8)' },
  rain_snow: { border: '#3b82f6', bg: 'rgba(59, 130, 246, 0.8)' },
  other: { border: '#a855f7', bg: 'rgba(168, 85, 247, 0.8)' },
};

onMounted(() => {
  emit('ready', categoryColors);
});

const chartData = computed(() => {
  const cats = props.analyticsData?.categories;
  if (!cats) return { labels: [], datasets: [] };

  const labels = [
    cats.sunny?.label || 'Sunny',
    cats.cloudy?.label || 'Cloudy',
    cats.rain_snow?.label || 'Rain/Snow',
    cats.other?.label || 'Other'
  ];

  const dataValues = [
    cats.sunny?.total_power || 0,
    cats.cloudy?.total_power || 0,
    cats.rain_snow?.total_power || 0,
    cats.other?.total_power || 0
  ];

  const backgroundColor = [categoryColors.sunny.bg, categoryColors.cloudy.bg, categoryColors.rain_snow.bg, categoryColors.other.bg];
  const borderColor = [categoryColors.sunny.border, categoryColors.cloudy.border, categoryColors.rain_snow.border, categoryColors.other.border];

  return {
    labels,
    datasets: [
      {
        data: dataValues,
        backgroundColor,
        borderColor,
        borderWidth: 2,
        hoverOffset: 15,
      }
    ]
  };
});

const chartOptions = computed(() => ({
  responsive: true,
  maintainAspectRatio: false,
  layout: {
    padding: 5
  },
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      backgroundColor: '#1f2937',
      padding: 14,
      borderColor: '#a855f7',
      borderWidth: 1,
      titleFont: { size: 14, weight: 'bold' },
      bodyFont: { size: 13 },
      callbacks: {
        label: function (context: any) {
          const cats = props.analyticsData?.categories;
          if (!cats) return '';

          const keys: (keyof BackendResponse['categories'])[] = ['sunny', 'cloudy', 'rain_snow', 'other'];
          const currentKey = keys[context.dataIndex];
          const info = cats[currentKey];

          if (!info) return '';

          const powerKwh = round((info.total_power || 0) / 1000, 2);

          return [
            `• Duration: ${info.days_count} days`,
            `• Generated: ${powerKwh} kWh`,
            `• Total Savings: ${info.total_cost} UAH`
          ];
        }
      }
    }
  },
  cutout: '65%'
}));

const centerTextPlugin: Plugin = {
  id: 'centerText',
  beforeDraw(chart) {
    const cats = props.analyticsData?.categories;
    if (!cats) return;

    const { ctx, width, height } = chart;
    ctx.save();

    const totalYearPowerWatts = (cats.sunny?.total_power || 0) +
        (cats.cloudy?.total_power || 0) +
        (cats.rain_snow?.total_power || 0) +
        (cats.other?.total_power || 0);

    const totalYearPowerKwh = round(totalYearPowerWatts / 1000, 2);

    ctx.font = 'bold 24px sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(`${totalYearPowerKwh} kWh`, width / 2, height / 2 + 25);

    ctx.font = '11px sans-serif';
    ctx.fillStyle = '#6b7280';
    ctx.fillText('TOTAL GENERATED', width / 2, height / 2 + 48);
    ctx.restore();
  }
};

function round(value: number, decimals: number) {
  return Number(Math.round(Number(value + 'e' + decimals)) + 'e-' + decimals);
}
</script>

<template>
  <div class="chart-holder">
    <Doughnut :data="chartData" :options="chartOptions" :plugins="[centerTextPlugin]" />
  </div>
</template>

<style scoped>
.chart-holder {
  position: relative;
  height: 360px;
  width: 60%;
  max-width: 440px;
  margin: 0 auto;
}
</style>