<script setup>
import { ref, onMounted, nextTick } from 'vue';
import backendApi from "../../../services/calculator/backendApi.js";
import IconsMap from "../IconsMap.vue";
import Productivity from "./Productivity.vue";
import MiniCalendar from "./MiniCalendar.vue";

const forecast = ref(null);
const loading = ref(true);
const showCalendar = ref(false);

const fetchForecast = async () => {
  try {
    const response = await backendApi.get('solar-forecast/');
    forecast.value = response.data;
  } catch (error) {
    console.error("Error retrieving forecast:", error);
  } finally {
    loading.value = false;
  }
};

// Mini calendar
const showDetailChart = ref(false);
const activeDate = ref(null);

const onDatePicked = (day) => {
  activeDate.value = day;
  showDetailChart.value = true;
};

onMounted(() => {
   fetchForecast();
});
</script>

<template>
  <div class="card border-0 neomorphic" style="width: 45rem">
    <div class="row" v-if="!loading && forecast">
      <div class="col-xxl-6 border-right">
        <h4 class="text-muted" style="font-weight: 200">Forecast: Today</h4>
<!--        <small class="text-muted">Click a date to see comparison</small>-->
        <div class="d-flex justify-content-between align-items-center">
          <div>
            <h2 class="text-sky-blue-4">{{ forecast.predicted_total_kwh }} kWh</h2>
            <p class="text-success mb-0">+{{ forecast.predicted_savings }} UAH savings</p>
          </div>
          <div class="text-muted small">
            <div class="text-end">
              Peak: {{ forecast.peak_hour }}:00
            </div>
            <h2 class="mb-0">{{ forecast.current_temp }}°C</h2>
            <p class="text-muted small mb-1 text-end">{{ forecast.weather_condition }}</p>
          </div>
        </div>
        <div class="d-flex justify-content-between align-items-center mt-2">
          <div class="position-relative d-inline-block d-flex flex-row">
            <button @click="showCalendar = !showCalendar" class="btn btn-success btn-sm text-light  ">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar3" viewBox="0 0 16 16">
                <path d="M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2M1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857z"/>
                <path d="M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2"/>
              </svg>
              calendar
            </button>

            <transition v-if="showCalendar" class="custom-tooltip-box" name="fade-slide" mode="out-in">
                <mini-calendar
                    transparent
                    borderless
                    trim-weeks
                    :attributes="attributes"
                    @dayclick="onDayClick"
                    locale="uk"
                    class="calendar-card w-100"
                />
            </transition>
          </div>
          <!--        MODAL-->
          <div class="d-flex justify-content-start">
<!--            <button>-->
<!--              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar3" viewBox="0 0 16 16">-->
<!--                <path d="M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2M1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857z"/>-->
<!--                <path d="M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2"/>-->
<!--              </svg>-->
<!--            </button>-->

            <!--            <button type="button" class="btn btn-light btn-c-light btn-sm d-flex align-items-center justify-content-center text-purple" data-bs-toggle="modal" data-bs-target="#exampleModal">-->
<!--              <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-table pr-2" viewBox="0 0 16 16">-->
<!--                <path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 2h-4v3h4zm0 4h-4v3h4zm0 4h-4v3h3a1 1 0 0 0 1-1zm-5 3v-3H6v3zm-5 0v-3H1v2a1 1 0 0 0 1 1zm-4-4h4V8H1zm0-4h4V4H1zm5-3v3h4V4zm4 4H6v3h4z"/>-->
<!--              </svg> comparison table-->
<!--            </button>-->
          </div>

          <!-- Modal -->
          <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
              <div class="modal-content">
                <div class="modal-header">
                  <h1 class="modal-title fs-5" id="exampleModalLabel">Comparison table of actual and real solar energy production rates</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <productivity/>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
              </div>
            </div>
          </div>

          <!--        END MODAL-->
          <icons-map
              v-if="forecast"
              :wmoCode="forecast.weather_code"
              style="width: 82px; height: 52px; opacity: 0.8;"
          />
        </div>
      </div>
      <div class="col-xxl-6">
        <div class="flex-grow-1 ps-4 position-relative d-flex align-items-center justify-content-center">
          <div v-if="!showDetailChart" class="w-100 text-center">
            <div id="mini-calendar"></div>

          </div>

          <div v-else class="w-100 h-100">
          </div>
        </div>
      </div>
    </div>
    <div v-else-if="loading" class="text-center p-3">
      <span>Loading forecast...</span>
    </div>
  </div>
</template>

<style scoped>
.calendar-card {
  position: relative;
  overflow: visible;
  height: 100%;
}

.custom-tooltip-box {
  position: absolute;
  z-index: 1050;
  top: 130%;
  left: 50%;
  transform: translateX(-50%);
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateX(-50%) translateY(-10px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateX(-50%) translateY(-10px);
}
</style>