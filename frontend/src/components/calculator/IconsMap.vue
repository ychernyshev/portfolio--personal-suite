<script setup>
import { computed } from "vue";
import sunnyIcon from "../../assets/images/weather_icons/light/sunny.png";
import foggyIcon from "../../assets/images/weather_icons/light/overcast.png";
import overcastIcon from "../../assets/images/weather_icons/light/overcast.png";
import partlyCloudyIcon from "../../assets/images/weather_icons/light/partly_cloudy.png";
import rainyIcon from "../../assets/images/weather_icons/light/rainy.png";
import ThunderstormIcon from "../../assets/images/weather_icons/light/rainy.png";
import SnowyIcon from "../../assets/images/weather_icons/light/rainy.png";

const props = defineProps({
  wmoCode: {
    type: [Number, String],
    required: true,
  }
});

const iconSrc = computed(() => {
  const iconMap = {
    0: sunnyIcon,                  // Clear sky
    1: partlyCloudyIcon,           // Mainly clear
    2: partlyCloudyIcon,           // Partly cloudy
    3: overcastIcon,               // Overcast
    4: foggyIcon,                  // Fog
    5: 'rain_slight',              // Slight rain
    6: 'thunderstorm',             // Thunderstorm
    7: 'snowy',                    // Snow
    8: rainyIcon,                  // Rainy
    "sunny": sunnyIcon,
    "mainly_clear": partlyCloudyIcon,
    "partly_cloudy": partlyCloudyIcon,
    "cloudy": overcastIcon,
    "foggy": foggyIcon,
    "rainy": rainyIcon,
    "rain_slight": rainyIcon,
    "thunderstorm": ThunderstormIcon,
    "snowy": SnowyIcon,

  };


  const iconName = iconMap[props.wmoCode] || 'unknown';
  console.log("Icon name:", iconName);
  console.log("Icon address: ", iconSrc)
  return iconMap[props.wmoCode] || sunnyIcon;
});
</script>

<template>
  <img
      :src="iconSrc"
      alt="Weather Icon"
      class="weather-icon ms-2 weather-icon"
  />
</template>

<style scoped>

</style>