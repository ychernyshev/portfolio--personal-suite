// src/components/calculator/IconsMap/iconsMap.js
import sunnyIcon from "../../../../public/assets/calculator/images/icons/weather/light/sunny.png";
import foggyIcon from "../../../../public/assets/calculator/images/icons/weather/light/overcast.png";
import overcastIcon from "../../../../public/assets/calculator/images/icons/weather/light/overcast.png";
import partlyCloudyIcon from "../../../../public/assets/calculator/images/icons/weather/light/partly_cloudy.png";
import rainyIcon from "../../../../public/assets/calculator/images/icons/weather/light/rainy.png";
import ThunderstormIcon from "../../../../public/assets/calculator/images/icons/weather/light/rainy.png";
import SnowyIcon from "../../../../public/assets/calculator/images/icons/weather/light/rainy.png";

export const iconMap = {
    0: sunnyIcon,
    1: partlyCloudyIcon,
    2: partlyCloudyIcon,
    3: overcastIcon,
    4: foggyIcon,
    5: rainyIcon,
    6: ThunderstormIcon,
    7: SnowyIcon,
    8: rainyIcon,
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

export function getWeatherIconSrc(code) {
    return iconMap[code] || sunnyIcon;
}
