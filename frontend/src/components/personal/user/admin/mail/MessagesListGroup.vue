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
        class="list-group-item bg-transparent text-light border-top-0 border-end-0 border-bottom-0 mb-2 cursor-pointer msg-card p-4"
        :class="{ 'active-msg': props.selectedMessage?.id === msg.id }"
    >
      <div class="d-flex justify-content-between small">
        <span class="text-info fw-bold">{{ msg.subject_name }}</span>
        <span class="text-secondary">{{ new Date(msg.created_at).toLocaleDateString() }}</span>
      </div>
      <div class="text-truncate mt-1 small">{{ msg.project_theme }}</div>
    </div>
  </div>
</template>

<style scoped>
.msg-card {
  transition: all 0.4s ease;
  border-left: 3px solid transparent;
  cursor: pointer;
}
.msg-card:hover {
  background: #27314A !important;
  box-shadow: 0 0 3rem 0.5rem rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.active-msg {
  background: #0f172a !important;
  border-left-color: #ffc107 !important;
  border-left-width: 4px !important;
}
</style>