import type { RouteRecordRaw } from "vue-router";
import { RouterView} from "vue-router";

const adminPageRoutes: RouteRecordRaw = {
    path: "/user",
    component: RouterView,
    // meta: { layout: "InboxLayout" },
    meta: { layout: "DashboardLayout" },
    children: [
        {
            path: "dashboard",
            component: () => import("@/views/personal/user/dasboard/mail/Inbox.vue"),
        },
        {
            path: "dashboard/mail_hub",
            component: () => import("@/views/personal/user/dasboard/mail/Inbox.vue"),
        },
    ],
}

export default adminPageRoutes;