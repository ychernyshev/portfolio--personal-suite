// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
import { ref, computed, onMounted } from "vue";
import IconsMap from "./IconsMap/IconsMap.vue";
import Settings from "./settings/Settings.vue";
import NewRecord from "./NewRecord.vue";

import PowerChart from "./charts/PowerChart.vue";
import SavingsChart from "./charts/SavingsChart.vue";

import { useCalculatorStore } from "../../../store/useCalculatorStore";
const store = useCalculatorStore();

const error = ref("");

const isExpanded = ref(false);
const activeTab = ref('power');

const chartEntries = ref([]);
const chartLoading = ref(false);
const totalPages = ref(1);
const currentPage = ref(1);
</script>

<template>
  <div class="row mt-2 mt-xl-0 position-relative">
    <div class="col-xxl-12 p-0 records-data-table">
      <transition name="fade-slide" mode="out-in">
        <div
          v-if="store.currentView === 'table'"
          class="table-container card-light"
          :class="{ 'expanded-right': store.isChartsExpanded }"
          key="table"
        >
          <div class="row g-3 m-0 align-items-start">
            <div :class="store.isChartsExpanded ? 'col-12 col-xl-9 m-0 p-0' : 'col-12 p-0 m-0'">
              <div class="table-responsive">
                <table class="table table-borderless mb-1">
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
                    <tr v-for="entry in store.entries" :key="entry.id">
                      <th scope="row" class="c-border small">{{ entry.date }}</th>
                      <td class="text-center d-none d-sm-table-cell c-border">{{ entry.power }}</td>
                      <td class="text-center c-border">
                        <template v-if="entry.weather_details && entry.weather_details.length > 0">
                          <icons-map v-for="condition in entry.weather_details" :key="condition.id" :wmo-code="condition.name" style="width: 22px; height: 22px; opacity: 0.8" />
                        </template>
                        <span v-else class="text-muted text-center c-border small">not discovered</span>
                      </td>
                      <td class="text-center c-border d-none d-md-table-cell" v-if="entry.morning_data_charge > 0 || entry.morning_data_price">{{ entry.morning_data_charge }}% - {{ entry.morning_data_price }} UAH</td>
                      <td class="text-center d-none d-md-table-cell small" v-else-if="entry.afternoon_data_charge && entry.evening_data_charge"><span class="bg-body-tertiary p-2 rounded-1 small text-upper text-success-2">not tracked</span></td>
                      <td class="text-center d-none d-md-table-cell small" v-else><span class="bg-body-tertiary p-2 rounded-1 small text-upper text-warning-2">no generation</span></td>
                      <td class="text-center d-none d-xl-table-cell" v-if="entry.afternoon_data_charge > 0 || entry.afternoon_data_price">{{ entry.afternoon_data_charge }}% - {{ entry.afternoon_data_price }}</td>
                      <td class="text-center d-none d-xl-table-cell small" v-else-if="!entry.morning_data_charge && !entry.evening_data_charge"><span class="bg-body-tertiary p-2 rounded-1 small text-upper text-warning-2">no generation</span></td>
                      <td class="text-center d-none d-xl-table-cell small" v-else><span class="bg-body-tertiary p-2 rounded-1 small text-upper text-success-2">not tracked</span></td>
                      <td class="text-center d-none d-md-table-cell" v-if="entry.evening_data_charge > 0 || entry.evening_data_price">{{ entry.evening_data_charge }}% - {{ entry.evening_data_price }} UAH</td>
                      <td class="text-center d-none d-md-table-cell small" v-else><span class="bg-body-tertiary p-2 rounded-1 small text-upper text-warning-2">no generation</span></td>
                      <td class="text-center" v-if="entry.full_day_power > 0"><span class="badge bg-gradient-blue-1 text-light p-2 w-100">{{ entry.full_day_power.toFixed(2) }}W</span></td>
                      <td class="text-center small" v-else><span class="bg-body-tertiary p-2 rounded-1 small text-upper text-warning-2">no generation</span></td>
                      <td class="text-center" v-if="entry.full_day_cost > 0"><span class="badge bg-dark-blue text-light p-2 w-sm-100">{{ entry.full_day_cost.toFixed(2) }}UAH</span></td>
                      <td class="text-center small" v-else><span class="bg-body-tertiary p-2 rounded-1 small text-upper text-warning-2">not calculated</span></td>
                      <td class="text-center d-none d-lg-table-cell"><small>{{ entry.power_tariff }}</small></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <transition name="fade-in-quick">
              <div v-if="store.isChartsExpanded" class="col-12 col-xl-3 charts-side-panel m-0 p-0" :class="{ 'bg-white' : store.isChartsExpanded }">
<!--                <ul class="nav nav-pills mb-2" id="pills-tab" role="tablist">-->
<!--                  <li class="nav-item w-100" role="presentation">-->
<!--                    <button-->
<!--                      class="nav-link btn btn-sm w-100 btn-graphic-tab p-1"-->
<!--                      :class="{ active: activeTab === 'power', 'btn-light text-sky-blue-4': activeTab !== 'power', 'bg-gradient-blue-2 text-light': activeTab === 'power' }"-->
<!--                      @click="activeTab = 'power'"-->
<!--                    >-->
<!--                      <span class="fw-bold">Count of power generation and cost</span>-->
<!--                    </button>-->
<!--                  </li>-->
<!--                </ul>-->

                <div class="tab-content">
                  <div v-show="activeTab === 'power'" class="tab-pane fade show active inner-chart-card">
                    <power-chart :labels="chartLabels" :power="chartValues" @goToPage="fetchChartEntries" />
                  </div>
                  <div v-show="activeTab === 'cost'" class="tab-pane fade show active inner-chart-card">
                    <savings-chart :labels="chartLabels" :cost="chartCosts" @goToPage="fetchChartEntries" />
                  </div>
                </div>
              </div>
            </transition>

          </div>
        </div>

        <div v-else-if="store.currentView === 'form'" class="form-container" key="form">
          <AddSolarRecordForm @saved="toggleAddRecord" @cancel="toggleAddRecord" />
          <new-record @entry-added="() => { fetchEntries(); fetchStats(); }" />
        </div>

        <div v-else-if="store.currentView === 'settings'" key="settings" class="settings-containe" style="height: 49vh">
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

.table-container {
  transition: width 0.4s cubic-bezier(0.25, 1, 0.5, 1), max-width 0.4s cubic-bezier(0.25, 1, 0.5, 1);
  position: relative;
  width: 100%;
  z-index: 1;
}

@media (min-width: 1200px) {
  .table-container.expanded-right {
    position: absolute;
    left: 0;
    width: 136.7%;
    max-width: 139%;
    z-index: 100;
  }
}

.charts-side-panel {
  border-left: 1px dashed rgba(52, 86, 173, 0.15);
}

.inner-chart-card {
  background: rgba(255, 255, 255, 0.4);
  border-radius: 12px;
  padding: 12px;
  border: 1px solid rgba(255, 255, 255, 0.5);
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

.btn-graphic-tab {
  padding: 0.6rem;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>