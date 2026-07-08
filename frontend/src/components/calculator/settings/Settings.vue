// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
  import EnergyTariffSetup from "@/components/calculator/settings/EnergyTariffSetup.vue";
  import SystemFactorSetup from "@/components/calculator/settings/SystemFactorSetup.vue";
  import GeolocationSetup from "@/components/calculator/settings/GeolocationSetup.vue";
</script>

<template>
  <div class="card row shadow-sm border-0 justify-content-center align-items-center align-items-md-start">
    <div class="col-6 col-xxl-6">
      <ul class="nav nav-tabs mt-3 mb-3" id="pills-tab" role="tablist">
        <li class="nav-item" role="presentation">
          <button class="nav-link active nav-title"
                  id="pills-tariff-tab"
                  data-bs-toggle="pill"
                  data-bs-target="#pills-tariff"
                  type="button" role="tab"
                  aria-controls="pills-tariff"
                  aria-selected="true">Tariff
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link nav-title"
                  id="pills-system-factor-tab"
                  data-bs-toggle="pill"
                  data-bs-target="#pills-system-factor"
                  type="button"
                  role="tab"
                  aria-controls="pills-system-factor"
                  aria-selected="false">System factor
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link nav-title"
                  id="pills-geolocation-tab"
                  data-bs-toggle="pill"
                  data-bs-target="#pills-geolocation"
                  type="button"
                  role="tab"
                  aria-controls="pills-geolocation"
                  aria-selected="false">Geolocation
          </button>
        </li>
      </ul>
    </div>
    <div class="row mx-auto">
      <div class="col-12">
        <div class="tab-content w-100" id="pills-tabContent">
          <div class="tab-pane fade show active" id="pills-tariff" role="tabpanel" aria-labelledby="pills-tariff-tab"
               tabindex="0">
            <energy-tariff-setup/>
          </div>
          <div class="tab-pane fade text-start" id="pills-system-factor" role="tabpanel"
               aria-labelledby="pills-system-factor-tab" tabindex="0">
            <system-factor-setup/>
          </div>
          <div class="tab-pane fade" id="pills-geolocation" role="tabpanel" aria-labelledby="pills-geolocation-tab"
               tabindex="0">
            <geolocation-setup/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .nav-title {
    font-size: clamp(1.1rem, 1vw, 1rem);
  }
</style>
