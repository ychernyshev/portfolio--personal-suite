<script setup lang="ts">
  import axios from "axios";
  import { ref, onMounted } from "vue";

  const repoData = ref<any>(null);

  onMounted(async () => {
    try {
      const response = await axios.get(
          "https://raw.githubusercontent.com/ychernyshev/portfolio--personal-suite"
      );
      repoData.value = response.data;
    } catch (error) {
      console.error("Error during downloading data:", error);
    }
  });

  console.log(repoData)

</script>

<template>
<!--  <div v-if="repoData">-->
<!--    {{ repoData.name }}-->
<!--  </div>-->
  <img src="https://img.shields.io/github/commit-activity/m/ychernyshev/portfolio--personal-suite" alt="Stars"/>
  <img src="https://img.shields.io/github/repo-size/ychernyshev/portfolio--personal-suite" alt="Stars"/>
</template>

<style scoped>

</style>