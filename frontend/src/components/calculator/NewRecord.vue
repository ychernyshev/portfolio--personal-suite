<script setup>
import { ref, onMounted } from "vue";
import backendApi from "../../services/calculator/backendApi.js";
import WeatherIcon from "./WeatherIcon.vue";

const emit = defineEmits(["entry-added"]);

const formData = ref({
  date: new Date().toISOString().split("T")[0],
  power: "600",
  morning_data_charge: 0,
  morning_data_price: 0,
  afternoon_data_charge: 0,
  afternoon_data_price: 0,
  evening_data_charge: 0,
  evening_data_price: 0,
  weather: [],
});

const weatherOptions = ref([]);

const fetchWeather = async () => {
  try {
    const res = await backendApi.get("weather-conditions/");
    weatherOptions.value = res.data.results || res.data;
  } catch (e) {
    console.error("Помилка завантаження типів погоди", e);
  }
};

const toggleWeather = (id) => {
  const index = formData.value.weather.indexOf(id);
  if (index > -1) {
    formData.value.weather.splice(index, 1);
  } else {
    formData.value.weather.push(id);
  }
};

const submitForm = async () => {
  try {
    await backendApi.post("entries/", formData.value);
    alert("Запис успішно додано!");
    emit("entry-added");
  } catch (e) {
    console.error(e.response?.data);
    alert("Помилка: " + JSON.stringify(e.response?.data));
  }
};

onMounted(fetchWeather);
</script>

