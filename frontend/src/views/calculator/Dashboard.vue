<script setup>
import { ref, onMounted, computed } from "vue";
import backendApi from "../../services/calculator/backendApi.js";
import WeatherIcon from "../../components/calculator/WeatherIcon.vue";
import WeatherWidget from "../../components/calculator/wingets/WeatherWidget.vue";
import Productivity from "../../components/calculator/wingets/Productivity.vue";
import IconsMap from "../../components/calculator/IconsMap.vue";
import NewRecord from "../../components/calculator/NewRecord.vue";
import Settings from "../../components/calculator/Settings.vue";
import StatWidget from "../../components/calculator/wingets/StatWidget.vue";
import DataControllers from "../../components/calculator/DataControllers.vue";
import Sidebar from "../../components/calculator/Sidebar.vue";
import RecordsTable from "../../components/calculator/RecordsTable.vue";

import { useNotificationStore } from "../../../store/useNotificationStore.js";
import { useCalculatorStore } from "../../../store/useCalculatorStore";

const store = useCalculatorStore();

// Total data (all time)
const stats = ref({ total_power: 0, total_cost: 0 });

const fetchStats = async () => {
  try {
    const response = await backendApi.get("stats/");
    stats.value = response.data;
  } catch (error) {
    console.error("Error during data loading:", error);
  }
};

onMounted(() => {
  fetchStats();
  store.fetchEntries();
});
</script>

<template>
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
      <records-table v-if="store.currentView === 'table'" :entries="store.entries" />
      <new-record    v-else-if="store.currentView === 'form'" />
      <settings      v-else-if="store.currentView === 'settings'" />
    </section>
  </main>
  <sidebar />
</template>

<style scoped>
.main-content {
  grid-area: content;
}


.widgets-container {
  max-width: 100%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-bottom: 30px;
}

.widgets-container .card:nth-child(1),
.widgets-container .card:nth-child(2) {
  width: 100%;
}

.widgets-container .card:nth-child(3) {
  grid-column: span 2;
  width: 100%;
}

@media (min-width: 1200px) {
  .widgets-container {
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>
