<script setup>
import TopNav from "../navs/_TopNav.vue";
</script>

<template>
  <header>
    <top-nav />
  </header>

  <main class="position-relative">
    <slot />
  </main>

  <footer>
    <p class="text-muted mb-0 small">
      &copy; 2026 Solar Power Calculator. Based on Django + Vue 3.
    </p>
  </footer>
</template>

<style></style>
