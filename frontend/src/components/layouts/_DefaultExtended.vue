<script setup>
import TopNav from "../navs/_TopNav.vue";
</script>

<template>
  <div class="layout-wrapper bg-c-dark-gray min-vh-100 w-100">
    <header>
      <top-nav />
    </header>

    <main class="position-relative">
      <slot />
    </main>

    <footer>
      <p class="text-muted mb-0 small text-center p-5">
        &copy; 2026 Solar Power Calculator. Based on Django + Vue 3.
      </p>
    </footer>
  </div>
</template>

<style></style>
