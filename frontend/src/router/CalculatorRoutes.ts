import type { RouteRecordRaw } from 'vue-router';
import { RouterView } from "vue-router";

const calculatorRoutes: RouteRecordRaw = {
    path: "/calculator",
    component: RouterView,
    // Додай meta сюди, щоб батьківський роут знав, який лейаут використовувати
    meta: { layout: "CalculatorLayout" },
    children: [
        {
            path: "",
            name: "calculator-home", // Бажано додавати імена для зручного переходу
            component: () => import("../views/calculator/Dashboard.vue"),
            meta: { layout: "CalculatorLayout" }
        },
        {
            path: "dashboard",
            name: "calculator-dashboard",
            component: () => import("../views/calculator/Dashboard.vue"),
            meta: { layout: "CalculatorLayout" }
        },
        {
            path: "add_entry",
            name: "calculator-add",
            component: () => import("../components/calculator/NewRecord.vue"),
            meta: { layout: "CalculatorLayout" }
        },
        {
            path: "settings",
            name: "calculator-settings",
            component: () => import("../components/calculator/Settings.vue"),
            meta: { layout: "CalculatorLayout" }
        },
    ]
}

export default calculatorRoutes;