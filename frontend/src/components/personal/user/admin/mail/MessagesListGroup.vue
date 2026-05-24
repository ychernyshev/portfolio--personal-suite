<script setup lang="ts">
interface Message {
  id: number;
  subject_name: string;
  subject_email: string;
  project_theme: string;
  mail_body: string;
  created_at: string;
  is_read: boolean;
  is_archived: boolean;
  is_spam: boolean;
  is_deleted: boolean;
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
        v-show="!msg.is_archived || !msg.is_spam || !msg.is_deleted"
        class="list-group-item bg-transparent text-light border-top-0 border-end-0 border-bottom-0 mb-2 cursor-pointer msg-card pt-4"
        :class="{ 'active-msg': props.selectedMessage?.id === msg.id }"
    >
      {{ msg.is_archived }}
      <div class="d-flex justify-content-between small">
        <span class="text-info fw-bold">{{ msg.subject_name }}</span>
        <div class="d-flex flex-row">
          <span class="text-secondary">{{ new Date(msg.created_at).toLocaleDateString() }}</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash text-warning-emphasis ms-2" viewBox="0 0 16 16">
            <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
            <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
          </svg>
          <svg v-if="msg.is_read" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-slash" viewBox="0 0 16 16">
            <path d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7 7 0 0 0-2.79.588l.77.771A6 6 0 0 1 8 3.5c4.478 0 7.268 4.73 7.474 5.08-.102.166-.49.734-1.127 1.336l.752.752zM7.42 5.617l1.16 1.16a2.1 2.1 0 0 1 .132 2.193l1.56 1.56a4 4 0 0 0-.58-4.784 4 4 0 0 0-2.272-.13z"/>
            <path d="M4.908 6.754a3 3 0 0 0 3.75 3.752l.955.955A4.01 4.01 0 0 1 8 12c-4.478 0-7.268-4.73-7.474-5.08.102-.166.49-.734 1.127-1.336a7 7 0 0 1 2.301-1.633l.954.953zm.648-.648-.954-.954A6.14 6.14 0 0 0 1 8s3 5.5 8 5.5a7 7 0 0 0 2.79-.588l-.77-.771A6 6 0 0 1 8 12.5c-4.478 0-7.268-4.73-7.474-5.08a11.5 11.5 0 0 1 1.127-1.336 6 6 0 0 1 1.745-1.328l.77.77z"/>
            <path d="M11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">
            <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8M1.173 8a13 13 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5s3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5s-3.879-1.168-5.168-2.457A13 13 0 0 1 1.172 8z"/>
            <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5M4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0"/>
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