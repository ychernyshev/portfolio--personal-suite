<script setup lang="ts">
  import TopNav from "./TopNav.vue";
  import ContactForm from "./ContactForm.vue";
</script>

<template>
  <div class="page-container">
    <top-nav />
    <contact-form />
    <slot />
  </div>
</template>

<style>
  .page-container {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-areas:
      "header"
      "content"
  ;
    padding: 30px 20px 0 20px;
    min-width: 100%;
  }
</style>