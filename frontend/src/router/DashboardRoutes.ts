import type { RouteRecordRaw } from "vue-router";
import { RouterView } from "vue-router";

const adminPageRoutes: RouteRecordRaw = {
    path: "/layout",
    component: RouterView,
    meta: { layout: "DashboardLayout" },
    children: [
        {
            path: "/user/dashboard",
            component: () => import("@/components/personal/user/dashboard/Dashboard.vue"),
        },
        {
            path: "/user/dashboard/mail_hub",
            component: () => import("@/components/personal/user/dashboard/mail/Inbox.vue"),
        },
    ],
}

export default adminPageRoutes;