<script setup lang="ts">
  const props = defineProps<{
    title: string
  }>()
</script>

<template>
  <button class="btn border-0 btn-transform">
    <slot name="left"></slot>
    <span>{{ title }}</span>
    <slot name="right"></slot>
    <slot></slot>
  </button>
</template>

<style scoped>
  .shift-icon {}
  .shift-icon:hover {
     margin-right: .4rem;
     transition: .5s;
  }
</style>