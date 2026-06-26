<script setup>
import { onMounted, ref, watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useMessagesStore } from '../../../../store/useMessagesStore';

const messageStore = useMessagesStore();
const { loading, currentForecast, formatTime } = storeToRefs(messageStore);

const currentDateTime = ref(messageStore.getCurrentDateTimeISO());

watch(currentDateTime, (newDateTime) => {
  messageStore.fetchMessagesForDate(newDateTime);
});

onMounted(() => {
  messageStore.fetchMessagesForDate(currentDateTime.value);
});
</script>

<template>
  <div>
    <p v-if="loading">Loading solar data...</p>

    <div v-else-if="currentForecast">
      <p>Sunrise: {{ formatTime(currentForecast.sunrise) }}</p>
      <p>Sunset: {{ formatTime(currentForecast.sunset) }}</p>
    </div>

    <p v-else>No tracking data available for today.</p>
  </div>
</template>