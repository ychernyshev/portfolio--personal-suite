<script setup>
import ButtonComp from "@/components/personal/ButtonComp.vue";
import {computed, ref} from "vue";
import {useCalculatorStore} from "../../../../store/useCalculatorStore.js";
import {storeToRefs} from "pinia";

const CalculatorStore = useCalculatorStore();
const {entries} = storeToRefs(CalculatorStore);

const now = new Date()
const currentYear = now.getFullYear()
const currentMonth = now.getMonth()

const activeYear = ref(currentYear)
const activeMonth = ref(currentMonth)

const minDataDate = computed(() => {
  if (!entries.value || entries.value.length === 0) {
    const now = new Date()
    return { year: now.getFullYear(), month: now.getMonth() }
  }

  const earliestEntry = entries.value.reduce((min, entry) => {
    return new Date(entry.date) < new Date(min.date) ? entry : min
  }, entries.value[0])

  const dateObj = new Date(earliestEntry.date)
  return {
    year: dateObj.getFullYear(),
    month: dateObj.getMonth()
  }
})

const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

const currentMonthName = computed(() => monthNames[activeMonth.value])

const canGoPrev = computed(() => {
  const totalMonthsActive = activeYear.value * 12 + activeMonth.value
  const totalMonthsMin = minDataDate.value.year * 12 + minDataDate.value.month
  return totalMonthsActive > totalMonthsMin
})

const canGoNext = computed(() => {
  const totalMonthsActive = activeYear.value * 12 + activeMonth.value
  const totalMonthsCurrent = currentYear * 12 + currentMonth
  return totalMonthsActive < totalMonthsCurrent
})

const prevMonth = () => {
  if (!canGoPrev.value) return
  if (activeMonth.value === 0) {
    activeMonth.value = 11
    activeYear.value--
  } else {
    activeMonth.value--
  }
}

const nextMonth = () => {
  if (!canGoNext.value) return
  if (activeMonth.value === 11) {
    activeMonth.value = 0
    activeYear.value++
  } else {
    activeMonth.value++
  }
}
</script>

<template>
  <button-comp type="button"
               title="<<"
               class="neomorphic text-purple p-1 pl-3 pr-3"
               @click="prevMonth"
               :disabled="!canGoPrev"
               :class="{ 'opacity-40 cursor-not-allowed': !canGoPrev }" />
  <span class="ml-3 mr-3">{{ currentMonthName }}</span>
  <button-comp type="button"
               title=">>"
               class="neomorphic text-purple p-1 pl-3 pr-3"
               @click="nextMonth"
               :disabled="!canGoNext"
               :class="{ 'opacity-40 cursor-not-allowed': !canGoNext }" />
</template>

<style scoped>

</style>