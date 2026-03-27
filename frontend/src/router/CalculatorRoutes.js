export default {
    path: "/calculator",
    meta: { layout: "_DefaultExtended" },
    children: [
        { path: "", component: () => import("../views/calculator/Dashboard.vue"), meta: { layout: "_DefaultExtended" } },
        { path: "dashboard", component: () => import("../views/calculator/Dashboard.vue"), meta: { layout: "_DefaultExtended" } },
        { path: "add_entry", component: () => import("../components/calculator/NewRecord.vue"), meta: { layout: "_DefaultExtended" } },
        { path: "settings", component: () => import("../views/calculator/Settings.vue"), meta: { layout: "_DefaultExtended" }},
    ]
}