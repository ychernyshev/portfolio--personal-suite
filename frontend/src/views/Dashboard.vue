<script setup>
import { ref, onMounted, computed } from "vue";
import backendApi from "../services/backendApi";
import pagination from "../components/Pagination.vue";
import PowerChart from "../components/charts/PowerChart.vue";
import SavingsChart from "../components/charts/SavingsChart.vue";
import WeatherIcon from "../components/WeatherIcon.vue";

const currentPage = ref(1);
const totalPages = ref(1);
const entries = ref([]);
const loading = ref(true);
const error = ref(null);

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

onMounted(() => {
  fetchEntries();
  fetchStats();
});
</script>

<template>
  <div class="container-fliud p-4">
    <div class="row">
      <div class="col-xxl-9">
        <ul class="nav nav-tabs" id="myTab" role="tablist">
          <li class="nav-item" role="presentation">
            <button
              class="nav-link active"
              id="home-tab"
              data-bs-toggle="tab"
              data-bs-target="#home-tab-pane"
              type="button"
              role="tab"
              aria-controls="home-tab-pane"
              aria-selected="true"
            >
              Power generation
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button
              class="nav-link"
              id="profile-tab"
              data-bs-toggle="tab"
              data-bs-target="#profile-tab-pane"
              type="button"
              role="tab"
              aria-controls="profile-tab-pane"
              aria-selected="false"
            >
              Cost sevings
            </button>
          </li>
        </ul>
        <div class="card rounded-3 p-4">
          <div class="tab-content" id="myTabContent">
            <div
              class="tab-pane fade show active"
              id="home-tab-pane"
              role="tabpanel"
              aria-labelledby="home-tab"
              tabindex="0"
            >
              <h4 class="text-info">GENERATED POWER</h4>
              <power-chart
                :labels="chartLabels"
                :power="chartValues"
                @goToPage="fetchEntries"
              />
            </div>
            <div
              class="tab-pane fade"
              id="profile-tab-pane"
              role="tabpanel"
              aria-labelledby="profile-tab"
              tabindex="0"
            >
              <h4 class="text-info">COST OF GENERATED POWER</h4>
              <savings-chart
                :labels="chartLabels"
                :cost="chartCosts"
                @goToPage="fetchEntries"
              />
            </div>
          </div>
          <pagination
            :current="currentPage"
            :total="totalPages"
            @goToPage="fetchEntries"
          />
        </div>
      </div>
      <div class="col-xxl-3">
        <div class="row">
          <div class="col-xxl-6">
            <div class="card rounded-3 p-4">
              <h4 class="text-info">
                TOTAL GENERATED POWER:
                <span
                  class="badge p-2 bg-success text-light"
                  :title="stats.total_power.toFixed(2) + ' Watt'"
                  style="cursor: help"
                >
                  {{ (stats.total_power / 1000).toFixed(2) }} kWt
                </span>
              </h4>
            </div>
          </div>
          <div class="col-xxl-6">
            <div class="card rounded-3 p-4">
              <h4 class="text-info">
                COST OF GENERATED POWER:
                <span class="badge p-2 bg-info text-light">
                  {{ stats.total_cost.toFixed(2) }} UAH
                </span>
              </h4>
            </div>
          </div>
        </div>
        <div class="row mt-3">
          <div class="col-xxl-12">
            <div class="card rounded-3 p-4">Weather widget</div>
          </div>
        </div>
      </div>
    </div>
    <div class="row mt-4">
      <div class="col-xxl-12">
        <div class="card rounded-3 p-4">
          <div class="row">
            <div class="col-xxl-4 mb-3 border-end">
              <!-- <label for="formFileSm" class="form-label">Import data</label> -->
              <form action="" class="d-flex flex-row">
                <input
                  class="form-control form-control-sm border-top border-start border-bottom right-angle-end"
                  style="border: none"
                  id="formFileSm"
                  type="file"
                  placeholder="Select the CSV file to import"
                />
                <button
                  class="btn btn-sm btn-light w-50 border-top border-end border-bottom right-angle-start"
                >
                  Import data
                </button>
              </form>
            </div>
            <div class="col-xxl-2">
              <button type="button" class="btn btn-sm btn-primary w-75">
                Export data
              </button>
            </div>
          </div>
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col" class="text-center">Date</th>
                <th scope="col" class="text-center">Power</th>
                <th scope="col" class="text-center">Weather indicators</th>
                <th scope="col" class="text-center">Morning indicators</th>
                <th scope="col" class="text-center">Afternoon indicators</th>
                <th scope="col" class="text-center">Evening indicators</th>
                <th scope="col" class="text-center">Energy generated</th>
                <th scope="col" class="text-center">Total cost</th>
                <th scope="col" class="text-center">Tariff</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="entry in entries" :key="entry.id">
                <th scope="row" class="text-center">{{ entry.date }}</th>
                <td class="text-center">{{ entry.power }}</td>
                <td class="text-center">
                  <template
                    v-if="
                      entry.weather_details && entry.weather_details.length > 0
                    "
                  >
                    <WeatherIcon
                      v-for="condition in entry.weather_details"
                      :key="condition.id"
                      :name="condition.name"
                    />
                  </template>
                  <span v-else class="text-muted">- -</span>
                </td>
                <td
                  class="text-center"
                  v-if="
                    entry.morning_data_charge > 0 || entry.morning_data_price
                  "
                >
                  {{ entry.morning_data_charge }}% -
                  {{ entry.morning_data_price }} UAH
                </td>
                <td class="text-center" v-else>- -</td>
                <td
                  class="text-center"
                  v-if="
                    entry.afternoon_data_charge > 0 ||
                    entry.afternoon_data_price
                  "
                >
                  {{ entry.afternoon_data_charge }}% -
                  {{ entry.afternoon_data_price }}
                </td>
                <td class="text-center" v-else>- -</td>
                <td
                  class="text-center"
                  v-if="
                    entry.evening_data_charge > 0 || entry.evening_data_price
                  "
                >
                  {{ entry.evening_data_charge }}% -
                  {{ entry.evening_data_price }} UAH
                </td>
                <td class="text-center" v-else>- -</td>
                <td class="text-center" v-if="entry.full_day_power > 0">
                  <span class="badge p-2 bg-success"
                    >{{ entry.full_day_power.toFixed(2) }}W</span
                  >
                </td>
                <td class="text-center" v-else>- -</td>
                <td class="text-center" v-if="entry.full_day_cost > 0">
                  <span class="badge p-2 bg-info"
                    >{{ entry.full_day_cost.toFixed(2) }}UAH</span
                  >
                </td>
                <td class="text-center" v-else>- -</td>
                <td class="text-center">
                  <small>{{ entry.power_tariff }}</small>
                </td>
              </tr>
            </tbody>
          </table>
          <pagination
            :current="currentPage"
            :total="totalPages"
            @goToPage="fetchEntries"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