<template>
  <div class="card shadow-sm border-0">
    <div class="card-body card-light pl-3 pr-3 pb-2">
      <form @submit.prevent="submitForm">
        <div class="row mt-1">
          <div class="col-md-6 mt-3 mb-2">
            <label class="form-label">Date</label>
            <input
                type="date"
                v-model="formData.date"
                class="form-control"
                required
            />
          </div>
          <div class="col-md-6 mt-3 mb-2">
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

        <div class="row text-center mb-2">
          <div class="col-md-4 border-end">
            <div class="time-section mb-4 p-3">
              <h6 class="text-success fw-bold mb-3">Morning</h6>
                <div class="input-group w-100 mb-2">
                  <span class="input-group-text bg-white border-end-0 rounded-start-3 text-muted p-0 pl-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#6c757d" viewBox="0 0 16 16">
                      <path d="M2 6h10v4H2V6z"/>
                      <path d="M2 4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2H2zm10 1a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h10zm4 3a1.5 1.5 0 0 1-1.5 1.5v-3A1.5 1.5 0 0 1 16 8z"/>
                    </svg>
                  </span>
                  <input
                      type="number"
                      step="any"
                      class="form-control border-start-0 rounded-end-3"
                      placeholder="0"
                      v-model="formData.morning_data_charge"
                  >
                  <span class="input-group-text bg-transparent border-0 small text-muted pe-2" style="width: 1%">%</span>
                </div>
                <div class="input-group w-100">
                  <span class="input-group-text bg-white border-end-0 rounded-start-3 text-muted p-0 pl-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#f1c40f" viewBox="0 0 16 16">
                      <path d="M5.5 9.511c.076.04.16.08.252.117a18.721 18.721 0 0 0 2.248.707V12.5c0 .017.001.033.001.05a10.39 10.39 0 0 0 2.248-.707c.417-.147.756-.323 1.001-.518V9.51a10.39 10.39 0 0 0 2.248-.707c.417-.147.756-.323 1.001-.518v3.018c0 .697-.463 1.442-1.26 1.956C12.192 13.754 10.916 14 9.5 14c-1.416 0-2.692-.246-3.488-.744-.797-.514-1.26-1.259-1.26-1.956V9.511z"/>
                      <path d="M14 6.5c0 .697-.463 1.442-1.26 1.956C11.942 8.954 10.666 9.2 9.5 9.2c-1.416 0-2.692-.246-3.488-.744C5.215 7.942 4.75 7.197 4.75 6.5c0-.697.463-1.442 1.26-1.956C6.808 4.046 8.084 3.8 9.5 3.8c1.416 0 2.692.246 3.488.744.797.514 1.26 1.259 1.26 1.956z"/>
                      <path d="M9.5 10c-1.416 0-2.692-.246-3.488-.744C5.215 8.742 4.75 7.997 4.75 7.3V9.5c0 .697.463 1.442 1.26 1.956C6.808 11.954 8.084 12.2 9.5 12.2c1.416 0 2.692-.246 3.488-.744.797-.514 1.26-1.259 1.26-1.956V7.3c0 .697-.463 1.442-1.26 1.956C12.192 9.754 10.916 10 9.5 10z"/>
                    </svg>
                    </span>
                  <input
                      type="number"
                      step="any"
                      class="form-control border-start-0 rounded-end-3"
                      placeholder="0.00"
                      v-model="formData.morning_data_price"
                  >
                  <span class="input-group-text bg-transparent border-0 small text-muted pe-2" style="width: 1%">₴</span>
                </div>
            </div>
          </div>
          <div class="col-md-4 border-end">
            <div class="time-section mb-4 p-3">
              <h6 class="text-primary fw-bold mb-3">Afternoon</h6>
              <div class="input-group w-100 mb-2">
                  <span class="input-group-text bg-white border-end-0 rounded-start-3 text-muted p-0 pl-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#6c757d" viewBox="0 0 16 16">
                      <path d="M2 6h10v4H2V6z"/>
                      <path d="M2 4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2H2zm10 1a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h10zm4 3a1.5 1.5 0 0 1-1.5 1.5v-3A1.5 1.5 0 0 1 16 8z"/>
                    </svg>
                  </span>
                <input
                    type="number"
                    step="any"
                    class="form-control border-start-0 rounded-end-3"
                    placeholder="0"
                    v-model="formData.afternoon_data_charge"
                >
                <span class="input-group-text bg-transparent border-0 small text-muted pe-2" style="width: 1%">%</span>
              </div>
              <div class="input-group w-100">
                  <span class="input-group-text bg-white border-end-0 rounded-start-3 text-muted p-0 pl-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#f1c40f" viewBox="0 0 16 16">
                      <path d="M5.5 9.511c.076.04.16.08.252.117a18.721 18.721 0 0 0 2.248.707V12.5c0 .017.001.033.001.05a10.39 10.39 0 0 0 2.248-.707c.417-.147.756-.323 1.001-.518V9.51a10.39 10.39 0 0 0 2.248-.707c.417-.147.756-.323 1.001-.518v3.018c0 .697-.463 1.442-1.26 1.956C12.192 13.754 10.916 14 9.5 14c-1.416 0-2.692-.246-3.488-.744-.797-.514-1.26-1.259-1.26-1.956V9.511z"/>
                      <path d="M14 6.5c0 .697-.463 1.442-1.26 1.956C11.942 8.954 10.666 9.2 9.5 9.2c-1.416 0-2.692-.246-3.488-.744C5.215 7.942 4.75 7.197 4.75 6.5c0-.697.463-1.442 1.26-1.956C6.808 4.046 8.084 3.8 9.5 3.8c1.416 0 2.692.246 3.488.744.797.514 1.26 1.259 1.26 1.956z"/>
                      <path d="M9.5 10c-1.416 0-2.692-.246-3.488-.744C5.215 8.742 4.75 7.997 4.75 7.3V9.5c0 .697.463 1.442 1.26 1.956C6.808 11.954 8.084 12.2 9.5 12.2c1.416 0 2.692-.246 3.488-.744.797-.514 1.26-1.259 1.26-1.956V7.3c0 .697-.463 1.442-1.26 1.956C12.192 9.754 10.916 10 9.5 10z"/>
                    </svg>
                    </span>
                <input
                    type="number"
                    step="any"
                    class="form-control border-start-0 rounded-end-3"
                    placeholder="0.00"
                    v-model="formData.afternoon_data_price"
                >
                <span class="input-group-text bg-transparent border-0 small text-muted pe-2" style="width: 1%">₴</span>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="time-section mb-4 p-3">
              <h6 class="text-purple fw-bold mb-3">Evening</h6>
              <div class="input-group w-100 mb-2">
                  <span class="input-group-text bg-white border-end-0 rounded-start-3 text-muted p-0 pl-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#6c757d" viewBox="0 0 16 16">
                      <path d="M2 6h10v4H2V6z"/>
                      <path d="M2 4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2H2zm10 1a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h10zm4 3a1.5 1.5 0 0 1-1.5 1.5v-3A1.5 1.5 0 0 1 16 8z"/>
                    </svg>
                  </span>
                <input
                    type="number"
                    step="any"
                    class="form-control border-start-0 rounded-end-3"
                    placeholder="0"
                    v-model="formData.evening_data_charge"
                >
                <span class="input-group-text bg-transparent border-0 small text-muted pe-2" style="width: 1%">%</span>
              </div>
              <div class="input-group w-100">
                  <span class="input-group-text bg-white border-end-0 rounded-start-3 text-muted p-0 pl-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#f1c40f" viewBox="0 0 16 16">
                      <path d="M5.5 9.511c.076.04.16.08.252.117a18.721 18.721 0 0 0 2.248.707V12.5c0 .017.001.033.001.05a10.39 10.39 0 0 0 2.248-.707c.417-.147.756-.323 1.001-.518V9.51a10.39 10.39 0 0 0 2.248-.707c.417-.147.756-.323 1.001-.518v3.018c0 .697-.463 1.442-1.26 1.956C12.192 13.754 10.916 14 9.5 14c-1.416 0-2.692-.246-3.488-.744-.797-.514-1.26-1.259-1.26-1.956V9.511z"/>
                      <path d="M14 6.5c0 .697-.463 1.442-1.26 1.956C11.942 8.954 10.666 9.2 9.5 9.2c-1.416 0-2.692-.246-3.488-.744C5.215 7.942 4.75 7.197 4.75 6.5c0-.697.463-1.442 1.26-1.956C6.808 4.046 8.084 3.8 9.5 3.8c1.416 0 2.692.246 3.488.744.797.514 1.26 1.259 1.26 1.956z"/>
                      <path d="M9.5 10c-1.416 0-2.692-.246-3.488-.744C5.215 8.742 4.75 7.997 4.75 7.3V9.5c0 .697.463 1.442 1.26 1.956C6.808 11.954 8.084 12.2 9.5 12.2c1.416 0 2.692-.246 3.488-.744.797-.514 1.26-1.259 1.26-1.956V7.3c0 .697-.463 1.442-1.26 1.956C12.192 9.754 10.916 10 9.5 10z"/>
                    </svg>
                    </span>
                <input
                    type="number"
                    step="any"
                    class="form-control border-start-0 rounded-end-3"
                    placeholder="0.00"
                    v-model="formData.evening_data_price"
                >
                <span class="input-group-text bg-transparent border-0 small text-muted pe-2" style="width: 1%">₴</span>
              </div>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-xxl-4">
            <div class="time-section mb-1 pl-3 pr-3">
              <label class="form-label d-block text-center">
                Extra power (from USB)
              </label>
              <div class="input-group w-100 my-4">
                  <span class="input-group-text bg-white border-end-0 rounded-start-3 text-muted p-0 pl-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#6f42c1" viewBox="0 0 16 16">
                      <path d="M5.52.359A.5.5 0 0 1 6 0h4a.5.5 0 0 1 .474.658L8.694 6H12.5a.5.5 0 0 1 .395.807l-7 9a.5.5 0 0 1-.873-.454L6.823 9.5H3.5a.5.5 0 0 1-.48-.641l2.5-8.5zM6.374 1 4.168 8.5H7.5a.5.5 0 0 1 .478.647L6.78 13.04 11.478 7H8a.5.5 0 0 1-.474-.658L9.306 1H6.374z"/>
                      <path fill-rule="evenodd" d="M12.5 11a.5.5 0 0 1 .5.5v1.5h1.5a.5.5 0 0 1 0 1H13v1.5a.5.5 0 0 1-1 0V14h-1.5a.5.5 0 0 1 0-1H12v-1.5a.5.5 0 0 1 .5-.5z"/>
                    </svg>
                  </span>
                <input
                    type="number"
                    step="any"
                    class="form-control border-start-0 rounded-end-3"
                    placeholder="0"

                >
                <span class="input-group-text bg-transparent border-0 small text-muted pe-2" style="width: 1%; font-size: .7rem">Wh</span>
              </div>
            </div>
          </div>
          <div class="col-xxl-4">
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
          <div class="col-xxl-4">
            <div class="time-section">
              <label class="form-label d-block text-center"
              >Form controllers</label
              >
              <div class="btn-group my-3" role="group" aria-label="Basic example">
                <button type="button" class="btn btn-light mb-1 w-10 py-2">Clear form</button>
                <button type="submit" class="btn btn-success mb-1 w-10 py-2">
                  Add Record
                </button>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
