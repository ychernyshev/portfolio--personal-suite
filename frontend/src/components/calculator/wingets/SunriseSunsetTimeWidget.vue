<script setup>
import {onMounted, ref, watch} from 'vue';
import {storeToRefs} from 'pinia';
import {useMessagesStore} from '../../../../store/useMessagesStore.js';

const messageStore = useMessagesStore();
const {loading, currentForecast, formatTime} = storeToRefs(messageStore);

const currentDateTime = ref(messageStore.getCurrentDateTimeISO());

watch(currentDateTime, (newDateTime) => {
  messageStore.fetchMessagesForDate(newDateTime);
});

onMounted(() => {
  messageStore.fetchMessagesForDate(currentDateTime.value);
});
</script>

<!--<template>-->
<!--  <div class="neomorphic ps-4 pe-4 pt-3 pb-3">-->
<!--    <div v-if="loading" class="widget-loading">-->
<!--      <span>Updating solar times...</span>-->
<!--    </div>-->

<!--    <div v-else-if="currentForecast" class="widget-content">-->
<!--      <div class="time-block d-flex align-items-end">-->
<!--        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-sunrise-fill text-warning-1 mb-1"-->
<!--             viewBox="0 0 16 16">-->
<!--          <path-->
<!--              d="M7.646 1.146a.5.5 0 0 1 .708 0l1.5 1.5a.5.5 0 0 1-.708.708L8.5 2.707V4.5a.5.5 0 0 1-1 0V2.707l-.646.647a.5.5 0 1 1-.708-.708zM2.343 4.343a.5.5 0 0 1 .707 0l1.414 1.414a.5.5 0 0 1-.707.707L2.343 5.05a.5.5 0 0 1 0-.707m11.314 0a.5.5 0 0 1 0 .707l-1.414 1.414a.5.5 0 1 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0M11.709 11.5a4 4 0 1 0-7.418 0H.5a.5.5 0 0 0 0 1h15a.5.5 0 0 0 0-1h-3.79zM0 10a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2A.5.5 0 0 1 0 10m13 0a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/>-->
<!--        </svg>-->
<!--        <div class="info">-->
<!--          <span class="label text-purple">Sunrise</span>-->
<!--          <span class="time ">{{ formatTime(currentForecast.sunrise) }}</span>-->
<!--        </div>-->
<!--      </div>-->

<!--      {{ currentForecast.day_length }}-->
<!--      <div class="time-divider"></div>-->

<!--      <div class="time-block d-flex align-items-end">-->
<!--        <div class="info">-->
<!--          <span class="label text-purple">Sunset</span>-->
<!--          <span class="time ">{{ formatTime(currentForecast.sunset) }}</span>-->
<!--        </div>-->
<!--        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-sunset-fill text-warning-2 mb-1"-->
<!--             viewBox="0 0 16 16">-->
<!--          <path-->
<!--              d="M7.646 4.854a.5.5 0 0 0 .708 0l1.5-1.5a.5.5 0 0 0-.708-.708l-.646.647V1.5a.5.5 0 0 0-1 0v1.793l-.646-.647a.5.5 0 1 0-.708.708zm-5.303-.51a.5.5 0 0 1 .707 0l1.414 1.413a.5.5 0 0 1-.707.707L2.343 5.05a.5.5 0 0 1 0-.707zm11.314 0a.5.5 0 0 1 0 .706l-1.414 1.414a.5.5 0 1 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zM11.709 11.5a4 4 0 1 0-7.418 0H.5a.5.5 0 0 0 0 1h15a.5.5 0 0 0 0-1h-3.79zM0 10a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2A.5.5 0 0 1 0 10m13 0a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/>-->
<!--        </svg>-->
<!--      </div>-->
<!--    </div>-->

