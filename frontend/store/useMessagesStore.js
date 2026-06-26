import { defineStore } from 'pinia';
import backendApi from "@/services/calculator/backendApi";

export const useMessagesStore = defineStore('messages', {
    state: () => ({
        messages: null,
        loading: false,
        userTimeZone: 'Europe/Kyiv',
    }),

    getters: {
        currentForecast: (state) => {
            return state.messages?.results?.[0] || null;
        },

        formatTime: (state) => {
            return (isoString) => {
                if (!isoString) return '';
                const date = new Date(isoString);
                return date.toLocaleTimeString([], {
                    hour: '2-digit',
                    minute: '2-digit',
                    timeZone: state.userTimeZone
                });
            };
        }
    },

    actions: {
        getCurrentDateTimeISO() {
            const now = new Date();
            return `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}T${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`;
        },

        async fetchMessagesForDate(date = null) {
            this.loading = true;
            const queryDate = date || this.getCurrentDateTimeISO();

            try {
                const response = await backendApi.get(`calculator/sunrise-sunset-time?date=${queryDate}`);
                this.messages = response.data;
            } catch (error) {
                console.error("Messages error:", error);
                this.messages = null;
            } finally {
                this.loading = false;
            }
        },
    },
});