<script setup lang="ts">
import MailReply from "@/components/personal/user/admin/mail/MailReply.vue";
import MailAnswer from "@/components/personal/user/admin/mail/MailAnswer.vue";

interface Message {
  id: number;
  subject_name: string;
  subject_email: string;
  project_theme: string;
  mail_body: string;
  created_at: string;
  is_read: boolean;
}

const props = defineProps<{
  message: Message | null;
}>();
</script>

<template>
  <div v-if="props.message" class="d-flex flex-column mail-body-container mt-3 ms-3 pt-3 ps-3 pe-3 h-75">
    <div class="pb-3 mb-3">
      <h2 class="text-warning">{{ props.message.project_theme }}</h2>
      <div class="d-flex justify-content-between">
        <span class="text-info">From: {{ props.message.subject_email }}</span>
        <span class="text-info-emphasis bg-body-tertiary ps-2 pe-2 rounded-2">{{ new Date(props.message.created_at).toLocaleString() }}</span>
      </div>
    </div>
    <div class="flex-grow-1 p-3 rounded border-0 mail-body">
      <div class="d-flex flex-row justify-content-between">
        <mail-reply
            :subject_email="props.message.subject_email"
            :project_theme="props.message.project_theme"
            :mail_body="props.message.subject_email"
        />
        <mail-answer />
      </div>
      {{ props.message.mail_body }}
    </div>
  </div>

  <div v-else class="h-100 d-flex align-items-center justify-content-center border-0 rounded text-muted">
    Select a message to view details
  </div>
</template>

<style scoped>
.mail-body-container {
  background: var(--p-light-2);
  border-top-left-radius: 1.2rem;
  color: var(--primary-emphasis);
}

.mail-body {
  white-space: pre-wrap;
  font-family: 'Courier New', Courier, monospace;
  line-height: 1.6;
  overflow: scroll;
}
</style>