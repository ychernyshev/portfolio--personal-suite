import { defineStore } from 'pinia';
import backendApi from '../src/services/calculator/backendApi';

export const useCalculatorStore = defineStore('calculator', {
    state: () => ({
        entries: [],
        stats: { total_power: 0, total_cost: 0 },

        currentPage: 1,
        totalPages: 1,
        totalCount: 0,
        loading: false,

        currentView: 'table'
    }),

    actions: {
        async fetchStats() {
            try {
                const response = await backendApi.get("stats/");
                this.stats = response.data;
            } catch (error) {
                console.error("Stats error:", error);
            }
        },

        async fetchEntries(page = 1) {
            this.loading = true;
            try {
                const response = await backendApi.get(`entries/?page=${page}`);
                this.entries = response.data.results;
                this.totalCount = response.data.count;
                this.totalPages = Math.ceil(response.data.count / 10);
                this.currentPage = page;
            } catch (error) {
                console.error("Entries error:", error);
            } finally {
                this.loading = false;
            }
        },

        async setPage(page) {
            if (page >= 1 && page <= this.totalPages) {
                await this.fetchEntries(page);
            }
        },

        setView(view) {
            this.currentView = view;
        }
    }
});