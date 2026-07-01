<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<script setup>
import { onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useOpenMeteoForecastStore } from "../../../../store/useOpenMeteoForecastStore.js";
import ButtonComp from "@/components/personal/ButtonComp.vue";

const store = useOpenMeteoForecastStore();
// Додаємо dbLat та dbLon з Pinia
const { browserLat, browserLon, dbLat, dbLon, loading, isLocationDenied } = storeToRefs(store);

onMounted(async () => {
  // 1. Спочатку пробуємо підтягнути те, що вже збережено в БД
  await store.fetchDbCoordinates();

  // 2. Якщо БД пуста, лише тоді запускаємо геолокацію
  if (!dbLat.value) {
    await store.fetchForecast();
  }
});

const handleSave = async () => {
  if (browserLat.value && browserLon.value) {
    await store.saveCoordinates(browserLat.value, browserLon.value);
    alert("Coordinates saved successfully!");
  }
};
</script>

<template>
  <div class="geolocation-wrapper mt-3 mb-3 text-start">
    <p class="mb-1 fw-medium text-purple">Power Station Coordinates</p>

    <small v-if="isLocationDenied" class="text-muted">To see your browser coordinates, you need to enable <span class="fw-bold">geolocation</span></small>

    <div v-if="loading" class="text-muted small">
      <span>Detecting coordinates...</span>
    </div>

    <div v-else-if="browserLat && browserLon" class="text-muted lat-lon-text mb-2">
      <small>📍 Your browser coordinates. Latitude:
        <span class="fw-bold text-dark">{{ browserLat }}</span>, Longitude: <span class="fw-bold text-dark">{{ browserLon }}</span>
      </small>
    </div>

    <form @submit.prevent="handleSave" class="row">
      <div class="col-12 col-md-6 input-group mb-3" data-v-47349c20="">
        <span class="input-group-text" data-v-47349c20="">Latitude</span>
        <input type="text" class="form-control"  v-model=browserLat placeholder="For example: 49.8400" aria-label="Username" data-v-47349c20="">
        <span class="input-group-text" data-v-47349c20="">Longitude</span>
        <input type="text" class="form-control" v-model=browserLon placeholder="For example: 24.0300" aria-label="Server" data-v-47349c20="">
      </div>
      <button-comp title="Save" class="col-12 col-md-2 btn btn-blue-1 text-light h-100 p-1" />
    </form>

    <small v-if="dbLat && dbLon" class="text-muted">Your stored coordinates.
      <span class="fw-bold text-dark">{{ dbLat }}</span>, Longitude: <span class="fw-bold text-dark">{{ dbLon }}</span>
    </small>
    <small v-else class="text-muted">Your have not stored coordinates.</small>
  </div>
</template>

<style scoped>
.lat-lon-text {
  font-size: 0.9rem;
}
</style>