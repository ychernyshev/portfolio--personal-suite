import { createRouter, createWebHistory } from "vue-router";
import calculatorRoutes from "./CalculatorRoutes.js";

const routes = [
  calculatorRoutes,
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  linkActiveClass: "text-c-primary",
  linkExactActiveClass: "text-c-primary",
});

export default router;
