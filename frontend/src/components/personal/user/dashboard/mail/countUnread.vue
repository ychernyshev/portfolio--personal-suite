// SPDX-License-Identifier: AGPL-3.0-or-later
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