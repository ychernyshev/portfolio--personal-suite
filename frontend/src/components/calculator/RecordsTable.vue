<script setup>
import {onMounted, ref} from "vue";
import IconsMap from "./IconsMap.vue";
import Settings from "./Settings.vue";
import NewRecord from "./NewRecord.vue";
import backendApi from "../../services/calculator/backendApi.js";

const currentView = ref('table');
const entries = ref([]);
const error = ref("");

const fetchEntries = async () => {
  try {
    const response = await backendApi.get('entries');
    entries.value = response.data.results || response.data;
  } catch (error) {
    error.value = error;
  }
}

onMounted(() => {
  fetchEntries();
})
</script>

<template>
  <div class="row mt-2 mt-xl-0">
    <div class="col-xxl-12 p-0 records-data-table">
      <transition name="fade-slide" mode="out-in">
        <div v-if="currentView === 'table'" class="table-container card-light" key="table">
          <div class="table-responsive">
            <table class="table table-borderless mb-1">
<!--                          <colgroup>-->
<!--                            <col style="width: 10%;">-->
<!--                            <col style="width: 10%;" class="d-none d-sm-table-cell">-->
<!--                            <col style="width: 10%;">-->
<!--                            <col style="width: 15%;" class="d-none d-md-table-cell">-->
<!--                            <col style="width: 15%;" class="d-none d-xl-table-cell">-->
<!--                            <col style="width: 15%;" class="d-none d-md-table-cell">-->
<!--                            <col style="width: 10%;">-->
<!--                            <col style="width: 10%;">-->
<!--                            <col style="width: 10%;" class="d-none d-lg-table-cell">-->
<!--                          </colgroup>-->
              <thead>
              <tr>
                <th scope="col" class="title">Date</th>
                <th scope="col" class="title text-center d-none d-sm-table-cell">Power (Wt)</th>
                <th scope="col" class="title text-center">Weather indicators</th>
                <th scope="col" class="title d-none d-md-table-cell">Morning indicators</th>
                <th scope="col" class="title text-center d-none d-xl-table-cell">Afternoon indicators</th>
                <th scope="col" class="title text-center d-none d-md-table-cell">Evening indicators</th>
                <th scope="col" class="title text-center">Energy generated</th>
                <th scope="col" class="title text-center">Energy cost</th>
                <th scope="col" class="title text-center d-none d-lg-table-cell">Tariff</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="entry in entries" :key="entry.id">
                <th scope="row" class="c-border small">{{ entry.date }}</th>
                <td class="text-center d-none d-sm-table-cell c-border">{{ entry.power }}</td>
                <td class="text-center c-border">
                  <template
                      v-if="
                    entry.weather_details && entry.weather_details.length > 0
                  "
                  >
                    <icons-map
                        v-for="condition in entry.weather_details"
                        :key="condition.id"
                        :wmo-code="condition.name"
                        style="width: 22px; height: 22px; opacity: 0.8"
                    />
                  </template>
                  <span v-else class="text-muted text-center c-border">- -</span>
                </td>
                <td
                    class="text-center c-border d-none d-md-table-cell"
                    v-if="entry.morning_data_charge > 0 || entry.morning_data_price"
                >
                  {{ entry.morning_data_charge }}% -
                  {{ entry.morning_data_price }} UAH
                </td>
                <td class="text-center d-none d-md-table-cell" v-else>- -</td>
                <td
                    class="text-center d-none d-xl-table-cell"
                    v-if="
                  entry.afternoon_data_charge > 0 || entry.afternoon_data_price
                "
                >
                  {{ entry.afternoon_data_charge }}% -
                  {{ entry.afternoon_data_price }}
                </td>
                <td class="text-center d-none d-xl-table-cell" v-else>- -</td>
                <td
                    class="text-center d-none d-md-table-cell"
                    v-if="entry.evening_data_charge > 0 || entry.evening_data_price"
                >
                  {{ entry.evening_data_charge }}% -
                  {{ entry.evening_data_price }} UAH
                </td>
                <td class="text-center d-none d-md-table-cell" v-else>- -</td>
                <td class="text-center" v-if="entry.full_day_power > 0">
                    <span class="badge bg-gradient-blue-1 text-light p-2 w-100"
                    >{{ entry.full_day_power.toFixed(2) }}W</span
                    >
                </td>
                <td class="text-center" v-else>- -</td>
                <td class="text-center" v-if="entry.full_day_cost > 0">
                    <span class="badge bg-dark-blue text-light p-2 w-sm-100"
                    >{{ entry.full_day_cost.toFixed(2) }}UAH</span
                    >
                </td>
                <td class="text-center" v-else>- -</td>
                <td class="text-center d-none d-lg-table-cell">
                  <small>{{ entry.power_tariff }}</small>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div v-else-if="currentView === 'form'" class="form-container" key="form">
          <AddSolarRecordForm @saved="toggleAddRecord" @cancel="toggleAddRecord" />
          <new-record @entry-added="() => { fetchEntries(); fetchStats(); }" />
        </div>

        <div v-else-if="currentView === 'settings'" key="settings" class="settings-containe" style="height: 49vh">
          <settings />
        </div>

      </transition>

    </div>
  </div>
</template>

<style scoped>
.records-data-table {
  min-width: 0;
  display: block;
  width: 100%;
}

.table-responsive {
  display: block;
  width: 100%;
  overflow-x: auto;
  max-width: 100%;
}

.title {
  font-size: clamp(1rem, 2vw, 1.1rem);
  font-weight: 500;
}
</style>