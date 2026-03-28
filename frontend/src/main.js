import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { setupCalendar, Calendar } from 'v-calendar';
import 'v-calendar/style.css';
createApp(App).use(router).mount("#app");
