<script setup lang="ts">
import {ref, onMounted} from "vue";
import backendApi from "@/services/backendApi.ts";
import ButtonComp from "@/components/personal/ButtonComp.vue";

const tariff = ref(0);
const lastUpdated = ref("");
const loading = ref(false);
const message = ref({text: "", type: ""});

const fetchTariff = async () => {
  try {
    const res = await backendApi.get("calculator/current-tariff/");
    tariff.value = res.data.power_tariff;
    lastUpdated.value = new Date(res.data.last_updated).toLocaleString();
  } catch (e) {
    console.error("Помилка завантаження тарифу", e);
  }
};

const updateTariff = async () => {
  loading.value = true;
  message.value = {text: "", type: ""};
  try {
    await backendApi.patch("calculator/current-tariff/", {
      power_tariff: tariff.value,
    });
    message.value = {text: "Тариф успішно оновлено!", type: "success"};
    fetchTariff(); // Оновлюємо дату останньої зміни
  } catch (e) {
    message.value = {text: "Помилка при збереженні", type: "danger"};
  } finally {
    loading.value = false;
  }
};

onMounted(fetchTariff);
</script>

<template>
  <div
      v-if="message.text"
      :class="['alert', 'alert-' + message.type, 'py-2 small']"
  >
    {{ message.text }}
  </div>

  <label class="form-label pt-3 pb-3 title text-purple">
    Energy Tariff | Current Cost (UAH/kW)
  </label>

  <div class="row justify-content-center">
    <p class="text-muted label-text">
      Last update: {{ lastUpdated }}
    </p>
    <div class="col-12 col-lg-4 form-group neomorphic p-lg-0">
      <div class="row">
        <div class="col-12 col-lg-8">
          <div class="input-group m-2">
            <input
                type="number"
                step="0.01"
                v-model="tariff"
                class="form-control text-purple border-0 bg-transparent"
            />
            <span class="input-group-text bg-transparent border-0">₴</span>
          </div>
        </div>
        <div class="col-12 col-lg-4">
          <button-comp
              type="button"
              @click="updateTariff"
              :disabled="loading"
              title="Renew tariff"
              class="btn-blue-1 text-light w-100 h-100 border-radius-bottom-start-4 border-radius-bottom-end-4 border-radius-top-start-lg-0 border-radius-bottom-start-lg-0 border-radius-top-end-lg-4 rounded-md-4 ml-md-1 p-2 p-lg-0"
          />
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