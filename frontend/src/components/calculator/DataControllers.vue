<script setup>
import pagination from "../../components/calculator/Pagination.vue";

import {exportData} from "../../services/calculator/DataExport.js";
import {importData, handleFileChange} from "../../services/calculator/DataImport.js"
import backendApi from "../../services/calculator/backendApi.js";
import {useNumberAnimation} from "../../services/calculator/useNumberAnimation.js";
import {ref} from "vue";

const { animatedNumber: displayCost, animate: animateCost } = useNumberAnimation();
const { animatedNumber: displayEnergy, animate: animateEnergy } = useNumberAnimation();



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
</script>

<template>
  <div class="row align-items-end data-navigation-group">
    <div class="col-sm-12 col-xl-7">
      <div class="input-group">
        <form action="" class="w-100">
          <div class="row p-0 justify-content-center align-items-center">
            <div class="col-sm-12 col-md-8 input-group-dynamic-grid border-bottom right-angle-end p-0">
              <input
                  class="form-control form-control border-top border-start"
                  style="border: none"
                  id="formFileSm"
                  placeholder="Select the CSV file to import"
                  type="file"
                  @change="handleFileChange"
                  accept=".csv"
              />
            </div>
            <div class="col-12 col-sm-12 col-md-4 pl-0 pr-0 pt-3 pb-3 pr-xl-2">
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
    <div class="col-sm-12 col-xl-2 col-md-3 add-record-section card-light p-0 p-xl-2">
      <button class="btn btn-primary text-light w-100 p-md-3 p-xl-1 mb-xl-2" @click="currentView = currentView === 'form' ? 'table' : 'form'"
      >
        {{ currentView === 'form' ? 'Records table' : 'Add Record' }}</button>
    </div>
    <div class="col-12 col-md-9 col-xl-3">
      <div class="row setup-data-section p-0 pr-1 pt-2 pb-2 pt-md-0 pb-md-0 pb-xl-1">
        <div class="col-11 col-xl-10 p-0 pr-2 pl-md-2">
          <pagination />
        </div>
        <div class="col-1 col-xl-2 col-sm-1 p-0 pb-xl-1">

          <button class="btn card-light card-shadow text-purple w-100 h-100" @click="currentView = currentView === 'settings' ? 'table' : 'settings'"
                  :title="currentView === 'settings' ? 'Back to Table' : 'Settings'"
          >
            <svg v-if="currentView === 'settings'" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-table" viewBox="0 0 15 15">
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

  @media (min-width: 1200px) {
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
  }
</style>