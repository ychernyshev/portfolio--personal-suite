<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<script setup lang="ts">
import {ref, computed, onMounted, onUnmounted, watch} from 'vue';
import { Line } from 'vue-chartjs';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Filler,
  Chart
} from 'chart.js';
import { storeToRefs } from "pinia";
import { useOpenMeteoForecastStore } from "../../../../../store/useOpenMeteoForecastStore";
import { getWeatherIconSrc } from "@/components/calculator/IconsMap/IconsMap";

const solarForecastStore = useOpenMeteoForecastStore();
const { forecast, weatherDayData } = storeToRefs(solarForecastStore);
const currentTime = ref(new Date());
const chartRef = ref<{ chart: Chart } | null>(null);

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Filler);

const weatherIconPlugin = {
  id: 'weatherIconPlugin',
  afterDraw(chart: any) {
    const { ctx, scales: { x, y } } = chart;
    const meta = chart.getDatasetMeta(0);

    meta.data.forEach((point: any, index: number) => {
      const weatherRecord = weatherDayData.value[index];
      if (weatherRecord && weatherRecord.weather_code) {
        const iconSrc = getWeatherIconSrc(weatherRecord.weather_code);
        const img = new Image();
        img.src = iconSrc;

        if (img.complete) {
          ctx.drawImage(img, point.x - 12, point.y - 35, 24, 24);
        }
      }
    });
  }
};

const currentTimePlugin = {
  id: 'nowLine',
  afterDraw(chart: any) {
    const { ctx, chartArea: { top, bottom }, scales: { x } } = chart;

    const now = currentTime.value;
    const currentHour = now.getHours() + now.getMinutes() / 60;

    const startIndex = (forecast.value?.daily?.sunrise ? new Date(forecast.value.daily.sunrise[0]).getHours() : 6);
    const nowIndex = currentHour - startIndex;

    if (nowIndex >= 0 && nowIndex < chart.data.labels.length) {
      const xPos = x.getPixelForValue(nowIndex);

      ctx.save();
      ctx.beginPath();
      ctx.lineWidth = 2;
      ctx.strokeStyle = '#9CA3AF';
      ctx.setLineDash([4, 4]);
      ctx.moveTo(xPos, top);
      ctx.lineTo(xPos, bottom);
      ctx.stroke();

      ctx.fillStyle = '#9CA3AF';
      ctx.font = 'bold 9px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('NOW', xPos, top - 10);
      ctx.restore();
    }
  }
};

onMounted(() => {
  solarForecastStore.fetchDayForecast();

  const timer = setInterval(() => {
    currentTime.value = new Date();
  }, 60000); // Оновлюємо кожну хвилину

  onUnmounted(() => clearInterval(timer));
})

watch(currentTime, () => {
  if (chartRef.value) {
    chartRef.value.chart.update('none');
  }
});

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

const chartOptions = computed(() => ({
  responsive: true,
  maintainAspectRatio: false,
  layout: {
    padding: {
      top: 40,
      bottom: 0
    }
  },
  plugins: {
    legend: {
      display: false
    },
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
}));
</script>

<template>
  <div class="chart-container h-100">
    <Line
        ref="chartRef"
        v-if="forecast"
        :data="chartData"
        :options="chartOptions"
        :plugins="[weatherIconPlugin, currentTimePlugin]"
    />
    <div v-else class="text-muted text-center py-5 my-auto">Loading Hourly Generation Chart...</div>
  </div>
</template>

<style scoped>
.chart-container {
  position: relative;
  height: 170px;
  width: 100%;
}
</style>