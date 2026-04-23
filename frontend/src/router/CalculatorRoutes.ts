import type { RouteRecordRaw } from 'vue-router';
import { RouterView } from "vue-router";

const Dashboard = () => import("@/views/calculator/Dashboard.vue");

const calculatorRoutes: RouteRecordRaw = {
    path: "/calculator",
    component: RouterView,
    // Додай meta сюди, щоб батьківський роут знав, який лейаут використовувати
    meta: { layout: "CalculatorLayout" },
    children: [
        {
            path: "",
            name: "calculator-home", // Бажано додавати імена для зручного переходу
            component: Dashboard,
            meta: { layout: "CalculatorLayout" }
        },
        {
            path: "dashboard",
            name: "calculator-dashboard",
            component: Dashboard,
            meta: { layout: "CalculatorLayout" }
        },
    ]
}

export default calculatorRoutes;