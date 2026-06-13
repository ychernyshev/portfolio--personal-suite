<script setup lang="ts">
  const currentYear = new Date().getFullYear();
</script>

<template>
  <footer class="footer pt-3">
    <div class="container-fluid">
      <div class="row align-items-center justify-content-lg-between">
        <div class="col-12 mb-lg-0 mb-4">
          <div class="copyright text-start text-sm text-muted text-lg-left">
            © {{ currentYear }}, the <span class="text-info">personal dev showcase</span> by
            <router-link to="/" class="fw-bold">
              Yevgenii Chernyshev
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped></style>