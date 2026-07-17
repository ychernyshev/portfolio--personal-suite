// store/useUserProfileSettingsStore.js
import { defineStore } from 'pinia';
import { ref } from 'vue';
import backendApi from "@/services/backendApi.ts";

export const useUserProfileSettingsStore = defineStore('userProfileSettings', () => {
    const settings = ref(null);
    const loading = ref(false);

    const updateSettings = async (newData) => {
        try {
            loading.value = true;
            const response = await backendApi.patch('/calculator/user_settings/', newData);

            settings.value = { ...settings.value, ...response.data };
            return true;
        } catch (err) {
            console.error("Error updating settings:", err);
            return false;
        } finally {
            loading.value = false;
        }
    };

    const fetchSettings = async () => {
        if (settings.value) return;
        loading.value = true;
        try {
            const response = await backendApi.get('/calculator/user_settings/');
            settings.value = response.data;
        } finally {
            loading.value = false;
        }
    };

    return { settings, loading, fetchSettings };
});