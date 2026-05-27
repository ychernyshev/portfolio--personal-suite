<script setup lang="ts">

</script>

<template>
  <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
    <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
      <svg class="bi me-2" width="40" height="32" aria-hidden="true"><use xlink:href="#bootstrap"></use></svg>
      <span class="fs-4">Showcase Dashboard</span>
    </a>
    <ul class="nav nav-pills">
      <li class="nav-item">
        <router-link to="/user/dashboard/mail_hub" class="nav-link active" aria-current="page">Mail Hub</router-link>
      </li>
    </ul>
  </header>
</template>

<style scoped>

</style>