<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useMessageStore } from "@/services/personal/useMessageStore";
import { storeToRefs } from "pinia";

import '@/assets/personal/css/personal.css';
import MessagesListGroup from "@/components/personal/user/admin/mail/MessagesListGroup.vue";
import SelectedMessage from "@/components/personal/user/admin/mail/SelectedMessage.vue";

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
  messageStore.initWebSocket();
});
</script>

<template>
  <div class="row m-0 h-100 text-light font-monospace">
    <div class="col-md-4 m-0 p-0 pt-3 inbox-list-container">
      <h4 class="text-warning mb-4 ps-3">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-inbox" viewBox="0 0 16 16">
          <path d="M4.98 4a.5.5 0 0 0-.39.188L1.54 8H6a.5.5 0 0 1 .5.5 1.5 1.5 0 1 0 3 0A.5.5 0 0 1 10 8h4.46l-3.05-3.812A.5.5 0 0 0 11.02 4zm9.954 5H10.45a2.5 2.5 0 0 1-4.9 0H1.066l.32 2.562a.5.5 0 0 0 .497.438h12.234a.5.5 0 0 0 .496-.438zM3.809 3.563A1.5 1.5 0 0 1 4.981 3h6.038a1.5 1.5 0 0 1 1.172.563l3.7 4.625a.5.5 0 0 1 .105.374l-.39 3.124A1.5 1.5 0 0 1 14.117 13H1.883a1.5 1.5 0 0 1-1.489-1.314l-.39-3.124a.5.5 0 0 1 .106-.374z"/>
        </svg>
        INBOX
      </h4>

      <div v-if="isLoading" class="text-center">
        <div class="text-warning" role="status"></div>
      </div>

      <div v-else-if="messages.length === 0" class="text-muted text-center mt-5">
        No inbound data found.
      </div>

      <messages-list-group
          :messages="messages"
          :selected-message="selectedMessage"
          :on-select="selectMessage"
      />

    </div>

    <div class="col-md-8 m-0 p-0">
      <selected-message
          :message="selectedMessage"
      />
    </div>
  </div>
</template>

<style scoped>
.inbox-list-container {
  height: 100vh;
  overflow: scroll;
}
</style>