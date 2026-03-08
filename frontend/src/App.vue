<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import MainLayout from "./components/layouts/_DefaultExtended.vue";

const route = useRoute();

const layouts = {
  MainLayout,
};

const currentLayout = computed(() => layouts[route.meta.layout] || MainLayout);
</script>

<template>
  <component :is="currentLayout">
    <router-view />
  </component>
</template>

<style scoped></style>
