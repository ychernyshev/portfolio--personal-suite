<script setup lang="ts">
import { computed } from "vue";
import { useRoute } from "vue-router";
import CalculatorLayout from "./components/calculator/layouts/_DefaultExtended.vue";
import PersonalLayout from "./components/personal/layouts/MainLayout.vue";

const layouts: Record<string, any> = {
  CalculatorLayout,
  PersonalLayout,
};

const currentLayout = computed(() => layouts[route.meta.layout as string] || PersonalLayout);
</script>

<template>
  <component :is="currentLayout">
    <router-view />
  </component>
</template>

<style scoped></style>
