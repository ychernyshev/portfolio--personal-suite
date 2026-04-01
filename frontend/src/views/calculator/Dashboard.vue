<script setup>
import { ref, onMounted, computed } from "vue";
import backendApi from "../../services/calculator/backendApi.js";
import {useNumberAnimation} from "../../services/calculator/useNumberAnimation.js";
import {importData, handleFileChange} from "../../services/calculator/DataImport.js";
import {exportData} from "../../services/calculator/DataExport.js";
import MessagesStack from "../../components/calculator/MessagesStack.vue";
import pagination from "../../components/calculator/Pagination.vue";
import PowerChart from "../../components/calculator/charts/PowerChart.vue";
import SavingsChart from "../../components/calculator/charts/SavingsChart.vue";
import WeatherIcon from "../../components/calculator/WeatherIcon.vue";
import WeatherWidget from "../../components/calculator/wingets/WeatherWidget.vue";
import Productivity from "../../components/calculator/wingets/Productivity.vue";
import IconsMap from "../../components/calculator/IconsMap.vue";
import NewRecord from "../../components/calculator/NewRecord.vue";
import Settings from "../../components/calculator/Settings.vue";
import StatWidget from "../../components/calculator/wingets/StatWidget.vue";
import {useNotificationStore} from "../../../store/useNotificationStore.js";

const currentPage = ref(1);
const totalPages = ref(1);
const entries = ref([]);
const loading = ref(true);
const error = ref(null);
const activeTab = ref('power');
const currentView = ref('table');
const { animatedNumber: displayCost, animate: animateCost } = useNumberAnimation();
const { animatedNumber: displayEnergy, animate: animateEnergy } = useNumberAnimation();

// Entries and pagination
const fetchEntries = async (page = 1) => {
  try {
    loading.value = true;
    const response = await backendApi.get(`entries/?page=${page}`);
    entries.value = response.data.results;
    currentPage.value = page;
    totalPages.value = Math.ceil(response.data.count / 10);
  } catch (error) {
    error.value = "Cannot load data from backend";
    console.error(error);
  } finally {
    loading.value = false;
  }
};

// Number animate
const handleSave = async (newData) => {
  try {
    const response = await backendApi.get('entries/', newData);

    const { total_cost, total_power } = response.data;

    animateCost(total_cost);
    animateEnergy(total_power);

    currentView.value = 'table';
  } catch (error) {
    console.error("Error during loading:", error);
  }
};

// Switching "records table" and "add new record" cards
const isAddingRecord = ref(false);

const toggleAddRecord = () => {
  isAddingRecord.value = !isAddingRecord.value;
};

// Charts
const chartLabels = computed(() => {
  return entries.value.map((item) => item.date);
});

const chartValues = computed(() => {
  return entries.value.map((item) => item.full_day_power);
});

const chartCosts = computed(() => {
  return entries.value.map((item) => item.full_day_cost);
});

// Total data (all time)
const stats = ref({ total_power: 0, total_cost: 0 });

const fetchStats = async () => {
  try {
    const response = await backendApi.get("stats/");
    stats.value = response.data;
  } catch (error) {
    console.error("Помилка при завантаженні статистики:", error);
  }
};

// Messages
const notificationStore = useNotificationStore();
const handleMessage = (payload) => {
  notificationStore.addNotification(payload);
};

onMounted(() => {
  // const response = await backendApi.get('entries/');
  //
  // animateCost(response.data.total_cost);
  // animateEnergy(response.data.total_power);
  fetchEntries();
  fetchStats();
});
</script>

