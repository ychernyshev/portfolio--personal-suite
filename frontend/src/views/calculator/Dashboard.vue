<script setup>
import { ref, onMounted, computed } from "vue";
import backendApi from "../../services/calculator/backendApi.js";
import MessagesStack from "../../components/calculator/MessagesStack.vue";
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
import DataControllers from "../../components/calculator/DataControllers.vue";

const entries = ref([]);

const error = ref(null);
const activeTab = ref('power');

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
  fetchStats();
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

    <section class="table-section neomorphic pt-2 pb-3 pl-4 pr-4">
      <data-controllers />


<!--      <div class="row">-->
<!--        <div class="col-xxl-12 p-0 records-data-table">-->
<!--          <transition name="fade-slide" mode="out-in">-->
<!--            <div v-if="currentView === 'table'" class="table-container card-light table-responsive" key="table">-->
<!--              <table class="table table-borderless mb-1">-->
<!--                <colgroup>-->
<!--                  <col style="width: 10%;">-->
<!--                  <col style="width: 10%;">-->
<!--                  <col style="width: 10%;">-->
<!--                  <col style="width: 15%;">-->
<!--                  <col style="width: 15%;">-->
<!--                  <col style="width: 15%;">-->
<!--                  <col style="width: 10%;">-->
<!--                  <col style="width: 10%;">-->
<!--                  <col style="width: 10%;" class="d-none d-lg-block">-->
<!--                  <col style="width: 10%;" class="d-none d-lg-block">-->
<!--                </colgroup>-->
<!--                <thead>-->
<!--                <tr>-->
<!--                  <th scope="col">Date</th>-->
<!--                  <th scope="col" class="text-center d-none">Power</th>-->
<!--                  <th scope="col" class="w-10 text-center">Weather indicators</th>-->
<!--                  <th scope="col" class="text-center">Morning indicators</th>-->
<!--                  <th scope="col" class="text-center d-none">Afternoon indicators</th>-->
<!--                  <th scope="col" class="text-center">Evening indicators</th>-->
<!--                  <th scope="col" class="text-center">Energy generated</th>-->
<!--                  <th scope="col" class="text-center">Total power</th>-->
<!--                  <th scope="col" class="text-center d-none d-lg-block">Total cost</th>-->
<!--                  <th scope="col" class="text-center d-none d-lg-block">Tariff</th>-->
<!--                </tr>-->
<!--                </thead>-->
<!--                <tbody>-->
<!--                <tr v-for="entry in entries" :key="entry.id">-->
<!--                  <th scope="row" class="c-border small">{{ entry.date }}</th>-->
<!--                  <td class="text-center d-none d-md-table-cell c-border">{{ entry.power }}</td>-->
<!--                  <td class="text-center c-border">-->
<!--                    <template-->
<!--                        v-if="-->
<!--                    entry.weather_details && entry.weather_details.length > 0-->
<!--                  "-->
<!--                    >-->
<!--                      <icons-map-->
<!--                          v-for="condition in entry.weather_details"-->
<!--                          :key="condition.id"-->
<!--                          :wmo-code="condition.name"-->
<!--                          style="width: 22px; height: 22px; opacity: 0.8"-->
<!--                      />-->
<!--                    </template>-->
<!--                    <span v-else class="text-muted text-center d-none c-border">- -</span>-->
<!--                  </td>-->
<!--                  <td-->
<!--                      class="text-center c-border"-->
<!--                      v-if="entry.morning_data_charge > 0 || entry.morning_data_price"-->
<!--                  >-->
<!--                    {{ entry.morning_data_charge }}% - -->
<!--                    {{ entry.morning_data_price }} UAH-->
<!--                  </td>-->
<!--                  <td class="text-center" v-else>- -</td>-->
<!--                  <td-->
<!--                      class="text-center d-none"-->
<!--                      v-if="-->
<!--                  entry.afternoon_data_charge > 0 || entry.afternoon_data_price-->
<!--                "-->
<!--                  >-->
<!--                    {{ entry.afternoon_data_charge }}% - -->
<!--                    {{ entry.afternoon_data_price }}-->
<!--                  </td>-->
<!--                  <td class="text-center d-none" v-else>- -</td>-->
<!--                  <td-->
<!--                      class="text-center"-->
<!--                      v-if="entry.evening_data_charge > 0 || entry.evening_data_price"-->
<!--                  >-->
<!--                    {{ entry.evening_data_charge }}% - -->
<!--                    {{ entry.evening_data_price }} UAH-->
<!--                  </td>-->
<!--                  <td class="text-center" v-else>- -</td>-->
<!--                  <td class="text-center" v-if="entry.full_day_power > 0">-->
<!--                    <span class="badge bg-gradient-blue-1 text-light p-2 w-100"-->
<!--                    >{{ entry.full_day_power.toFixed(2) }}W</span-->
<!--                    >-->
<!--                  </td>-->
<!--                  <td class="text-center" v-else>- -</td>-->
<!--                  <td class="text-center d-none d-lg-block" v-if="entry.full_day_cost > 0">-->
<!--                    <span class="badge bg-dark-blue text-light p-2 w-sm-100"-->
<!--                    >{{ entry.full_day_cost.toFixed(2) }}UAH</span-->
<!--                    >-->
<!--                  </td>-->
<!--                  <td class="text-center d-none d-lg-block" v-else>- -</td>-->
<!--                  <td class="text-center d-none d-lg-block">-->
<!--                    <small>{{ entry.power_tariff }}</small>-->
<!--                  </td>-->
<!--                </tr>-->
<!--                </tbody>-->
<!--              </table>-->
<!--            </div>-->

