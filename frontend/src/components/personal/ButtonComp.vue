<script setup lang="ts">
  const props = defineProps<{
    title: string
  }>()
</script>

<template>
  <button class="btn border-0 rounded-2 text-primary-emphasis btn-transform">
    <slot name="left"></slot>
    <span>{{ title }}</span>
    <slot name="right"></slot>
    <slot></slot>
  </button>
</template>

<style scoped>

</style>