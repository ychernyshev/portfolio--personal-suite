// SPDX-License-Identifier: AGPL-3.0-or-later
import type { RouteRecordRaw } from 'vue-router';
import { RouterView } from "vue-router";

const Dashboard = () => import("@/views/calculator/Dashboard.vue");

const calculatorRoutes: RouteRecordRaw = {
    path: "/calculator",
    component: RouterView,
    meta: { layout: "CalculatorLayout" },
    children: [
        {
            path: "",
            name: "calculator-home",
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