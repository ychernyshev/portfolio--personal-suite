// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
import { ref, computed } from 'vue';
import { DatePicker } from 'v-calendar';
import 'v-calendar/style.css';

const props = defineProps({
  recordedDates: {
    type: Array,
    default: () => [new Date(2026, 2, 10), new Date(2026, 2, 15)]
  }
});

const emit = defineEmits(['date-selected']);

const selectedDate = ref(new Date());

const attributes = computed(() => [
  {
    key: 'today',
    highlight: {
      color: 'purple',
      fillMode: 'light',
    },
    dates: new Date(),
  },
  {
    dot: 'green',
    dates: props.recordedDates,
  },
]);

const handleDayClick = (day) => {
  emit('date-selected', day);
};
</script>

<template>
  <div class="w-100">
    <DatePicker
        v-model="selectedDate"
        @dayclick="handleDayClick"
        :attributes="attributes"
        expanded
        transparent
        borderless
        trim-weeks
        locale="uk"
        title-position="left"
    >
    <template #header="{
        monthLabel,
        yearLabel,
        pages,
        attributes,
        movePrev,
        moveNext,
        hasPrevPage,
        hasNextPage
      }">
      <div class="d-flex justify-content-between align-items-center px-1 mb-2">
        <!-- Назва місяця/року (або залишаємо стандартний стиль заголовка) -->
        <div class="vc-title" style="color: var(--purple); font-weight: 500; text-transform: capitalize;">
          {{ monthLabel }} {{ yearLabel }}
        </div>

        <!-- Кнопки навігації зі стрілками, до яких застосовано ВАШ існуючий клас -->
        <div class="d-flex gap-1">
          <button
              type="button"
              class="your-existing-class-here"
              :disabled="!hasPrevPage"
              @click="movePrev"
          >
            &lt;
          </button>
          <button
              type="button"
              class="your-existing-class-here"
              :disabled="!hasNextPage"
              @click="moveNext"
          >
            &gt;
          </button>
        </div>
      </div>
    </template>
    </DatePicker>
  </div>
</template>

<style scoped>
:deep(.vc-purple) {
  --vc-accent-500: #6f42c1;
  --vc-accent-600: #59359a;
}

:deep(.vc-container) {
  --vc-font-family: inherit;
  background: transparent;
  color: gray;
}

:deep(.vc-pane-container) {
  padding: .5rem;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(10px) saturate(180%);
  -webkit-backdrop-filter: blur(10px) saturate(180%);
  box-shadow: .2rem .3rem 1rem #e0e5ec;
}

:deep(.vc-day-content:focus) {
  box-shadow: none !important;
}

:deep(.vc-header) {
  margin-bottom: 10px;
  padding: 0 40px 0 20px;
}

:deep(.vc-title) {
  background: transparent;
  color: var(--purple);
  font-weight: 500;
  text-transform: capitalize;
}

.calendar-card {
  position: relative;
  overflow: visible;
  height: 100%;
}
:deep(.vc-arrow) {
  flex-shrink: 0;
  background: linear-gradient(#f4f7fe, #eaf0fe);
  border-radius: 8px;
  border: none;
  color: var(--purple);
  display: flex;
  align-items: center;
  width: 32px;
  height: 32px;
  box-shadow:
      4px 5px 22px var(--lighter-blue-3),
      -4px -5px 22px var(--shadow-light);
  transition: all 0.2s ease;
}

:deep(.vc-arrow:hover) {
  background: rgba(111, 66, 193, 0.05);
  box-shadow: inset .1rem .1rem .3rem #e0e5ec, inset -.1rem -.1rem .3rem #fff;
}

:deep(.vc-arrow:disabled) {
  opacity: 0.4;
  cursor: not-allowed;
  box-shadow: none;
}

:deep(.vc-day-content.is-selected),
:deep(.vc-highlight) {
  background: linear-gradient(#f4f7fe, #eaf0fe);
  color: var(--purple);
  border-radius: 20px;
  padding: 20px;
  border: 1px solid var(--dark-gray-rgba);
}

:deep(.vc-highlight-content-solid) {
  --vc-highlight-solid-content-color: var(--purple) !important;
}

:deep(.vc-day-content:hover) {
  background-color: transparent !important;
  color: inherit !important;
  box-shadow: none !important;
}

:deep(.vc-day-content.active) {
  background-color: var(--purple);
  color: black;
}
</style>