<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { useRoute } from "vue-router";
import CalculatorLayout from "./components/calculator/layouts/_DefaultExtended.vue";
import PersonalLayout from "./components/personal/MainLayout.vue";

const route = useRoute();

const layouts: Record<string, any> = {
  CalculatorLayout,
  PersonalLayout,
};

const currentLayout = computed(() => layouts[route.meta.layout as string]);

const isBackendReady = ref(false);
const isWakeUp = ref(false);

const wakeUpBackend = async () => {
  try {
    const response = fetch('https://personal-dev-showcase-django.onrender.com/api/ping/');

    if(response.ok) {
      const isBackendReady = false;
      const isWakeUp = false;
    }
  } catch (error) {
    console.log("Waiting for backend...");
  }
}

onMounted(() => {
  wakeUpBackend();

  setTimeout(() => {
    if (!isBackendReady.value) {
      isWakeUp.value = true;
    }
  }, 3000);
})
</script>

<template>
  <component :is="currentLayout">
    <router-view />
  </component>
</template>

<style scoped></style>\
