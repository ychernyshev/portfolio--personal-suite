<script setup>
import { computed } from "vue";

const props = defineProps({
  title: String,
  label: String,
  value: Number,
  unit: String,
  colorClass: { type: String, default: 'text-success' }
});

const formatted = computed(() => {
  const rawValue = props.label === "power"
      ? (props.value / 1000)
      : props.value;

  const [int, dec] = Number(rawValue || 0).toFixed(2).split('.');

  return { int, dec };
});
</script>

<template>
  <div class="row h-100 align-items-start justify-content-center">
    <div class="d-inline-flex flex-column align-items-start widget-item">
      <p data-v-80000e9e="" class="text-purple widget-title">
        {{ title }}
      </p>
      <div class="d-flex flex-row align-items-end widget-numbers-container">
        <span :class="colorClass" class="widget-huge-number">
          {{ formatted.int }}
        </span>
        <div class="d-flex flex-column align-items-start ms-2 details-column">
          <p class="text-purple widget-label-text">{{ label }}</p>
          <span class="text-secondary widget-decimal-part">.{{ formatted.dec }}</span>
          <span class="text-sky-blue-4 widget-unit-text">{{ unit }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.widget-item {
  width: 100%;
  padding: 10px;
  height: 6.7rem;
  margin-top: -1rem;
}

.widget-title {
  font-size: clamp(1.2rem, 2.8vw, 1.5rem);
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.widget-numbers-container {
  display: flex;
  flex-direction: row;
  align-items: baseline;
  gap: 0;
}

.widget-huge-number {
  font-size: clamp(3rem, 10vw, 5.5rem);
  font-weight: 200;
  line-height: 0.5;
}

.details-column {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  line-height: 1;
}

.widget-label-text {
  font-size: clamp(1.2rem, 2.8vw, 1.5rem);
  margin: 0;
  text-transform: lowercase;
  font-weight: 500;
  line-height: .2rem;
}

.widget-decimal-part {
  font-size: 1.8rem;
  font-weight: 300;
  line-height: 3.1rem;
}

.widget-unit-text {
  font-size: clamp(1.1rem, 3vh, 1.4rem);
  font-weight: 400;
  line-height: 0.1rem;
}

@media (min-width: 768px) {
  .widget-item {
    height: 7.1rem;
  }
}
</style>