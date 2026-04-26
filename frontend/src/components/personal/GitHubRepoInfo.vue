<script setup lang="ts">
  import axios from "axios";
  import { ref, onMounted } from "vue";
  import {S} from "vue-router/dist/router-CWoNjPRp";

  const repoData = ref<any>(null);
  const props = defineProps<{
    repoName: { repoName: string }
  }>();

  console.log('repoData: ' + repoData)

  onMounted(async () => {
    try {
      const response = await axios.get(
          `https://raw.githubusercontent.com/ychernyshev/${props.repoName}`
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
  <img :src="`https://img.shields.io/github/commit-activity/m/ychernyshev/${props.repoName}`" class="rounded-2" alt="Stars"/>
  <img :src="`https://img.shields.io/github/repo-size/ychernyshev/${props.repoName}`" class="rounded-2" alt="Stars"/>
</template>

<style scoped>

</style>