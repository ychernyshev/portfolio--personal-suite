<script setup lang="ts">
import {useMailStore} from "@/services/personal/useMailStore.ts";

const mailStore = useMailStore();
</script>

<template>
  <span v-if="mailStore.unreadCount > 0">
    {{ mailStore.unreadCount }}
  </span>
</template>

<style scoped>

</style>