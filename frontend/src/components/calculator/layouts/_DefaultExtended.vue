<script setup>
import TopNav from "../navs/_TopNav.vue";
import '@/assets/calculator/js/bootswatch.min.css';
import '@/assets/calculator/css/calculator.css';
import '@/assets/calculator/css/style.css';
import '@/assets/calculator/css/mobile.css';
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

@media (min-width: 1200px) {
  .dashboard-grid {
    grid-template-columns: 3fr 1fr;
    grid-template-rows: auto 1fr;
    grid-template-areas:
      "header header"
      "content sidebar"
    ;
    gap: 30px;
    padding: 20px;
  }
}

@media (min-width: 1400px) {
}
</style>
