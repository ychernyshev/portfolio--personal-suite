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
        class="list-group-item bg-transparent text-light border-top-0 border-end-0 border-bottom-0 mb-2 cursor-pointer msg-card pt-4"
        :class="{ 'active-msg': props.selectedMessage?.id === msg.id }"
    >
      <div class="d-flex justify-content-between small">
        <span class="text-info fw-bold">{{ msg.subject_name }}</span>
        <div class="d-flex flex-row">
          <span class="text-secondary">{{ new Date(msg.created_at).toLocaleDateString() }}</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash text-warning-emphasis ms-2" viewBox="0 0 16 16">
            <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
            <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
          </svg>
        </div>
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
  box-shadow: 0 0 3rem 0.5rem rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  border-left-color: #ffc107 !important;
  border-left-width: 4px !important;
}
</style>