<!--            <div v-else-if="currentView === 'form'" class="form-container" key="form">-->
<!--              <AddSolarRecordForm @saved="toggleAddRecord" @cancel="toggleAddRecord" />-->
<!--              <new-record @entry-added="() => { fetchEntries(); fetchStats(); }" />-->
<!--            </div>-->

<!--            <div v-else-if="currentView === 'settings'" key="settings" class="settings-containe" style="height: 49vh">-->
<!--              <settings />-->
<!--            </div>-->

<!--          </transition>-->

<!--        </div>-->
<!--      </div>-->
    </section>
  </main>

<!--  <aside class="sidebar ml-xl-3 m-0">-->
<!--    <div class="row d-none d-md-block neomorphic" style="height: 27%">-->
<!--      <div class="col-xxl-12">-->
<!--        <messages-stack ref="messagesRef" />-->
<!--      </div>-->
<!--    </div>-->
<!--    <div class="row neomorphic graphics-card">-->
<!--      <div class="col-xxl-12 p-0">-->
<!--        <ul class="nav nav-pills mb-1" id="pills-tab" role="tablist">-->
<!--          <li class="nav-item w-50" role="presentation">-->
<!--            <button-->
<!--                class="nav-link btn btn-sm w-100"-->
<!--                :class="{ active: activeTab === 'power', 'btn-light text-sky-blue-4': activeTab !== 'power', 'bg-gradient-blue-2 text-light': activeTab === 'power' }"-->
<!--                @click="activeTab = 'power'"-->
<!--            >-->
<!--              Power generated-->
<!--            </button>-->
<!--          </li>-->
<!--          <li class="nav-item w-50" role="presentation">-->
<!--            <button-->
<!--                class="nav-link btn btn-sm w-100"-->
<!--                :class="{ active: activeTab === 'cost', 'btn-light text-sky-blue-4': activeTab !== 'cost', 'bg-gradient-blue-2 text-light': activeTab === 'cost' }"-->
<!--                @click="activeTab = 'cost'"-->
<!--            >-->
<!--              Power cost-->
<!--            </button>-->
<!--          </li>-->
<!--        </ul>-->

<!--        <div class="tab-content">-->
<!--          <div v-show="activeTab === 'power'" class="tab-pane fade show active card-light">-->
<!--            <power-chart :labels="chartLabels" :power="chartValues" @goToPage="fetchEntries" />-->
<!--          </div>-->
<!--          <div v-show="activeTab === 'cost'" class="tab-pane fade show active card-light">-->
<!--            <savings-chart :labels="chartLabels" :cost="chartCosts" @goToPage="fetchEntries" />-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </aside>-->
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
</style>
