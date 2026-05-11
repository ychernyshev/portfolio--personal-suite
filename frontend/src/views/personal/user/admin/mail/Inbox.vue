<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useMessageStore } from "@/services/personal/useMessageStore";
import { storeToRefs } from "pinia";

import '@/assets/personal/css/personal.css';

const messageStore = useMessageStore();
const { messages, isLoading } = storeToRefs(messageStore);

interface Message {
  id: number;
  subject_name: string;
  subject_email: string;
  project_theme: string;
  mail_body: string;
  created_at: string;
  is_read: boolean;
}
const selectedMessage = ref<Message | null>(null);

const selectMessage = (msg: Message) => {
  selectedMessage.value = msg;
  // Тут пізніше додамо запит на бекенд mark_as_read
};

onMounted( async () => {
  await messageStore.fetchMessages();
  console.log("INBOX: Завантажено повідомлень у стор:", messages.value.length);
});
</script>

<template>
  <div class="row m-0 p-3 h-100 bg-dark text-light font-monospace">
    <div class="col-md-4 border-end border-secondary overflow-auto h-100">
      <h4 class="text-warning mb-4 border-bottom border-secondary pb-2">
        <i class="fa-solid fa-inbox me-2"></i>INBOX
      </h4>

      <div v-if="isLoading" class="text-center">
        <div class="spinner-border text-warning" role="status"></div>
      </div>

      <div v-else-if="messages.length === 0" class="text-muted text-center mt-5">
        No inbound data found.
      </div>

      <div v-else class="list-group">
        <div
            v-for="msg in messages" :key="msg.id"
            @click="selectMessage(msg)"
            class="list-group-item bg-transparent text-light border-secondary mb-2 cursor-pointer msg-card"
            :class="{ 'active-msg': selectedMessage?.id === msg.id }"
        >
          <div class="d-flex justify-content-between small">
            <span class="text-info fw-bold">{{ msg.subject_name }}</span>
            <span class="text-muted">{{ new Date(msg.created_at).toLocaleDateString() }}</span>
          </div>
          <div class="text-truncate mt-1 small">{{ msg.project_theme }}</div>
        </div>
      </div>
    </div>

    <div class="col-md-8 ps-4">
      <div v-if="selectedMessage" class="h-100 d-flex flex-column">
        <div class="border-bottom border-secondary pb-3 mb-3">
          <h2 class="text-warning">{{ selectedMessage.project_theme }}</h2>
          <div class="d-flex justify-content-between">
            <span class="text-info">From: {{ selectedMessage.subject_email }}</span>
            <span class="text-muted">{{ new Date(selectedMessage.created_at).toLocaleString() }}</span>
          </div>
        </div>
        <div class="flex-grow-1 bg-black p-3 rounded border border-secondary mail-body">
          {{ selectedMessage.mail_body }}
        </div>
      </div>

      <div v-else class="h-100 d-flex align-items-center justify-content-center border border-secondary border-dashed rounded text-muted">
        Select a message to view details
      </div>
    </div>
  </div>
</template>

<style scoped>
  .msg-card { transition: all 0.2s ease; border-left: 3px solid transparent; }
  .msg-card:hover { background: rgba(255, 255, 255, 0.05) !important; }
  .active-msg {
    background: rgba(255, 193, 7, 0.1) !important;
    border-left-color: #ffc107 !important;
  }
  .mail-body { white-space: pre-wrap; font-family: 'Courier New', Courier, monospace; }
  .cursor-pointer { cursor: pointer; }
  .border-dashed { border-style: dashed !important; }
  .cursor-pointer { cursor: pointer; }
  .msg-card:hover { background: rgba(255,255,255,0.05) !important; }
  .active-msg { border-left: 4px solid #ffc107 !important; background: rgba(255,193,7,0.1) !important; }
  .mail-content { white-space: pre-wrap; line-height: 1.6; }
  .border-dashed { border-style: dashed !important; }
</style>