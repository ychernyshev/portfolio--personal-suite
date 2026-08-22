// SPDX-License-Identifier: AGPL-3.0-or-later
import axios from "axios";

const api = axios.create({
    baseURL: import.meta.env.VITE_BACKEND_URL,
    withCredentials: true,
});

let isRefreshing = false;
let failedQueue: any[] = [];

const processQueue = (error: any, token = null) => {
    failedQueue.forEach(prom => {
        if (error) {
            prom.reject(error);
        } else {
            prom.resolve(token);
        }
    });
    failedQueue = [];
};

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        if (originalRequest.url && originalRequest.url.includes('auth/jwt/refresh/')) {
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            window.location.href = `/login?next=${window.location.pathname}`;
            return Promise.reject(error);
        }

        if (error.response?.status === 401 && !originalRequest._retry) {
            if (isRefreshing) {
                return new Promise((resolve, reject) => {
                    failedQueue.push({ resolve, reject });
                }).then(token => {
                    originalRequest.headers.Authorization = `Bearer ${token}`;
                    return api(originalRequest);
                }).catch(err => {
                    return Promise.reject(err);
                });
            }

            originalRequest._retry = true;
            isRefreshing = true;

            try {
                const refreshToken = localStorage.getItem('refresh_token');
                const response = await axios.post(`${import.meta.env.VITE_BACKEND_URL}auth/jwt/refresh/`, {
                    refresh: refreshToken
                });

                const { access } = response.data;
                localStorage.setItem('access_token', access);

                api.defaults.headers.common['Authorization'] = `Bearer ${access}`;
                processQueue(null, access);

                isRefreshing = false;

                originalRequest.headers.Authorization = `Bearer ${access}`;
                return api(originalRequest);
            } catch (refreshError) {
                processQueue(refreshError, null);
                isRefreshing = false;

                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                window.location.href = `/login?next=${window.location.pathname}`;
                return Promise.reject(refreshError);
            }
        }
        return Promise.reject(error);
    }
);

export default api;


// SPDX-License-Identifier: AGPL-3.0-or-later
// import axios from "axios";
//
// const api = axios.create({
//     baseURL: import.meta.env.VITE_BACKEND_URL,
//     withCredentials: true,
// });
//
// api.interceptors.request.use(
//     (config) => {
//         const token = localStorage.getItem('access_token');
//         if (token) {
//             config.headers.Authorization = `Bearer ${token}`;
//         }
//         return config;
//     },
//     (error) => Promise.reject(error)
// );
//
// api.interceptors.response.use(
//     (response) => response,
//     async (error) => {
//         console.log("INTERCEPTOR ERROR:", error);
//         const originalRequest = error.config;
//
//         if (error.response?.status === 401 && !originalRequest._retry) {
//             console.log("401 detected, attempting refresh...");
//             originalRequest._retry = true;
//
//             try {
//                 const refreshToken = localStorage.getItem('refresh_token');
//
//                 const response = await axios.post(`${import.meta.env.VITE_BACKEND_URL}auth/jwt/refresh/`, {
//                     refresh: refreshToken
//                 });
//
//                 const {access, refresh} = response.data;
//                 localStorage.setItem('access_token', access);
//
//                 if (refresh) {
//                     localStorage.setItem('refresh_token', refresh);
//                 }
//
//                 originalRequest.headers.Authorization = `Bearer ${access}`;
//                 return api({
//                     ...originalRequest,
//                     headers: {
//                         ...originalRequest.headers,
//                         Authorization: `Bearer ${access}`
//                     }
//                 });
//             } catch (refreshError) {
//                 console.error("REFRESH FAILED:", refreshError);
//                 localStorage.removeItem('access_token');
//                 localStorage.removeItem('refresh_token');
//                 window.location.href = `/login?next=${window.location.pathname}`;
//             }
//         }
//         return Promise.reject(error);
//     }
// );
//
// export default api;