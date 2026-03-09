<script setup>
import { ref, onMounted, computed } from "vue";
import backendApi from "../services/backendApi";
import pagination from "../components/Pagination.vue";
import PowerChart from "../components/charts/PowerChart.vue";
import SavingsChart from "../components/charts/SavingsChart.vue";

const currentPage = ref(1);
const totalPages = ref(1);
const entries = ref([]);
const loading = ref(true);
const error = ref(null);

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

const chartLabels = computed(() => {
  return entries.value.map((item) => item.date);
});

const chartValues = computed(() => {
  return entries.value.map((item) => item.full_day_power);
});

const chartCosts = computed(() => {
  return entries.value.map((item) => item.full_day_cost);
});

onMounted(fetchEntries);
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
              <h4 class="text-info">
                TOTAL GENERATED POWER:
                <span class="badge p-2 bg-success text-light"
                  >30195.35WATT</span
                >
              </h4>
              <power-chart
                :labels="chartLabels"
                :power="chartValues"
                @goToPage="fetchEntries"
              />
              <pagination
                :current="currentPage"
                :total="totalPages"
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
              <h4 class="text-info">
                COST OF GENERATED POWER:
                <span class="badge p-2 bg-info text-light">131.90UAH</span>
              </h4>
              <savings-chart
                :labels="chartLabels"
                :cost="chartCosts"
                @goToPage="fetchEntries"
              />
              <pagination
                :current="currentPage"
                :total="totalPages"
                @goToPage="fetchEntries"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="col-xxl-3">
        <div class="card rounded-3 p-4">Weather widget</div>
      </div>
    </div>
    <div class="row mt-4">
      <div class="col-xxl-12">
        <div class="card rounded-3 p-4">
          <div class="row">
            <div class="col-xxl-3">
              <div class="mb-3">
                <label for="formFileSm" class="form-label">Import data</label>
                <input
                  class="form-control form-control-sm"
                  id="formFileSm"
                  type="file"
                />
              </div>
            </div>
            <div class="col-xxl-3">
              <button
                type="button"
                class="btn btn-light"
                style="margin-top: 1.8rem"
              >
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
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-snow2"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M8 16a.5.5 0 0 1-.5-.5v-1.293l-.646.647a.5.5 0 0 1-.707-.708L7.5 12.793v-1.086l-.646.647a.5.5 0 0 1-.707-.708L7.5 10.293V8.866l-1.236.713-.495 1.85a.5.5 0 1 1-.966-.26l.237-.882-.94.542-.496 1.85a.5.5 0 1 1-.966-.26l.237-.882-1.12.646a.5.5 0 0 1-.5-.866l1.12-.646-.884-.237a.5.5 0 1 1 .26-.966l1.848.495.94-.542-.882-.237a.5.5 0 1 1 .258-.966l1.85.495L7 8l-1.236-.713-1.849.495a.5.5 0 1 1-.258-.966l.883-.237-.94-.542-1.85.495a.5.5 0 0 1-.258-.966l.883-.237-1.12-.646a.5.5 0 1 1 .5-.866l1.12.646-.237-.883a.5.5 0 0 1 .966-.258l.495 1.849.94.542-.236-.883a.5.5 0 0 1 .966-.258l.495 1.849 1.236.713V5.707L6.147 4.354a.5.5 0 1 1 .707-.708l.646.647V3.207L6.147 1.854a.5.5 0 1 1 .707-.708l.646.647V.5a.5.5 0 0 1 1 0v1.293l.647-.647a.5.5 0 1 1 .707.708L8.5 3.207v1.086l.647-.647a.5.5 0 1 1 .707.708L8.5 5.707v1.427l1.236-.713.495-1.85a.5.5 0 1 1 .966.26l-.236.882.94-.542.495-1.85a.5.5 0 1 1 .966.26l-.236.882 1.12-.646a.5.5 0 0 1 .5.866l-1.12.646.883.237a.5.5 0 1 1-.26.966l-1.848-.495-.94.542.883.237a.5.5 0 1 1-.26.966l-1.848-.495L9 8l1.236.713 1.849-.495a.5.5 0 0 1 .259.966l-.883.237.94.542 1.849-.495a.5.5 0 0 1 .259.966l-.883.237 1.12.646a.5.5 0 0 1-.5.866l-1.12-.646.236.883a.5.5 0 1 1-.966.258l-.495-1.849-.94-.542.236.883a.5.5 0 0 1-.966.258L9.736 9.58 8.5 8.866v1.427l1.354 1.353a.5.5 0 0 1-.707.708l-.647-.647v1.086l1.354 1.353a.5.5 0 0 1-.707.708l-.647-.647V15.5a.5.5 0 0 1-.5.5"
                    />
                  </svg>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-cloud-sun-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M11.473 11a4.5 4.5 0 0 0-8.72-.99A3 3 0 0 0 3 16h8.5a2.5 2.5 0 0 0 0-5z"
                    />
                    <path
                      d="M10.5 1.5a.5.5 0 0 0-1 0v1a.5.5 0 0 0 1 0zm3.743 1.964a.5.5 0 1 0-.707-.707l-.708.707a.5.5 0 0 0 .708.708zm-7.779-.707a.5.5 0 0 0-.707.707l.707.708a.5.5 0 1 0 .708-.708zm1.734 3.374a2 2 0 1 1 3.296 2.198q.3.423.516.898a3 3 0 1 0-4.84-3.225q.529.017 1.028.129m4.484 4.074c.6.215 1.125.59 1.522 1.072a.5.5 0 0 0 .039-.742l-.707-.707a.5.5 0 0 0-.854.377M14.5 6.5a.5.5 0 0 0 0 1h1a.5.5 0 0 0 0-1z"
                    />
                  </svg>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-sun-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8M8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0m0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13m8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5M3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8m10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0m-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0m9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707M4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708"
                    />
                  </svg>
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
