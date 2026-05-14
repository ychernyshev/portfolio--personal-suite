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

      <messages-list-group
          :messages="messages"
          :selected-message="selectedMessage"
          :on-select="selectMessage"
      />

    </div>

    <div class="col-md-8 ps-4">
      <selected-message
          :message="selectedMessage"
      />
    </div>
  </div>
</template>

<style scoped></style>