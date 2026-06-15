// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup lang="ts">
import {onMounted, onUnmounted} from "vue";

import '@/assets/dashboard/css/nucleo-icons.css';
import '@/assets/dashboard/css/nucleo-svg.css';
import '@/assets/dashboard/css/nucleo-svg.css';
import SyncMail from "@/components/personal/user/dashboard/mail/SyncMail.vue";
import MainContent from "@/components/personal/user/dashboard/grid/MainContent.vue";
import DashboardHeader from "@/components/personal/user/dashboard/grid/dashboardHeader.vue";
import DashboardSidebar from "@/components/personal/user/dashboard/grid/dashboardSidebar.vue";

const SOFT_UI_DASHBOARD_CLASS = 'soft-ui-styles';
const SOFT_UI_JS_CLASS = 'soft-ui-scripts';

const currentYear: number = new Date().getFullYear();

onMounted(() => {
  document.body.classList.add('g-sidenav-show', 'bg-gray-100');

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

    if (document.getElementsByClassName(SOFT_UI_JS_CLASS).length === 0) {
      const script = document.createElement('script');
      script.src = '/public/assets/dashboard/js/soft-ui-dashboard.min.js?v=1.0.7';
      script.className = SOFT_UI_JS_CLASS;
      script.async = true;
      document.body.appendChild(script);
    }
  }
});

onUnmounted(() => {
  document.body.classList.remove('g-sidenav-show', 'bg-gray-100');

  const dynamicStyles = document.getElementsByClassName(SOFT_UI_DASHBOARD_CLASS);
  while (dynamicStyles.length > 0) {
    dynamicStyles[0].remove();
  }

  const dynamicScripts = document.getElementsByClassName(SOFT_UI_JS_CLASS);
  while (dynamicScripts.length > 0) {
    dynamicScripts[0].remove();
  }
});
</script>

<template>
  <dashboard-sidebar />
  <main class="main-content mt-1 border-radius-lg">
    <dashboard-header />
    <main-content>
      <router-view/>
    </main-content>
  </main>
</template>

<style scoped>
.main-content {
  margin-left: 0 !important;
  padding: 10px;
  transition: margin-left 0.3s ease-in-out;
}

@media (min-width: 1200px) {
  .main-content {
    margin-left: 275px !important;
    position: relative;
  }
}

.dashboard-wrapper {
  display: flex;
  flex-direction: row;
  background-color: #F8F9FA;
  width: 100%;
  min-height: 100vh;
}

@media (min-width: 1200px) {
  .dashboard-wrapper {
    flex-direction: column;
  }
}
</style>