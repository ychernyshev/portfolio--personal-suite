// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>

import EnergyTariffSetup from "@/components/calculator/settings/EnergyTariffSetup.vue";
import SystemFactorSetup from "@/components/calculator/settings/SystemFactorSetup.vue";
</script>

<template>
  <div class="card row shadow-sm border-0">
    <div class="col-12 col-xxl-6">


      <energy-tariff-setup />
      <hr>
      <system-factor-setup />
    </div>
  </div>
</template>

<style scoped>

</style>
