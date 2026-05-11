<script setup lang="ts">

</script>

<template>
  <div class="admin-layout-wrapper bg-dark min-vh-100">
    <nav class="navbar navbar-dark bg-black border-bottom border-secondary mb-3">
      <div class="container-fluid">
        <span class="navbar-brand text-warning font-monospace">SENTINEL_HUB</span>
      </div>
    </nav>

    <main class="container-fluid">
      <slot />
    </main>
  </div>
</template>

<style scoped>
.admin-layout-wrapper {
  background-color: #0f172a;
}
</style>