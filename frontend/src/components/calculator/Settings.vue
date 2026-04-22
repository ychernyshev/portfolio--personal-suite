<script setup>
import { ref, onMounted } from "vue";
import backendApi from "../../services/calculator/backendApi.js";

const tariff = ref(0);
const lastUpdated = ref("");
const loading = ref(false);
const message = ref({ text: "", type: "" });

// Завантажуємо поточний тариф
const fetchTariff = async () => {
  try {
    const res = await backendApi.get("calculator/current-tariff/");
    tariff.value = res.data.power_tariff;
    lastUpdated.value = new Date(res.data.last_updated).toLocaleString();
  } catch (e) {
    console.error("Помилка завантаження тарифу", e);
  }
};

// Зберігаємо оновлений тариф (використовуємо PATCH або PUT)
const updateTariff = async () => {
  loading.value = true;
  message.value = { text: "", type: "" };
  try {
    await backendApi.patch("calculator/current-tariff/", {
      power_tariff: tariff.value,
    });
    message.value = { text: "Тариф успішно оновлено!", type: "success" };
    fetchTariff(); // Оновлюємо дату останньої зміни
  } catch (e) {
    message.value = { text: "Помилка при збереженні", type: "danger" };
  } finally {
    loading.value = false;
  }
};

onMounted(fetchTariff);
</script>

<template>
  <div class="card row shadow-sm border-0">
    <div class="col-12 col-xxl-6">
      <div
          v-if="message.text"
          :class="['alert', 'alert-' + message.type, 'py-2 small']"
      >
        {{ message.text }}
      </div>

      <div class="form-group">
        <label class="form-label pt-3 title text-purple"
        >Energy Tariff Settings | Current Cost (UAH/kW) </label
        >
        <div class="row">
          <div class="col-12 col-xxl-8">
            <div class="input-group mb-2">
              <input
                  type="number"
                  step="0.01"
                  v-model="tariff"
                  class="form-control text-purple"
              />
              <span class="input-group-text">₴</span>
            </div>
            <p class="text-muted label-text">
              Last update: {{ lastUpdated }}
            </p>
          </div>
          <div class="col-12 col-xxl-4">
            <button
                @click="updateTariff"
                :disabled="loading"
                class="btn btn-c-warning text-light w-100 fw-bold"
            >
                  <span
                      v-if="loading"
                      class="spinner-border spinner-border-sm me-2"
                  ></span>
              Оновити тариф
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .title {
    font-size: clamp(1rem, 2vw, 1.1rem);
    font-weight: 400;
  }

  .label-text {
    font-size: 0.75rem;
    font-weight: 300;
  }
</style>
