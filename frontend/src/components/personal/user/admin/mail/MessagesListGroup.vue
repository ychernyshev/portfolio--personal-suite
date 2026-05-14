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

interface IProps {
  messages: Message[];
  selectedMessage: Message | null;
  onSelect: (msg: Message) => void;
}

const props = defineProps<IProps>();
</script>

<template>
  <div class="list-group">
    <div
        v-for="msg in props.messages"
        :key="msg.id"
        @click="props.onSelect(msg)"
        class="list-group-item bg-transparent text-light border-secondary mb-2 cursor-pointer msg-card"
        :class="{ 'active-msg': props.selectedMessage?.id === msg.id }"
    >
      <div class="d-flex justify-content-between small">
        <span class="text-info fw-bold">{{ msg.subject_name }}</span>
        <span class="text-muted">{{ new Date(msg.created_at).toLocaleDateString() }}</span>
      </div>
      <div class="text-truncate mt-1 small">{{ msg.project_theme }}</div>
    </div>
  </div>
</template>

<style scoped>
.msg-card {
  transition: all 0.2s ease;
  border-left: 3px solid transparent;
  cursor: pointer;
}
.msg-card:hover {
  background: rgba(255, 255, 255, 0.05) !important;
}
.active-msg {
  background: rgba(255, 193, 7, 0.1) !important;
  border-left-color: #ffc107 !important;
  border-left-width: 4px !important;
}
</style>