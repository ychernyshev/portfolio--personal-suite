<script setup>
import TopNav from "../navs/_TopNav.vue";
</script>

<template>
  <div class="dashboard-grid">
    <top-nav />
    <slot />
  </div>
</template>

<style scoped>
.dashboard-grid {
  min-width: 100%;
  padding: 30px 10px 0 10px;
  display: grid;
  grid-template-areas:
    "header"
    "widgets"
    "content"
    "sidebar";
  ;
}
</style>
