<script setup lang="ts">
import { computed } from "vue";
import { useRoute } from "vue-router";
import MainLayout from "./components/personal/MainLayout.vue";

const route = useRoute();

const layouts: Record<string, any> = { MainLayout };

const currentLayout = computed(
    () => layouts[route.meta.layout as string] || MainLayout
);
</script>

<template>
  <component :is="currentLayout">
    <router-view />
  </component>
</template>