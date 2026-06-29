<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<script setup>
import { onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useOpenMeteoForecastStore } from "../../../../store/useOpenMeteoForecastStore.js";

const openMeteoForecast = useOpenMeteoForecastStore();

const { browserLat, browserLon, loading } = storeToRefs(openMeteoForecast);

onMounted(async () => {
  if (!browserLat.value || !browserLon.value) {
    await openMeteoForecast.fetchForecast();
  }
});
</script>

<template>
  <div class="geolocation-wrapper mt-3 text-start">
    <p class="mb-1 fw-medium text-purple">System Geolocation</p>

    <div v-if="loading && !browserLat" class="text-muted small">
      <span>Detecting coordinates...</span>
    </div>

    <div v-else-if="browserLat && browserLon" class="text-muted lat-lon-text mb-2">
      <small>📍 Your coordinates: <span class="fw-bold text-dark">{{ browserLat }}, {{ browserLon }}</span></small>
    </div>
  </div>
</template>

<style scoped>
.lat-lon-text {
  font-size: 0.9rem;
}
</style>