<script setup lang="ts">
import {onMounted, onUnmounted} from "vue";

  import '@/assets/dashboard/css/nucleo-icons.css';
  import '@/assets/dashboard/css/nucleo-svg.css';
  import '@/assets/dashboard/css/nucleo-svg.css';
  import SyncMail from "@/components/personal/user/dashboard/mail/SyncMail.vue";
  import MainContent from "@/components/personal/user/dashboard/grid/MainContent.vue";
  import DashboardHeader from "@/components/personal/user/dashboard/grid/dashboardHeader.vue";

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
  <div class="dashboard-wrapper g-sidenav-show bg-gray-100">
    <div class="container-fluid">
      <dashboard-header />
      <main-content>
        <router-view/>
      </main-content>
    </div>
<!--    <asside />-->

  </div>
</template>

<style scoped>
  .dashboard-wrapper {
    //display: grid;
    background-color: #F8F9FA;
    width: 100%;
    min-height: 100vh;
  }

  @media (min-width: 1200px) {
    .dashboard-wrapper {
      //grid-template-rows: 1fr 1fr;
    }
  }
</style>