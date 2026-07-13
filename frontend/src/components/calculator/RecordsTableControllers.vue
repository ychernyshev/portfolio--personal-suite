// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
import {ref} from "vue";

import backendApi from "../../services/calculator/backendApi.js";
import {exportData} from "../../services/calculator/DataExport.js";
import {handleFileChange, importData} from "../../services/calculator/DataImport.js"
import {useNumberAnimation} from "../../services/calculator/useNumberAnimation.js";

import pagination from "../../components/calculator/Pagination.vue";

import {useCalculatorStore} from "../../../store/useCalculatorStore";

const store = useCalculatorStore();

const {animatedNumber: displayCost, animate: animateCost} = useNumberAnimation();
const {animatedNumber: displayEnergy, animate: animateEnergy} = useNumberAnimation();

// Switching "records table" and "add new record" cards
const isAddingRecord = ref(false);

const toggleAddRecord = () => {
  isAddingRecord.value = !isAddingRecord.value;
};

const handleSave = async (newData) => {
  try {
    const response = await backendApi.get('calculator/entries/', newData);

    const {total_cost, total_power} = response.data;

    animateCost(total_cost);
    animateEnergy(total_power);

    store.setView('table');
  } catch (error) {
    console.error("Error during loading:", error);
  }
};
</script>

<template>
  <div class="row align-items-end data-navigation-group">
    <div class="col-sm-12 col-xl-6">
      <div class="input-group">
        <form action="" class="w-100">
          <div class="row p-0 align-items-center">
<!--            <div-->
<!--                class="col-sm-12 col-md-8 col-xl-7 input-group-dynamic-grid right-angle-end p-0">-->
<!--              -->
<!--            </div>-->
            <div class="col-12 col-sm-12 col-md-4 col-xl-12 pl-0 pr-0 pt-3 pb-3 pl-xl-2 pr-xl-2">
              <div class="btn-group w-100" role="group" aria-label="Basic example">
                <input
                    class="form-control form-control neomorphic border-top border-start w-50 h-100 p-2 border-radius-bottom-end-lg-0 border-radius-top-end-lg-0"
                    style="border-bottom-right-radius: 0; border-top-right-radius: 0;"
                    id="formFileSm"
                    placeholder="Select the CSV file to import"
                    type="file"
                    @change="handleFileChange"
                    accept=".csv"
                />
<!--                <input type="file" id="file-upload" class="d-none" @change="handleFileChange" accept=".csv" />-->

