<script setup>
import { ref, onMounted } from "vue";
import backendApi from "../services/backendApi";

const tariff = ref(0);
const lastUpdated = ref("");
const loading = ref(false);
const message = ref({ text: "", type: "" });

// Завантажуємо поточний тариф
const fetchTariff = async () => {
  try {
    const res = await backendApi.get("current-tariff/");
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
    await backendApi.patch("current-tariff/", {
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
  <div class="card shadow-sm border-0">
    <div class="card-header bg-warning text-dark fw-bold">
      <i class="bi bi-lightning-charge-fill me-2"></i>Налаштування тарифу
    </div>
    <div class="card-body">
      <div
        v-if="message.text"
        :class="['alert', 'alert-' + message.type, 'py-2 small']"
      >
        {{ message.text }}
      </div>

      <div class="form-group">
        <label class="form-label small text-muted"
          >Поточна вартість (UAH/кВт)</label
        >
        <div class="input-group mb-2">
          <input
            type="number"
            step="0.01"
            v-model="tariff"
            class="form-control form-control-lg fw-bold text-primary"
          />
          <span class="input-group-text">₴</span>
        </div>
        <p class="text-muted" style="font-size: 0.75rem">
          Останнє оновлення: {{ lastUpdated }}
        </p>
      </div>

      <button
        @click="updateTariff"
        :disabled="loading"
        class="btn btn-warning w-100 fw-bold"
      >
        <span
          v-if="loading"
          class="spinner-border spinner-border-sm me-2"
        ></span>
        Оновити тариф
      </button>
    </div>
  </div>
</template>
