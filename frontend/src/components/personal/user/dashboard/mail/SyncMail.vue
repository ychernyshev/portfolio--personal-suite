// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup lang="ts">
  import backendApi from "@/services/backendApi.ts";
  import {onMounted, onUnmounted} from "vue";

  let mailSyncInterval: number | null | undefined = null

  const fetchMail = async () => {
    try {
      await backendApi.post("personal/user/dashboard/mail/inbound/sync/")
      console.log("Mail successfully synced")
    } catch (error) {
      console.error("Mail sync error:", error)
    }
  }

  onMounted(async () => {
    await fetchMail()

    mailSyncInterval = setInterval(fetchMail, 30000)
  })

  onUnmounted(() => {
    if (mailSyncInterval) {
      clearInterval(mailSyncInterval)
    }
  })
</script>

<template>

</template>

<style scoped>

</style>