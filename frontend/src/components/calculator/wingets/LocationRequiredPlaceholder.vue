<script setup lang="ts">

</script>

<template>
  <div
      class="d-flex flex-row align-items-start align-items-lg-center justify-content-center p-4 p-xl-1 h-100 min-placeholder-height">
    <div class="d-block d-lg-none geo-icon-wrapper mr-2">
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor"
           class="bi bi-geo-alt-fill text-muted" viewBox="0 0 16 16">
        <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10m0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6"/>
      </svg>
    </div>
    <div>
      <div class="d-flex flex-row">
        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor"
           class="d-none d-lg-block bi bi-geo-alt-fill text-muted geo-icon my-auto" viewBox="0 0 16 16">
        <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10m0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6"/>
      </svg>
      <h5 class="fw-medium text-purple text-start my-auto">Geolocation Required</h5>
      </div>
      <p class="text-muted small mb-0 max-w-text text-justify">
        To display the weather forecast, generation charts, and monthly analytical statistics, please enable location
        access in your browser settings.
      </p>
    </div>
  </div>
</template>

<style scoped>
.min-placeholder-height {
  min-height: 130px;
}

.geo-icon-wrapper {
  padding: 15px;
  border-radius: 50%;
  box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.05), inset -2px -2px 5px rgba(255, 255, 255, 0.7);
}

.max-w-text {
  max-width: 100%;
  line-height: 1.4;
}

@media (min-width: 768px) {
  .geo-icon {
    width: 16px;
    height: 16px;
  }
}
</style>