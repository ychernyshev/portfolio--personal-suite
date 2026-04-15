import type { RouteRecordRaw } from 'vue-router';
import {RouterView} from "vue-router";

const personalRoutes: RouteRecordRaw = {
    path: "/layout",
    component: RouterView,
    children: [
        {
            path: "/",
            component: () => import("../views/personal/Home.vue"),
            meta: { layout: "MainLayout" }
        },
        {
            path: "/introducing",
            component: () => import("../views/personal/Home.vue"),
            meta: { layout: "MainLayout" }
        },
        {
            path: "/intro",
            component: () => import("../views/personal/Home.vue"),
            meta: { layout: "MainLayout" }
        },
        {
            path: "/blogs",
            component: () => import("../views/personal/Blogs.vue"),
            meta: { layout: "MainLayout" }
        },
        {
            path: "/code",
            component: () => import("../views/personal/CodeAndVision.vue"),
            meta: { layout: "MainLayout" }
        },
        {
            path: "/contacts",
            component: () => import("../views/personal/Contacts.vue"),
            meta: { layout: "MainLayout" }
        },
    ]
};

export default personalRoutes;