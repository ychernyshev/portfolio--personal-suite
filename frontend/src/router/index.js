import { createRouter, createWebHistory } from "vue-router";
import dashboard from "../views/Dashboard.vue";
import add_entry from "../views/AddEntry.vue";
import settings from "../views/Settings.vue";

const routes = [
  {
    path: "/",
    component: dashboard,
    meta: { layout: "_DefaultExtended" },
  },
  {
    path: "/dashboard",
    component: dashboard,
    meta: { layout: "_DefaultExtended" },
  },
  {
    path: "/add_entry",
    component: add_entry,
    meta: { layout: "_DefaultExtended" },
  },
  {
    path: "/settings",
    component: settings,
    meta: { layout: "_DefaultExtended" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  linkActiveClass: "text-c-primary",
  linkExactActiveClass: "text-c-primary",
});

export default router;
