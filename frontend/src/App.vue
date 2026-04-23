<script setup lang="ts">
import { computed } from "vue";
import { useRoute } from "vue-router";
import PersonalLayout from "./components/personal/MainLayout.vue";

const route = useRoute();

const layouts: Record<string, any> = {
  PersonalLayout,
};

const currentLayout = computed(() => layouts[route.meta.layout as string]);
</script>

<template>
  <component :is="currentLayout">
    <router-view />
  </component>
</template>

<style scoped></style>