import { defineStore } from 'pinia'
import { ref } from 'vue'
import backendApi from "../src/services/backendApi.ts";

export const useDateRangeStore = defineStore('dateRange', () => {
    const dateRange = ref({ min: null, max: null })

    const now = new Date()
    const selectedYear = ref(now.getFullYear())
    const selectedMonth = ref(now.getMonth()) // 0-11
    const monthGenerationChartData = ref(null)
    const loading = ref(false)
    const errorMsg = ref("");
    const errorClass = ref("");

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

    const getMonthGeneration = async () => {
        loading.value = true
        try {
            const response = await backendApi.get('calculator/power_generation_month_analytics/', {
                params: {
                    year: selectedYear.value,
                    month: selectedMonth.value + 1
                }
            })
            monthGenerationChartData.value = response.data
        } catch (error) {
            console.error('MNo data is being received from the server:', error)
            monthGenerationChartData.value = null
            errorMsg.value = "No data is being received from the server.";
            errorClass.value = "alert-warning";
        } finally {
            loading.value = false
        }
    }

    const setSelectedPeriod = (year, month) => {
        selectedYear.value = year
        selectedMonth.value = month
        getMonthGeneration()
    }

    return {
        dateRange,
        selectedYear,
        selectedMonth,
        monthGenerationChartData,
        loading,
        errorMsg,
        errorClass,
        fetchDateRange,
        getMonthGeneration,
        setSelectedPeriod
    }
})