import { defineStore } from 'pinia'
import { ref } from 'vue'
import backendApi from "../src/services/backendApi.ts";

export const useDateRangeStore = defineStore('dateRange', () => {
    const dateRange = ref({ min: null, max: null })

    const fetchDateRange = async () => {
        try {
            const response = await backendApi.get('calculator/date_range/')
            dateRange.value = {
                min: response.data.min_date,
                max: response.data.max_date
            }
        } catch (error) {
            console.error('Error loading date range:', error)
        }
    }

    return {
        dateRange,
        fetchDateRange
    }
})