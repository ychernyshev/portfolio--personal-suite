import axios from "axios";

const api = axios.create({
    baseURL: import.meta.env.VITE_BACKEND_URL,
    withCredentials: true,
    xsrfCookieName: import.meta.env.XSRF_COOKIE_NAME,
    xsrfHeaderName: import.meta.env.XSRF_HEADER_NAME,
});

export default api;