<!--    <div v-else class="widget-empty">-->
<!--      <span>No data for today</span>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<template>
  <div class="neomorphic">
    <div v-if="loading" class="widget-loading">
      <span>Updating solar times...</span>
    </div>

    <div v-else-if="currentForecast" class="widget-content">
      <div class="time-block d-flex align-items-end">
        <svg xmlns="http://www.w3.org/2000/svg"
             width="30" height="30"
             fill="currentColor"
             class="bi bi-sunrise-fill text-warning-1 mb-1"
             viewBox="0 0 16 16">
          <path
              d="M7.646 1.146a.5.5 0 0 1 .708 0l1.5 1.5a.5.5 0 0 1-.708.708L8.5 2.707V4.5a.5.5 0 0 1-1 0V2.707l-.646.647a.5.5 0 1 1-.708-.708zM2.343 4.343a.5.5 0 0 1 .707 0l1.414 1.414a.5.5 0 0 1-.707.707L2.343 5.05a.5.5 0 0 1 0-.707m11.314 0a.5.5 0 0 1 0 .707l-1.414 1.414a.5.5 0 1 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0M11.709 11.5a4 4 0 1 0-7.418 0H.5a.5.5 0 0 0 0 1h15a.5.5 0 0 0 0-1h-3.79zM0 10a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2A.5.5 0 0 1 0 10m13 0a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/>
        </svg>
        <div class="info">
          <span class="label text-center">Sunrise</span>
          <span class="time">{{ formatTime(currentForecast.sunrise) }}</span>
        </div>
      </div>

      <div class="time-divider"></div>
      <div class="d-flex flex-column">
        <span class="label text-center">Day Length</span>
        <span class="length-value time">
          {{ currentForecast.day_length ? currentForecast.day_length.toFixed(2) : 0 }}
        </span>
      </div>
      <div class="time-divider"></div>

      <div class="time-block d-flex align-items-end">
        <div class="info">
          <span class="label text-center">Sunset</span>
          <span class="time">{{ formatTime(currentForecast.sunset) }}</span>
        </div>
        <svg xmlns="http://www.w3.org/2000/svg"
             width="30" height="30"
             fill="currentColor"
             class="bi bi-sunset-fill text-warning-2 mb-1"
             viewBox="0 0 16 16">
          <path
              d="M7.646 4.854a.5.5 0 0 0 .708 0l1.5-1.5a.5.5 0 0 0-.708-.708l-.646.647V1.5a.5.5 0 0 0-1 0v1.793l-.646-.647a.5.5 0 1 0-.708.708zm-5.303-.51a.5.5 0 0 1 .707 0l1.414 1.413a.5.5 0 0 1-.707.707L2.343 5.05a.5.5 0 0 1 0-.707zm11.314 0a.5.5 0 0 1 0 .706l-1.414 1.414a.5.5 0 1 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zM11.709 11.5a4 4 0 1 0-7.418 0H.5a.5.5 0 0 0 0 1h15a.5.5 0 0 0 0-1h-3.79zM0 10a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2A.5.5 0 0 1 0 10m13 0a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/>
        </svg>
      </div>
    </div>

    <div v-else class="widget-empty">
      <span>No data for today</span>
    </div>
  </div>
</template>

<style scoped>
.sun-widget {
  background: rgba(255, 255, 255, 0.45);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.6);
  border-radius: 16px;
  padding: 12px 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.03);
}

.widget-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.time-block {
  display: flex;
  align-items: center;
  gap: 8px;
}

.icon {
  font-size: 1.4rem;
}

.info {
  display: flex;
  flex-direction: column;
}

.label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.time {
  font-size: 1.85rem;
  font-weight: 400;
  color: var(--sky-blue-3);
}

.time-divider {
  width: 1px;
  height: 24px;
  background: rgba(0, 0, 0, 0.08);
}

.widget-loading, .widget-empty {
  text-align: center;
  font-size: 0.85rem;
  color: #7b8a9b;
  padding: 4px 0;
}
</style>