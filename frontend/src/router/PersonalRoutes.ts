import type { RouteRecordRaw } from 'vue-router';
import {RouterView} from "vue-router";

const personalRoutes: RouteRecordRaw = {
    path: "/layout",
    component: RouterView,
    meta: { layout: "PersonalLayout" },
    children: [
        {
            path: "/",
            component: () => import("../views/personal/Home.vue"),
            meta: { layout: "PersonalLayout" }
        },
        {
            path: "/introducing",
            component: () => import("../views/personal/Home.vue"),
            meta: { layout: "PersonalLayout" }
        },
        {
            path: "/intro",
            component: () => import("../views/personal/Home.vue"),
            meta: { layout: "PersonalLayout" }
        },
        {
            path: "/blogs",
            component: () => import("../views/personal/Blogs.vue"),
            meta: { layout: "PersonalLayout" }
        },
        {
            path: "/code",
            component: () => import("../views/personal/CodeAndVision.vue"),
            meta: { layout: "PersonalLayout" }
        },
        {
            path: "/contacts",
            component: () => import("../views/personal/Contacts.vue"),
            meta: { layout: "PersonalLayout" }
        },
    ]
};

export default personalRoutes;