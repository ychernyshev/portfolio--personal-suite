<script setup>
import { computed } from "vue";
import sunnyIcon from "../../assets/images/weather_icons/light/sunny.png";
import foggyIcon from "../../assets/images/weather_icons/light/overcast.png";
import overcastIcon from "../../assets/images/weather_icons/light/overcast.png";
import partlyCloudyIcon from "../../assets/images/weather_icons/light/partly_cloudy.png";
import rainyIcon from "../../assets/images/weather_icons/light/rainy.png";

const props = defineProps({
  wmoCode: {
    type: Number,
    required: true,
  }
});

const iconSrc = computed(() => {
  const iconMap = {
    0: sunnyIcon,                  // Clear sky
    1: partlyCloudyIcon,      // Mainly clear
    2: partlyCloudyIcon,      // Partly cloudy
    3: overcastIcon,           // Overcast
    4: foggyIcon,                // Fog
    5: 'rain_slight',       // Slight rain
    6: 'thunderstorm',      // Thunderstorm
    7: 'snowy',              // Snow
    8: rainyIcon              // Rainy
  };


  const iconName = iconMap[props.wmoCode] || 'unknown';
  console.log("Icon name:", iconName);
  console.log("Icon address: ", iconSrc.value)
  return iconMap[props.wmoCode] || sunnyIcon;
});
</script>

<template>
  <img
      :src="iconSrc"
      alt="Weather Icon"
      class="weather-icon ms-2"
      style="width: 82px; height: 52px; opacity: 0.8;"
  />
</template>

<style scoped>

</style>