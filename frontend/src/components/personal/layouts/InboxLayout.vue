<script setup lang="ts">
  import InboxSidebar from "@/components/personal/user/admin/mail/InboxSidebar.vue";
  import SyncMail from "@/components/personal/user/admin/mail/SyncMail.vue";
  import Toast from "@/components/personal/user/admin/Toast.vue";
</script>

<template>
  <div class="admin-layout-wrapper min-vh-100 m-0 p-0 ps-3 pt-3">
    <sync-mail />
    <inbox-sidebar />
    <main class="container-fluid inbox-container m-0 p-0">
      <slot />
    </main>
    <toast />
  </div>
</template>

<style scoped>
.admin-layout-wrapper {
  font-family: "Inter", sans-serif;
  background: var(--p-light-2);
}

.inbox-container {
  background-color: var(--p-darker-4);
  border-top-left-radius: 1.2rem;
}
</style>