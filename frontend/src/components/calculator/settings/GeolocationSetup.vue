<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
<script setup>
  import { onMounted } from "vue";
  import { storeToRefs } from "pinia";
  import { useOpenMeteoForecastStore } from "../../../../store/useOpenMeteoForecastStore.js";
  import ButtonComp from "@/components/personal/ButtonComp.vue";

  const store = useOpenMeteoForecastStore();
  const { browserLat, browserLon, dbLat, dbLon, loading, isLocationDenied } = storeToRefs(store);

  onMounted(async () => {
    await store.fetchDbCoordinates();

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
    <div class="row">
      <div class="col-12 pt-3 pb-3">
        <form @submit.prevent="handleSave" class="row justify-content-between">
          <div class="col-12 col-md-6 p-0 p-md-3">
            <small v-if="isLocationDenied" class="text-muted">To see your browser coordinates, you need to enable <span class="fw-bold">geolocation</span></small>

            <div v-if="loading" class="text-muted small">
              <span>Detecting coordinates...</span>
            </div>

            <div v-else-if="browserLat && browserLon" class="text-muted lat-lon-text mb-2">
              <small>📍 Your browser coordinates. Latitude:
                <span class="fw-bold text-dark">{{ browserLat }}</span>, Longitude: <span class="fw-bold text-dark">{{ browserLon }}</span>
              </small>
            </div>
            <div class="row neomorphic m-0 p-0">
              <div class="col-12 col-lg-10">
                <div class="row">
                  <div class="col-6 col-lg-3 text-purple p-3 text-center">
                    <span class="">Latitude</span>
                  </div>
                  <div class="col-6 col-lg-3 p-2">
                    <input type="text"
                           class="form-control form-control-sm form-control-plaintext border-0 bg-transparent w-auto"
                           v-model="browserLat"
                           placeholder="For example: 49.8400"
                           aria-label="Latitude">
                  </div>
                  <div class="col-6 col-lg-3 text-purple p-3 text-center">
                    <span class="">Longitude</span>
                  </div>
                  <div class="col-6 col-lg-3 p-2">
                    <input type="text"
                           class="form-control form-control-sm form-control-plaintext border-0 bg-transparent w-auto"
                           v-model=browserLon
                           placeholder="For example: 24.0300"
                           aria-label="Longitude">
                  </div>
                </div>
              </div>
              <div class="col-12 col-lg-2 pl-0 pr-0">
                <button-comp title="Save"
                             type="button"
                             class="btn-blue-1 text-light w-100 h-100 border-radius-bottom-start-4 border-radius-bottom-end-4 border-radius-top-start-lg-0 border-radius-bottom-start-lg-0 border-radius-top-end-lg-4 rounded-md-4" />
              </div>
            </div>
          </div>
          <div class="col-12 col-md-4 pt-3">
            <div class="lat-lon-text mb-2 text-md-end">
              <small class="text-muted">Your stored coordinates.</small>
            </div>
            <div class="row">
              <div class="col-6 col-lg-3 bg-gradient-blue-2 p-3 text-white fw-bold text-center">
                <span class="">Latitude</span>
              </div>
              <div class="col-6 col-lg-3 p-3 text-center bg-body-tertiary">
                {{ dbLat }}
              </div>
              <div class="col-6 col-lg-3 bg-gradient-blue-2 p-3 text-white fw-bold text-center">
                <span class="">Longitude</span>
              </div>
              <div class="col-6 col-lg-3 p-3 text-center bg-body-tertiary">
                {{ dbLon }}
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .lat-lon-text {
    font-size: 0.9rem;
  }

  @media (min-width: 768px) {
    .text-md-end {
      text-align: end;
    }
  }
</style>