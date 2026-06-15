// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
  import { ref, onMounted, computed } from "vue";
  import WeatherWidget from "../../components/calculator/wingets/WeatherWidget.vue";
  import NewRecord from "../../components/calculator/NewRecord.vue";
  import Settings from "../../components/calculator/Settings.vue";
  import StatWidget from "../../components/calculator/wingets/StatWidget.vue";
  import DataControllers from "../../components/calculator/DataControllers.vue";
  import Sidebar from "../../components/calculator/Sidebar.vue";
  import RecordsTable from "../../components/calculator/RecordsTable.vue";

  import { useNotificationStore } from "../../../store/useNotificationStore.js";
  import { useCalculatorStore } from "../../../store/useCalculatorStore";
  import WakeUpLoader from "@/components/calculator/WakeUpLoader.vue";

  const store = useCalculatorStore();
  const isLoading = ref(false);

  const stats = computed(() => store.stats);
  const currentView = computed(() => store.currentView);
  const entries = computed(() => store.entries);

  onMounted(async () => {
    const startTime = Date.now();
    isLoading.value = true;

    try {
      await Promise.all([
        store.fetchStats(),
        store.fetchEntries(1)
      ]);
    } catch (error) {
      const notification = useNotificationStore();
      notification.addNotification("Сервер ще не прокинувся, спробуйте оновити сторінку пізніше", "error");
    } finally {
      const duration = Date.now() - startTime;
      const minWait = 1500;
      if (duration < minWait) {
        setTimeout(() => {
          isLoading.value = false;
        }, minWait - duration);
      } else {
        isLoading.value = false;
      }
    }
  });
</script>

<template>
  <wake-up-loader :is-visible="isLoading" @cancel="isLoading = false" />
  <main class="main-content">
    <div class="widgets-container">
      <div class="card border-0 neomorphic">
        <stat-widget
            title="Total generated"
            label="power"
            :value="stats.total_power"
            unit="kWt"
        />
      </div>
      <div class="card border-0 neomorphic d-flex">
        <stat-widget
            title="Total earnings"
            label="cost"
            :value="stats.total_cost"
            unit="UAH"
            colorClass="text-primary"
        />
      </div>
      <weather-widget />
    </div>

    <section class="table-section neomorphic pl-4 pr-4">
      <data-controllers />

      <records-table v-if="currentView === 'table'" :entries="entries" />
      <new-record    v-else-if="currentView === 'form'" />
      <settings      v-else-if="currentView === 'settings'" />
    </section>
  </main>
  <sidebar />
</template>

<style scoped>
/* Твої стилі залишаються без змін */
.main-content { grid-area: content; }
.widgets-container {
  max-width: 100%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-bottom: 30px;
}
.widgets-container .card:nth-child(1),
.widgets-container .card:nth-child(2) { width: 100%; }
.widgets-container .card:nth-child(3) { grid-column: span 2; width: 100%; }
@media (min-width: 1200px) {
  .widgets-container { grid-template-columns: repeat(4, 1fr); }
}
</style>