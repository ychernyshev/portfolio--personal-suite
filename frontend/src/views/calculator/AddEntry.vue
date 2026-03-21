<script setup>
import { ref, onMounted } from "vue";
import backendApi from "../../services/calculator/backendApi.js";
import WeatherIcon from "../../components/calculator/WeatherIcon.vue"; // Переконайся, що шлях правильний

const emit = defineEmits(["entry-added"]);

// 1. Початковий стан форми (копія AddEntryForm з Django)
const formData = ref({
  date: new Date().toISOString().split("T")[0],
  power: "600",
  morning_data_charge: 0,
  morning_data_price: 0,
  afternoon_data_charge: 0,
  afternoon_data_price: 0,
  evening_data_charge: 0,
  evening_data_price: 0,
  weather: [], // Сюди підуть ID обраних погодних умов
});

const weatherOptions = ref([]);

// 2. Завантажуємо типи погоди для кнопок
const fetchWeather = async () => {
  try {
    const res = await backendApi.get("weather-conditions/");
    weatherOptions.value = res.data.results || res.data;
  } catch (e) {
    console.error("Помилка завантаження типів погоди", e);
  }
};

// 3. Логіка вибору погоди (Multiple Choice)
const toggleWeather = (id) => {
  const index = formData.value.weather.indexOf(id);
  if (index > -1) {
    formData.value.weather.splice(index, 1);
  } else {
    formData.value.weather.push(id);
  }
};

// 4. Відправка форми
const submitForm = async () => {
  try {
    // Django очікує ManyToMany як список ID, formData.weather вже є таким списком
    await backendApi.post("entries/", formData.value);
    alert("Запис успішно додано!");
    emit("entry-added"); // Оновити таблицю на Дашборді
  } catch (e) {
    console.error(e.response?.data);
    alert("Помилка: " + JSON.stringify(e.response?.data));
  }
};

onMounted(fetchWeather);
</script>

<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-xxl-12">
        <div class="card shadow-sm">
          <div class="card-header bg-primary text-white">
            <h5 class="mb-0">Add New Solar Record</h5>
          </div>
          <div class="card-body">
            <form @submit.prevent="submitForm">
              <div class="row">
                <div class="col-md-6 mb-3">
                  <label class="form-label">Date</label>
                  <input
                    type="date"
                    v-model="formData.date"
                    class="form-control"
                    required
                  />
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label">System Power</label>
                  <select v-model="formData.power" class="form-select">
                    <option value="200">200</option>
                    <option value="400">400</option>
                    <option value="600">600</option>
                    <option value="800">800</option>
                  </select>
                </div>
              </div>

              <hr />

              <div class="row text-center mb-3">
                <div class="col-md-4 border-end">
                  <h6>Morning</h6>
                  <input
                    type="number"
                    v-model="formData.morning_data_charge"
                    class="form-control mb-2"
                    placeholder="Charge level"
                  />
                  <input
                    type="number"
                    step="0.01"
                    v-model="formData.morning_data_price"
                    class="form-control"
                    placeholder="Price"
                  />
                </div>
                <div class="col-md-4 border-end">
                  <h6>Afternoon</h6>
                  <input
                    type="number"
                    v-model="formData.afternoon_data_charge"
                    class="form-control mb-2"
                    placeholder="Charge level"
                  />
                  <input
                    type="number"
                    step="0.01"
                    v-model="formData.afternoon_data_price"
                    class="form-control"
                    placeholder="Price"
                  />
                </div>
                <div class="col-md-4">
                  <h6>Evening</h6>
                  <input
                    type="number"
                    v-model="formData.evening_data_charge"
                    class="form-control mb-2"
                    placeholder="Charge level"
                  />
                  <input
                    type="number"
                    step="0.01"
                    v-model="formData.evening_data_price"
                    class="form-control"
                    placeholder="Price"
                  />
                </div>
              </div>

              <div class="mb-4">
                <label class="form-label d-block text-center"
                  >Weather Indicators</label
                >
                <div class="d-flex justify-content-center gap-2">
                  <div
                    v-for="opt in weatherOptions"
                    :key="opt.id"
                    @click="toggleWeather(opt.id)"
                    class="p-2 border rounded text-center cursor-pointer weather-btn"
                    :class="{
                      'bg-primary text-white border-primary shadow':
                        formData.weather.includes(opt.id),
                    }"
                    style="min-width: 80px"
                  >
                    <WeatherIcon :name="opt.name" />
                    <div class="small text-capitalize">{{ opt.name }}</div>
                  </div>
                </div>
              </div>

              <button type="submit" class="btn btn-success w-100 py-2">
                Save Record
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.weather-btn {
  transition: all 0.2s;
  cursor: pointer;
}
.weather-btn:hover {
  border-color: #0d6efd;
}
</style>
