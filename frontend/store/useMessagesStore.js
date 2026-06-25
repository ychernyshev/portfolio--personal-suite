import { defineStore } from 'pinia';
import backendApi from "@/services/backendApi.ts";

export const useMessagesStore = defineStore('messages', {
    state: () => ({
        messages: [],
        loading: false,
    }),
    actions: {
        async fetchMessagesForDate(date) {
            this.loading = true;
            try {
                const response = await backendApi.get(`calculator/sunrise-sunset-time?date=${date}`);
                this.messages = response.data;
            } catch (error) {
                console.error("Messages error:", error);
            } finally {
                this.loading = false;
            }
        },
    },
});
