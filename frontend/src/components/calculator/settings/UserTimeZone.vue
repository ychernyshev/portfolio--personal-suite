<script setup lang="ts">
  import {onMounted} from "vue";
  import {useOpenMeteoForecastStore} from "../../../../store/useOpenMeteoForecastStore";
  import {storeToRefs} from "pinia";

  const browserCoordinates = useOpenMeteoForecastStore();
  const { browserLat, browserLon, dbLat, dbLon, detectedTimezone } = storeToRefs(browserCoordinates);

  onMounted(async () => {
    await browserCoordinates.fetchDbCoordinates();

    let lat, lon

    if (dbLat.value && dbLon.value) {
      lat = dbLat.value;
      lon = dbLon.value;
    } if (browserLat.value && browserLon.value) {
      lat = browserLat.value;
      lon = browserLon.value;
    } else {
      const coords = await browserCoordinates.getUserCoordinates();
      if (coords) {
        lat = coords.lat;
        lon = coords.lon;
      }
    }

    if (lat && lon) {
      await browserCoordinates.detectTimezone(lat, lon);
    }
  });

  // + Дані з БД
  // + Якщо немає - дані з браузера
  // - Вказати time zone
  // - Шукати за назвою
</script>

<template>
  <div class="timezone-wrapper mt-3 mb-3 text-start">
    <p class="mb-1 fw-medium text-purple">User Time Zone</p>
    <div class="row">
      <div class="col-12 pt-3 pb-3">
        <form action="" class="row">
          detectedTimezone: {{detectedTimezone}}
          <input
              v-model=detectedTimezone
              type="text"
              class="form-control"
              placeholder="Determining timezone..."
          />
          <small class="text-muted">Detected based on your coordinates</small>
<!--          <small class="text-muted">Select your time zone</small>-->
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>