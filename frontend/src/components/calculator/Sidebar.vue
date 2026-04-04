<script setup>

import {computed, onMounted, ref} from "vue";
import SavingsChart from "./charts/SavingsChart.vue";
import PowerChart from "./charts/PowerChart.vue";
import MessagesStack from "./MessagesStack.vue";
import backendApi from "../../services/calculator/backendApi.js";
import {useNotificationStore} from "../../../store/useNotificationStore.js";

const entries = ref([]);
const activeTab = ref('power');
const error = ref(null);
const loading = ref(true);
const totalPages = ref(1);
const currentPage = ref(1);

// Messages
const notificationStore = useNotificationStore();
const handleMessage = (payload) => {
  notificationStore.addNotification(payload);
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

const fetchEntries = async(page = 1) => {
  try {
    loading.value = true;
    const response = await backendApi.get(`entries/?page=${page}`);
    entries.value = response.data.results;
    currentPage.value = page;
    totalPages.value = Math.ceil(response.data.count / 10);
  } catch(error) {
    loading.value = error;
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchEntries();
})
</script>

<template>
  <aside class="sidebar mt-4 m-0 row justify-content-center">
    <div class="row d-none d-lg-block neomorphic" style="height: 27%">
      <div class="col-xxl-12">
        <messages-stack ref="messagesRef" />
      </div>
    </div>
    <div class="row neomorphic graphics-card">
      <div class="col-xxl-12 p-0">
        <ul class="nav nav-pills mb-1" id="pills-tab" role="tablist">
          <li class="nav-item w-50" role="presentation">
            <button
                class="nav-link btn btn-sm w-100 btn-graphic-tab"
                :class="{ active: activeTab === 'power', 'btn-light text-sky-blue-4': activeTab !== 'power', 'bg-gradient-blue-2 text-light': activeTab === 'power' }"
                @click="activeTab = 'power'"
            >
              <span class="">Power generated</span>
            </button>
          </li>
          <li class="nav-item w-50" role="presentation">
            <button
                class="nav-link btn btn-sm w-100 btn-graphic-tab"
                :class="{ active: activeTab === 'cost', 'btn-light text-sky-blue-4': activeTab !== 'cost', 'bg-gradient-blue-2 text-light': activeTab === 'cost' }"
                @click="activeTab = 'cost'"
            >
              <span class="">Power cost</span>
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

<style scoped>
.btn-graphic-tab {
  padding: 1rem 0.5rem;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 48px;
}

@media (min-width: 992px) {
  .btn-graphic-tab {
    padding: 0.5rem 1rem;
    width: auto;
    min-height: auto;
  }
}
</style>