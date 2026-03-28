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
  <div class="row h-100 align-items-center justify-content-center">
    <div class="d-inline-flex flex-column align-items-start">
      <span class="text-purple" style="font-size: 2.3rem; font-weight: 300">
        {{ title }}
      </span>
      <div class="d-flex flex-row align-items-end" style="margin-top: -.5rem">
        <span :class="colorClass" style="font-size: 6rem; font-weight: 200; line-height: 1;">
          {{ formatted.int }}
        </span>
        <div class="d-flex flex-column align-items-start ms-2" style="line-height: 1.1;">
          <span class="text-purple" style="font-size: 1.8rem; line-height: 1; font-weight: 300">{{ label }}</span>
          <span class="text-secondary" style="font-size: 1.8rem; font-weight: 300;">.{{ formatted.dec }}</span>
          <span class="text-sky-blue-4" style="font-size: 1.2rem; font-weight: 400;">{{ unit }}</span>
        </div>
      </div>
    </div>
  </div>
</template>