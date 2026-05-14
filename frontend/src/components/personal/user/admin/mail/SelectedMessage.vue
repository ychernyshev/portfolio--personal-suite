<script setup lang="ts">
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
  <div v-if="props.message" class="h-100 d-flex flex-column">
    <div class="border-bottom border-secondary pb-3 mb-3">
      <h2 class="text-warning">{{ props.message.project_theme }}</h2>
      <div class="d-flex justify-content-between">
        <span class="text-info">From: {{ props.message.subject_email }}</span>
        <span class="text-muted">{{ new Date(props.message.created_at).toLocaleString() }}</span>
      </div>
    </div>
    <div class="flex-grow-1 bg-black p-3 rounded border border-secondary mail-body">
      {{ props.message.mail_body }}
    </div>
  </div>

  <div v-else class="h-100 d-flex align-items-center justify-content-center border border-secondary border-dashed rounded text-muted">
    Select a message to view details
  </div>
</template>

<style scoped>
.mail-body {
  white-space: pre-wrap;
  font-family: 'Courier New', Courier, monospace;
  line-height: 1.6;
}
.border-dashed {
  border-style: dashed !important;
}
</style>