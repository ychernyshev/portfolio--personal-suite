import backendApi from "./backendApi.js";

const api_url = backendApi.defaults.baseURL + 'data_export/';

export const exportData = async () => {
    try {
        const response = await backendApi.get('data-export/', {
            responseType: 'blob',
        });

        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;

        link.setAttribute('download','solar_generation_power_report.xlsx');

        document.body.appendChild(link);
        link.click();

        link.remove();
        window.URL.revokeObjectURL(url);
    } catch (error) {
        console.error("Помилка при завантаженні:", error);
    }
};