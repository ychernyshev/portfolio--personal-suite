import { createRouter, createWebHistory } from "vue-router";
import personalRoutes from "./PersonalRoutes";

const routes = [
  personalRoutes,
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  linkActiveClass: "text-c-primary",
  linkExactActiveClass: "text-c-primary",
});

export default router;
