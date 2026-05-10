import {createRouter, createWebHistory} from "vue-router";
import personalRoutes from "./PersonalRoutes";
import calculatorRoutes from "./CalculatorRoutes";

const routes = [
    personalRoutes,
    calculatorRoutes,
];

const router = createRouter({
    history: createWebHistory(),
    routes,
    linkActiveClass: "text-c-primary",
    linkExactActiveClass: "text-c-primary",
});

router.beforeEach((to, from, next) => {
    const isAuthenticated = localStorage.getItem('access_token');
    if (to.path.startsWith('/user') && !isAuthenticated) {
        next({
            path: '/login',
            query: {next: to.fullPath}
        });
    } else {
        next();
    }
});

export default router;