<!--                <label for="file-upload"-->
<!--                       class="form-control neomorphic p-2 cursor-pointer w-50 h-100 my-auto border-radius-bottom-end-lg-0 border-radius-top-end-lg-0 text-center  "-->
<!--                       style="border-bottom-right-radius: 0; border-top-right-radius: 0;">-->
<!--                  <span class="my-auto">{{ fileName || "Select the CSV file to import" }}</span>-->
<!--                </label>-->
                <button class="btn btn-secondary c-border neomorphic btn-import p-2"
                        id="inputGroupFileAddon04"
                        type="button"
                        @click="importData">Import data
                </button>
                <button type="button" @click="exportData" class="btn btn-secondary c-border btn-export neomorphic p-2">Export
                  data
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
    <div data-v-09d6a0f5=""
         class="col-12 col-md-12 col-xl-3 card-light d-flex flex-row justify-content-center align-items-start ps-1 pe-1 pt-1 pb-4 btn-group"
         style="border-bottom-left-radius: 0; border-bottom-right-radius: 0;"
         role="group"
         aria-label="Basic example">
      <button type="button"
              @click="store.setView(store.currentView === 'form' ? 'table' : 'form')"
              class="btn btn-primary c-border w-50 d-flex align-items-center justify-content-center">
        <svg v-if="store.currentView !== 'form'" xmlns="http://www.w3.org/2000/svg" width="20" height="20"
             fill="currentColor" class="bi bi-plus"
             viewBox="0 0 16 16">
          <path
              d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-table"
             viewBox="0 0 16 16">
          <path
              d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 2h-4v3h4zm0 4h-4v3h4zm0 4h-4v3h3a1 1 0 0 0 1-1zm-5 3v-3H6v3zm-5 0v-3H1v2a1 1 0 0 0 1 1zm-4-4h4V8H1zm0-4h4V4H1zm5-3v3h4V4zm4 4H6v3h4z"/>
        </svg>
        <span class="ms-1">{{ store.currentView === 'form' ? 'Records table' : 'Add Record' }}</span>
      </button>
      <button
          type="button"
          @click="store.toggleCharts()"
          class="btn btn-success w-50"
          :class="{ 'is-active': store.isChartsExpanded }"
          title="Toggle analytics panel"
      >
        <svg v-if="store.isChartsExpanded" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
             fill="currentColor" class="bi bi-box-arrow-in-left" viewBox="0 0 16 16">
          <path fill-rule="evenodd"
                d="M10 3.5a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v9a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-2a.5.5 0 0 1 1 0v2A1.5 1.5 0 0 1 9.5 14h-8A1.5 1.5 0 0 1 0 12.5v-9A1.5 1.5 0 0 1 1.5 2h8A1.5 1.5 0 0 1 11 3.5v2a.5.5 0 0 1-1 0z"/>
          <path fill-rule="evenodd"
                d="M4.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H14.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708z"/>
        </svg>

        <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
             class="bi bi-graph-up" viewBox="0 0 16 16">
          <path fill-rule="evenodd"
                d="M0 0h1v15h15v1H0zm14.817 3.113a.5.5 0 0 1 .07.704l-4.5 5.5a.5.5 0 0 1-.74.037L7.06 6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609 2.61 4.15-5.073a.5.5 0 0 1 .704-.07"/>
        </svg>

        <span class="ms-2">
          {{ store.isChartsExpanded ? "Hide Charts" : "Show Charts" }}
        </span>
      </button>
    </div>
    <div data-v-09d6a0f5="" class="col-12 col-md-12 col-xl-3 mb-2">
      <div data-v-09d6a0f5="" class="row setup-data-section p-2 pe-1 pt-2 pb-2 pt-md-0 pb-md-0">
        <div data-v-09d6a0f5="" class="col-10 col-xl-10 p-0 pr-2 pl-md-2">
          <pagination/>
        </div>
        <div data-v-09d6a0f5="" class="col-2 col-md-2 p-0 pb-md-1 pb-xl-1">
          <button type="button"
                  class="btn btn-transform card-shadow card-light neomorphic radius-0 text-purple w-100 h-100"
                  @click="store.setView(store.currentView === 'settings' ? 'table' : 'settings')"
                  :title="store.currentView === 'settings' ? 'Back to Table' : 'Settings'">
            <svg v-if="store.currentView === 'settings'" xmlns="http://www.w3.org/2000/svg" width="20" height="20"
                 fill="currentColor" class="bi bi-table" viewBox="0 0 16 16">
              <path
                  d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 2h-4v3h4zm0 4h-4v3h4zm0 4h-4v3h3a1 1 0 0 0 1-1zm-5 3v-3H6v3zm-5 0v-3H1v2a1 1 0 0 0 1 1zm-4-4h4V8H1zm0-4h4V4H1zm5-3v3h4V4zm4 4H6v3h4z"/>
            </svg>

            <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                 class="bi bi-wrench-adjustable-circle" viewBox="0 0 16 16">
              <path d="M12.496 8a4.5 4.5 0 0 1-1.703 3.526L9.497 8.5l2.959-1.11q.04.3.04.61"/>
              <path
                  d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-1 0a7 7 0 1 0-13.202 3.249l1.988-1.657a4.5 4.5 0 0 1 7.537-4.623L7.497 6.5l1 2.5 1.333 3.11c-.56.251-1.18.39-1.833.39a4.5 4.5 0 0 1-1.592-.29L4.747 14.2A7 7 0 0 0 15 8m-8.295.139a.25.25 0 0 0-.288-.376l-1.5.5.159.474.808-.27-.595.894a.25.25 0 0 0 .287.376l.808-.27-.595.894a.25.25 0 0 0 .287.376l1.5-.5-.159-.474-.808.27.596-.894a.25.25 0 0 0-.288-.376l-.808.27z"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.input-group-dynamic-grid {
  flex: 0 0 auto;
}

.setup-data-section {
  margin-top: 0.5rem;
  padding: 0.8rem;
}

.setup-data-section .col-xxl-10 {
  padding: 0;
}

.setup-data-section .page-link {
  padding: 1.3rem;
}

.setup-data-section .card-light {
  padding: 0.7rem;
}

.card-light {
  background-color: white;
  padding: 0.3rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px) saturate(180%);
  -webkit-backdrop-filter: blur(10px) saturate(180%);
}

.card-shadow {
  box-shadow: 0.2rem 0.3rem 1rem var(--bg-color);
}

.radius-0 {
  border-radius: 0;
}

.btn-expand-table {
  background: rgba(52, 86, 173, 0.06);
  border: 1px solid rgba(52, 86, 173, 0.15);
  color: #3456AD;
  padding: 6px 16px;
  font-size: 0.85rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
}

.btn-expand-table:hover {
  background: rgba(52, 86, 173, 0.12);
  transform: translateY(-1px);
}

.btn-expand-table.is-active {
  background: #3456AD;
  color: #fff;
  box-shadow: 0 4px 12px rgba(52, 86, 173, 0.2);
}

.fade-in-quick-enter-active {
  transition: opacity 0.3s ease 0.15s;
}

.fade-in-quick-leave-active {
  transition: opacity 0.15s ease;
}

.fade-in-quick-enter-from, .fade-in-quick-leave-to {
  opacity: 0;
}

.btn-export {}
.btn-export:hover {
  background: linear-gradient(
      to bottom,
      var(--sunrise-yelow),
      var(--sunset-yelow)
  );
}

.btn-import {}
.btn-import:hover {
  background: var(--green-1);
}

@media (min-width: 768px) {

}

@media (min-width: 1200px) {
  .data-button-value {
    font-size: 0.8rem;
  }
}
</style>