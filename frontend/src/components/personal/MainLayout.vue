<script setup lang="ts">
  import TopNav from "./TopNav.vue";
  import ContactForm from "./contacts/ContactForm.vue";
  import '@/assets/personal/css/personal.css';
</script>

<template>
  <div class="personal-theme">
    <div class="page-container">
      <top-nav class="neon-border"/>
      <contact-form />
      <slot />
    </div>
  </div>
</template>

<style scoped>
  .personal-theme {
    min-height: 100vh;
    background-image: url("@/assets/personal/images/dark_bg.png");
  }

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