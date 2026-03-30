<script setup>
import { ref, onMounted } from 'vue';
import backendApi from "../../../services/calculator/backendApi";

const history = ref([]);
const loadingHistory = ref(true);

const fetchHistory = async () => {
  try {
    const response = await backendApi.get('forecast/comparison/');
    history.value = response.data;
  } catch (error) {
    console.error("Error retrieving history:", error);
  } finally {
    loadingHistory.value = false;
  }
};

// Функція для визначення кольору точності
const getAccuracyClass = (accuracy) => {
  if (!accuracy) return 'text-muted';
  if (accuracy >= 90) return 'text-success'; // Дуже точно
  if (accuracy >= 75) return 'text-warning'; // Невелика похибка
  return 'text-danger'; // Аномалія
};

onMounted(fetchHistory);
</script>

<template>
  <div class="d-flex justify-content-between align-items-center mb-4">
    <h5 class="text-purple fw-bold mb-0 text-uppercase small" style="letter-spacing: 1px;">
      Efficiency Audit: Last 7 Days
    </h5>
    <i class="bi bi-calendar3 text-muted"></i>
  </div>

  <div v-if="loadingHistory" class="text-center py-5">
    <div class="spinner-border text-purple opacity-50" role="status"></div>
  </div>

  <div v-else class="table-responsive">
    <table class="table table-borderless align-middle mb-0">
      <thead>
      <tr class="text-muted small">
        <th>Date</th>
        <th>Forecast</th>
        <th>Actual</th>
        <th class="text-end">Accuracy</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="item in history" :key="item.date" class="border-top-neomorphic">
        <td class="fw-medium py-3">{{ item.date }}</td>
        <td class="text-secondary">{{ item.predicted }} <small>kWh</small></td>
        <td class="fw-bold text-dark">{{ item.actual }} <small>kWh</small></td>
        <td class="text-end">
              <span :class="getAccuracyClass(item.accuracy)" class="fw-bold">
                {{ item.accuracy ? item.accuracy + '%' : '—' }}
              </span>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.border-top-neomorphic {
  border-top: 1px solid rgba(0, 0, 0, 0.05);
}

.bg-purple-soft {
  background: rgba(111, 66, 193, 0.1);
}

/* Додатковий стиль для таблиці, щоб вона вписувалася в неоморфізм */
.table thead th {
  font-weight: 600;
  border: none;
  padding-bottom: 15px;
}
</style>