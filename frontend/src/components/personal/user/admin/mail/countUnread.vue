<script setup lang="ts">
import {useMailStore} from "@/services/personal/useMailStore.ts";

const mailStore = useMailStore();
</script>

<template>
  <span v-if="mailStore.unreadCount > 0" class="badge bg-gradient-primary ms-2">
    {{ mailStore.unreadCount }}
  </span>
</template>

<style scoped>

</style>