<template>
  <main class="main-content">
    <div class="cards-row-grid">
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

    <section class="table-section neomorphic pt-2 pb-3 pl-4 pr-4">
      <div class="row align-items-center data-navigation-group">
        <div class="col-xxl-8">
          <div class="input-group">
            <form action="" class="w-100">
              <div class="row">
                <div class="col-xxl-8 col-md-8 pl-0 pr-0 pl-1 pt-1">
                  <input
                      class="form-control form-control border-top border-start border-bottom right-angle-end"
                      style="border: none"
                      id="formFileSm"
                      placeholder="Select the CSV file to import"
                      type="file"
                      @change="handleFileChange"
                      accept=".csv"
                  />
                </div>
                <div class="col-xxl-4 col-md-4 pl-0 pr-0 pt-1">
                  <div class="btn-group w-100" role="group" aria-label="Basic example">
                    <button class="btn btn-secondary c-border"
                            id="inputGroupFileAddon04"
                            type="button"
                            @click="importData">Import data</button>
                    <button type="button" @click="exportData" class="btn btn-success c-border">Export data</button>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="col-xxl-2 col-md-3 card-light add-record-section">
          <button class="btn btn-primary text-light w-100" @click="currentView = currentView === 'form' ? 'table' : 'form'"
          >
            {{ currentView === 'form' ? 'Records table' : 'Add Record' }}</button>
        </div>
        <div class="col-xxl-2 col-md-9">
          <div class="row pt-1 pr-1 justify-content-between setup-data-section">
            <div class="col-xxl-10 col-sm-11 align-items-center pr-2">
              <pagination
                  :current="currentPage"
                  :total="totalPages"
                  @goToPage="fetchEntries"
              />

            </div>
            <div class="col-xxl-2 col-sm-1 d-flex justify-content-end align-items-baseline pe-0">

              <button class="btn card-light text-purple p-2 btn-sm" @click="currentView = currentView === 'settings' ? 'table' : 'settings'"
                      :title="currentView === 'settings' ? 'Back to Table' : 'Settings'"
              >
                <svg v-if="currentView === 'settings'" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-table" viewBox="0 0 16 16">
                  <path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 2h-4v3h4zm0 4h-4v3h4zm0 4h-4v3h3a1 1 0 0 0 1-1zm-5 3v-3H6v3zm-5 0v-3H1v2a1 1 0 0 0 1 1zm-4-4h4V8H1zm0-4h4V4H1zm5-3v3h4V4zm4 4H6v3h4z"/>
                </svg>

                <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                     class="bi bi-wrench-adjustable-circle" viewBox="0 0 16 16">
                  <path d="M12.496 8a4.5 4.5 0 0 1-1.703 3.526L9.497 8.5l2.959-1.11q.04.3.04.61" />
                  <path
                      d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-1 0a7 7 0 1 0-13.202 3.249l1.988-1.657a4.5 4.5 0 0 1 7.537-4.623L7.497 6.5l1 2.5 1.333 3.11c-.56.251-1.18.39-1.833.39a4.5 4.5 0 0 1-1.592-.29L4.747 14.2A7 7 0 0 0 15 8m-8.295.139a.25.25 0 0 0-.288-.376l-1.5.5.159.474.808-.27-.595.894a.25.25 0 0 0 .287.376l.808-.27-.595.894a.25.25 0 0 0 .287.376l1.5-.5-.159-.474-.808.27.596-.894a.25.25 0 0 0-.288-.376l-.808.27z" /></svg>
              </button>
            </div>
          </div>
        </div>
      </div>


      <div class="row">
        <div class="col-xxl-12 p-0 records-data-table">
          <transition name="fade-slide" mode="out-in">
            <div v-if="currentView === 'table'" class="table-container card-light" key="table">
              <table class="table table-borderless table-responsive mb-1">
                <colgroup>
                  <col style="width: 10%;">
                  <col style="width: 10%;">
                  <col style="width: 10%;">
                  <col style="width: 15%;">
                  <col style="width: 15%;">
                  <col style="width: 15%;">
                  <col style="width: 10%;">
                  <col style="width: 10%;">
                  <col style="width: 10%;">
                  <col style="width: 10%;">
                </colgroup>
                <thead>
                <tr>
                  <th scope="col">Date</th>
                  <th scope="col" class="text-center d-none d-md-table-cell">Power</th>
                  <th scope="col" class="w-10 text-center">Weather indicators</th>
                  <th scope="col" class="text-center">Morning indicators</th>
                  <th scope="col" class="text-center d-none d-md-table-cell">Afternoon indicators</th>
                  <th scope="col" class="text-center">Evening indicators</th>
                  <th scope="col" class="text-center">Energy generated</th>
                  <th scope="col" class="text-center d-xs-none d-md-table-cell">Tital cost</th>
                  <th scope="col" class="text-center d-xs-none d-md-table-cell">Tariff</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="entry in entries" :key="entry.id">
                  <th scope="row" class="c-border">{{ entry.date }}</th>
                  <td class="text-center d-none d-md-table-cell c-border">{{ entry.power }}</td>
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
                    <span v-else class="text-muted text-center d-none d-md-table-cell c-border">- -</span>
                  </td>
                  <td
                      class="text-center c-border"
                      v-if="entry.morning_data_charge > 0 || entry.morning_data_price"
                  >
                    {{ entry.morning_data_charge }}% -
                    {{ entry.morning_data_price }} UAH
                  </td>
                  <td class="text-center" v-else>- -</td>
                  <td
                      class="text-center d-none d-md-table-cell"
                      v-if="
                  entry.afternoon_data_charge > 0 || entry.afternoon_data_price
                "
                  >
                    {{ entry.afternoon_data_charge }}% -
                    {{ entry.afternoon_data_price }}
                  </td>
                  <td class="text-center d-none d-md-table-cell" v-else>- -</td>
                  <td
                      class="text-center"
                      v-if="entry.evening_data_charge > 0 || entry.evening_data_price"
                  >
                    {{ entry.evening_data_charge }}% -
                    {{ entry.evening_data_price }} UAH
                  </td>
                  <td class="text-center" v-else>- -</td>
                  <td class="text-center" v-if="entry.full_day_power > 0">
                    <span class="badge bg-gradient-blue-1 text-light p-2 w-100"
                    >{{ entry.full_day_power.toFixed(2) }}W</span
                    >
                  </td>
                  <td class="text-center" v-else>- -</td>
                  <td class="text-center d-xs-none" v-if="entry.full_day_cost > 0">
                    <span class="badge bg-dark-blue text-light p-2 w-sm-100 d-md-table-cell"
                    >{{ entry.full_day_cost.toFixed(2) }}UAH</span
                    >
                  </td>
                  <td class="text-center d-xs-none" v-else>- -</td>
                  <td class="text-center d-md-table-cell d-xs-none">
                    <small>{{ entry.power_tariff }}</small>
                  </td>
                </tr>
                </tbody>
              </table>
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
    </section>
  </main>

  <aside class="sidebar neomorphic">
    <div class="row d-lg-none" style="height: 30.5%">
      <div class="col-xxl-12">
        <messages-stack ref="messagesRef" />
      </div>
    </div>
    <div class="row">
      <div class="col-xxl-12">
        <ul class="nav nav-pills mb-1" id="pills-tab" role="tablist">
          <li class="nav-item w-50" role="presentation">
            <button
                class="nav-link btn btn-sm w-100"
                :class="{ active: activeTab === 'power', 'btn-light text-sky-blue-4': activeTab !== 'power', 'bg-gradient-blue-2 text-light': activeTab === 'power' }"
                @click="activeTab = 'power'"
            >
              Power generated
            </button>
          </li>
          <li class="nav-item w-50" role="presentation">
            <button
                class="nav-link btn btn-sm w-100"
                :class="{ active: activeTab === 'cost', 'btn-light text-sky-blue-4': activeTab !== 'cost', 'bg-gradient-blue-2 text-light': activeTab === 'cost' }"
                @click="activeTab = 'cost'"
            >
              Power cost
            </button>
          </li>
        </ul>

        <div class="tab-content">
          <div v-show="activeTab === 'power'" class="tab-pane fade show active card-light">
            <power-chart :labels="chartLabels" :power="chartValues" @goToPage="fetchEntries" />
          </div>
          <div v-show="activeTab === 'cost'" class="tab-pane fade show active card-light">
            <savings-chart :labels="chartLabels" :cost="chartCosts" @goToPage="fetchEntries" />
          </div>
        </div>
      </div>
    </div>
  </aside>
</template>

<style scoped></style>
