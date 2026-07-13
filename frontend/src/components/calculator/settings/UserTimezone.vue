<script setup lang="ts">
import {onMounted, ref} from "vue";
  import {useOpenMeteoForecastStore} from "../../../../store/useOpenMeteoForecastStore";
  import {storeToRefs} from "pinia";
import ButtonComp from "@/components/personal/ButtonComp.vue";

  const browserCoordinates = useOpenMeteoForecastStore();
  const { browserLat, browserLon, dbLat, dbLon, detectedTimezone, storedTimezone, fetchTimezone } = storeToRefs(browserCoordinates);
  const cityName = ref("");
  const message = ref({})

  const timezones = [
    { offset: -12, label: "(UTC-12:00) International Date Line West", zone: "Etc/GMT+12" },
    { offset: -11, label: "(UTC-11:00) Midway Island, Samoa", zone: "Pacific/Midway" },
    { offset: -10, label: "(UTC-10:00) Hawaii", zone: "Pacific/Honolulu" },
    { offset: -9,  label: "(UTC-09:00) Alaska", zone: "America/Anchorage" },
    { offset: -8,  label: "(UTC-08:00) Pacific Time (LA, Vancouver)", zone: "America/Los_Angeles" },
    { offset: -7,  label: "(UTC-07:00) Mountain Time (Denver, Phoenix)", zone: "America/Denver" },
    { offset: -6,  label: "(UTC-06:00) Central Time (Chicago, Mexico City)", zone: "America/Chicago" },
    { offset: -5,  label: "(UTC-05:00) Eastern Time (NY, Toronto, Lima)", zone: "America/New_York" },
    { offset: -4,  label: "(UTC-04:00) Caracas, Santiago, Halifax", zone: "America/Santiago" },
    { offset: -3,  label: "(UTC-03:00) Brasilia, Buenos Aires, Greenland", zone: "America/Argentina/Buenos_Aires" },
    { offset: -2,  label: "(UTC-02:00) Mid-Atlantic", zone: "Etc/GMT+2" },
    { offset: -1,  label: "(UTC-01:00) Azores, Cape Verde", zone: "Atlantic/Azores" },
    { offset: 0,   label: "(UTC+00:00) London, Lisbon, Casablanca", zone: "Europe/London" },
    { offset: 1,   label: "(UTC+01:00) Paris, Berlin, Rome, Lagos", zone: "Europe/Paris" },
    { offset: 2,   label: "(UTC+02:00) Kyiv, Cairo, Johannesburg", zone: "Europe/Kyiv" },
    { offset: 3,   label: "(UTC+03:00) Istanbul, Moscow, Nairobi, Riyadh", zone: "Europe/Istanbul" },
    { offset: 4,   label: "(UTC+04:00) Dubai, Baku, Tbilisi", zone: "Asia/Dubai" },
    { offset: 5,   label: "(UTC+05:00) Karachi, Tashkent", zone: "Asia/Karachi" },
    { offset: 6,   label: "(UTC+06:00) Dhaka, Almaty", zone: "Asia/Dhaka" },
    { offset: 7,   label: "(UTC+07:00) Bangkok, Jakarta, Hanoi", zone: "Asia/Bangkok" },
    { offset: 8,   label: "(UTC+08:00) Beijing, Singapore, Perth", zone: "Asia/Shanghai" },
    { offset: 9,   label: "(UTC+09:00) Tokyo, Seoul", zone: "Asia/Tokyo" },
    { offset: 10,  label: "(UTC+10:00) Sydney, Melbourne, Vladivostok", zone: "Australia/Sydney" },
    { offset: 11,  label: "(UTC+11:00) Solomon Is., New Caledonia", zone: "Pacific/Guadalcanal" },
    { offset: 12,  label: "(UTC+12:00) Auckland, Fiji", zone: "Pacific/Auckland" },
  ];

  const handleCitySearch = async () => {
    if (!cityName.value || cityName.value.length < 2) return;

    const result = await browserCoordinates.searchCity(cityName.value);

    if (result) {
      detectedTimezone.value = result.timezone;
      browserLat.value = result.lat;
      browserLon.value = result.lon;
    } else {
      message.value = { text: 'Error saving timezone.', type: 'danger' };
    }
  };

