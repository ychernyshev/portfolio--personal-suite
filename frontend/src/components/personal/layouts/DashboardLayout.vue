<script setup lang="ts">
import {onMounted, onUnmounted} from "vue";

  import '@/assets/dashboard/css/nucleo-icons.css';
  import '@/assets/dashboard/css/nucleo-svg.css';
  import '@/assets/dashboard/css/nucleo-svg.css';

  const SOFT_UI_DASHBOARD_CLASS = 'soft-ui-styles';

  onMounted(() => {
    const links: string[] = [
      '/public/assets/dashboard/css/soft-ui-dashboard.css?v=1.0.7',
      '/public/assets/dashboard/css/dashboard.css'
    ];

    if (document.getElementsByClassName(SOFT_UI_DASHBOARD_CLASS).length === 0) {
      links.forEach((linkValue: string) => {
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.className = SOFT_UI_DASHBOARD_CLASS;
        link.href = linkValue;

        document.head.appendChild(link);
      });
    }
  });

  onUnmounted(() => {
    const dynamicStyles = document.getElementsByClassName(SOFT_UI_DASHBOARD_CLASS);
    while (dynamicStyles.length > 0) {
      dynamicStyles[0].remove();
    }
  });
</script>

<template>
  <div class="dashboard-wrapper">
    <slot />
  </div>
</template>

<style scoped>

</style>