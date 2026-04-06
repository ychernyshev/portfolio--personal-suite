<script setup>
import { ref, computed } from 'vue';
import { DatePicker } from 'v-calendar';
import 'v-calendar/style.css';

const props = defineProps({
  recordedDates: {
    type: Array,
    default: () => [new Date(2026, 2, 10), new Date(2026, 2, 15)] // Приклад
  }
});

const emit = defineEmits(['date-selected']);

const selectedDate = ref(new Date());

// Налаштування точок та виділення сьогоднішнього дня
const attributes = computed(() => [
  // Виділення сьогодні
  {
    key: 'today',
    highlight: {
      color: 'purple',
      fillMode: 'light',
    },
    dates: new Date(),
  },
  // Зелені точки для днів з даними
  {
    dot: 'green',
    dates: props.recordedDates,
  },
]);

const handleDayClick = (day) => {
  // Передаємо подію вгору до батьківського компонента
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
    />
  </div>
</template>

<style scoped>
/* Кастомізація під твій фіолетовий колір */
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
  //background-color: white;
  padding: .5rem;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(10px) saturate(180%);
  -webkit-backdrop-filter: blur(10px) saturate(180%);
  box-shadow: .2rem .3rem 1rem #e0e5ec;
}

/* Прибираємо стандартні обводки кнопок при фокусі */
:deep(.vc-day-content:focus) {
  background-color: rgba(111, 66, 193, 0.1) !important;
  box-shadow: none !important;
}

:deep(.vc-header) {
  margin-bottom: 10px;
  padding: 0;
}

:deep(.vc-title) {
  background: transparent;
  color: gray;
  font-weight: 600;
  text-transform: capitalize;
}

.calendar-card {
  position: relative;
  overflow: visible;
  height: 100%;
}
</style>