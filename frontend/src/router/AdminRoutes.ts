import type { RouteRecordRaw } from "vue-router";
import { RouterView} from "vue-router";

const adminPageRoutes: RouteRecordRaw = {
    path: "/user",
    component: RouterView,
    meta: { layout: "InboxLayout" },
    children: [
        {
            path: "dashboard/mail_hub",
            component: () => import("@/views/personal/user/admin/mail/Inbox.vue"),
        },
    ],
}

export default adminPageRoutes;