const handleSave = async () => {
  await browserCoordinates.saveTimezone(detectedTimezone.value);
};

  onMounted(async () => {
    await browserCoordinates.fetchTimezone();
    await browserCoordinates.fetchDbCoordinates();

    if (dbLat.value && dbLon.value) {
      await browserCoordinates.detectTimezone(dbLat.value, dbLon.value);
    } else if (browserLat.value && browserLon.value) {
      await browserCoordinates.detectTimezone(browserLat.value, browserLon.value);
    } else {
      const coords = await browserCoordinates.getUserCoordinates();
      if (coords) {
        await browserCoordinates.detectTimezone(coords.lat, coords.lon);
      }
    }
  });

  // - Use the Geocoding API to enter a city name in multiple languages
</script>

<template>
  <div class="timezone-wrapper mt-3 mb-3 text-start">
    <p class="mb-1 fw-medium text-purple">User's Power Station Time Zone</p>
    <div class="row">
      <div class="col-12 pt-3 pb-3">
        <form action="">
          <small class="text-muted">Your timezone has been detected based on your browser coordinates</small>
          <div class="row neomorphic p-0 mt-2">
            <div class="col-12 col-lg-10">
              <div class="row">
                <div class="col-12 col-lg-3 mb-2 mb-lg-0 d-flex justify-content-center align-items-center">
                  <p class="my-auto" disabled>
                    {{detectedTimezone}}
                  </p>
                </div>
                <div class="col-12 col-lg-4 mb-2 mb-lg-0 pl-lg-0 pr-lg-0 d-flex justify-content-center align-items-center">
                  <select v-model="detectedTimezone" class="form-select bg-transparent border-0">
                    <option value="" disabled>Select your time zone...</option>
                    <option
                        v-for="zone in timezones"
                        :key="zone.zone"
                        :value="zone.zone"
                        class="my-auto"
                    >
                      {{ zone.label }}
                    </option>
                  </select>
                </div>
                <div class="col-12 col-lg-5 mb-2 mb-lg-0 d-flex flex-row pl-lg-0 pr-lg-0 d-flex justify-content-center align-items-center">
                  <span class="ml-lg-3 mr-lg-3 my-auto">or</span>
                  <div class="input-group my-auto">
                    <input
                        v-model="cityName"
                        @keyup.prevent="handleCitySearch"
                        type="text"
                        class="form-control bg-transparent border-0 my-auto"
                        placeholder="Enter the name of your settlement"
                    />
                    <button @click="handleCitySearch" class="btn btn-info right-angle p-3" type="button">
                      Find
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-12 col-lg-2 pl-lg-0 pr-lg-0">
              <button-comp @click=handleSave
                           type="button"
                           title="Set Timezone"
                           class="btn-blue-1 text-light w-100 h-100 border-radius-bottom-start-4 border-radius-bottom-end-4 border-radius-top-start-lg-0 border-radius-bottom-start-lg-0 border-radius-top-end-lg-4 rounded-md-4" />
            </div>
          </div>
          <div class="row mt-2">
            <div class="col-lg-3"></div>
            <div class="col-lg-4 pl-lg-0 pr-lg-0">
              <small class="text-muted">Select your time zone through numbers</small>
            </div>
          </div>
        </form>
        <div class="row">
          <div class="col-12 pt-3">
            <div class="lat-lon-text mb-2 text-md-start">
            </div>
            <div class="row justify-content-center">
              <div class="col-6 col-lg-3 bg-gradient-blue-2 p-3 text-white fw-bold text-center">
                <span class="">Stored Power Station Timezone</span>
              </div>
              <div class="col-6 col-lg-3 p-3 text-center bg-body-tertiary">
                <span v-if="storedTimezone">
                  {{ storedTimezone || 'Loading...' }}
                </span>
                <span v-else>Add you your timezone</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>