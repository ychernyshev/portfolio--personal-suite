<script setup lang="ts">
import {onMounted, onUnmounted} from "vue";

  import '@/assets/dashboard/css/styles.css';
  import '@/assets/dashboard/css/nucleo-icons.css';
  import '@/assets/dashboard/css/nucleo-svg.css';
  import '@/assets/dashboard/css/nucleo-svg.css';

  const SOFT_UI_DASHBOARD = 'soft-ui-dashboard';

  onMounted(() => {
    if (!document.getElementById(SOFT_UI_DASHBOARD)) {
      const link = document.createElement('link');
      link.id = SOFT_UI_DASHBOARD;
      link.rel = 'stylesheet';
      link.href = '/assets/dashboard/css/soft-ui-dashboard.css?v=1.0.7';
      document.head.appendChild(link);
    }
  });

  onUnmounted(() => {
    const link = document.getElementById(SOFT_UI_DASHBOARD);
    if (link) {
      link.remove();
    }
  });
</script>

<template>

</template>

<style scoped>

</style>