<script setup lang="ts">
import {ref, onMounted} from 'vue';
import {useMailStore} from "@/services/personal/useMailStore";
import {storeToRefs} from "pinia";

import '@/assets/personal/css/personal.css';
import MessagesListGroup from "@/components/personal/user/dashboard/mail/MessagesListGroup.vue";
import SelectedMessage from "@/components/personal/user/dashboard/mail/SelectedMessage.vue";
import CountUnread from "@/components/personal/user/dashboard/mail/countUnread.vue";

const messageStore = useMailStore();
const {messages, filteredMessages, currentFolder, isLoading} = storeToRefs(messageStore);

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

const selectedMessage = ref<Message | null>(null);

const selectMessage = (msg: Message) => {
  selectedMessage.value = msg;
};

onMounted(async () => {
  await messageStore.fetchMessages();
  messageStore.initWebSocket();
});
</script>

<template>
  <div class="row m-0 h-100 text-light font-monospace">
    <div class="col-md-4 m-0 p-0 pt-3 h-100 d-flex flex-column">
      <div class=" d-flex flex-row align-items-baseline justify-content-between">
        <h4 class="text-warning mb-4 ps-3">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-inbox"
               viewBox="0 0 16 16">
            <path
                d="M4.98 4a.5.5 0 0 0-.39.188L1.54 8H6a.5.5 0 0 1 .5.5 1.5 1.5 0 1 0 3 0A.5.5 0 0 1 10 8h4.46l-3.05-3.812A.5.5 0 0 0 11.02 4zm9.954 5H10.45a2.5 2.5 0 0 1-4.9 0H1.066l.32 2.562a.5.5 0 0 0 .497.438h12.234a.5.5 0 0 0 .496-.438zM3.809 3.563A1.5 1.5 0 0 1 4.981 3h6.038a1.5 1.5 0 0 1 1.172.563l3.7 4.625a.5.5 0 0 1 .105.374l-.39 3.124A1.5 1.5 0 0 1 14.117 13H1.883a1.5 1.5 0 0 1-1.489-1.314l-.39-3.124a.5.5 0 0 1 .106-.374z"/>
          </svg>
          <span>
          INBOX
            <span class="translate-middle badge rounded-pill bg-danger">
              <count-unread/>
              <span class="visually-hidden">unread messages</span>
            </span>
          </span>
        </h4>
        <div>
          <button
              :class="{ 'text-success': currentFolder === 'inbox', 'text-secondary': currentFolder !== 'inbox' }"
              @click="currentFolder = 'inbox'"
              type="button"
              class="ps-2 pe-2 border-0 bg-transparent text-success">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill"
                 viewBox="0 0 16 16">
              <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0"/>
              <path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8m8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7"/>
            </svg>
          </button>
          <button
              :class="{ 'text-info': currentFolder === 'archive', 'text-secondary': currentFolder !== 'archive' }"
              @click="currentFolder = 'archive'"
              class="ps-2 pe-2 border-0 bg-transparent text-info">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-archive-fill"
                 viewBox="0 0 16 16">
              <path
                  d="M12.643 15C13.979 15 15 13.845 15 12.5V5H1v7.5C1 13.845 2.021 15 3.357 15zM5.5 7h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1 0-1M.8 1a.8.8 0 0 0-.8.8V3a.8.8 0 0 0 .8.8h14.4A.8.8 0 0 0 16 3V1.8a.8.8 0 0 0-.8-.8z"/>
            </svg>
          </button>
          <button
              :class="{ 'text-warning': currentFolder === 'spam', 'text-secondary': currentFolder !== 'spam' }"
              @click="currentFolder = 'spam'"
              class="ps-2 pe-2 border-0 bg-transparent text-warning">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fire"
                 viewBox="0 0 16 16">
              <path
                  d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16m0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15"/>
            </svg>
          </button>
          <button
              :class="{ 'text-danger': currentFolder === 'trash', 'text-secondary': currentFolder !== 'trash' }"
              @click="currentFolder = 'trash'"
              class="ps-2 pe-2 border-0 bg-transparent text-danger">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill"
                 viewBox="0 0 16 16">
              <path
                  d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5M8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5m3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0"/>
            </svg>
          </button>
        </div>
      </div>
      <div class="inbox-list-container">
        <div v-if="isLoading" class="text-center">
          <div class="text-warning" role="status"></div>
        </div>
        <div v-else-if="messages.length === 0" class="text-muted text-center mt-5">
          No inbound data found.
        </div>
        <messages-list-group
            :messages="filteredMessages"
            :selected-message="selectedMessage"
            :on-select="selectMessage"
        />
      </div>
    </div>
    <div class="col-md-8 m-0 p-0">
      <selected-message
          :message="selectedMessage"
      />
    </div>
  </div>
</template>

<style scoped>
.row.h-100 {
  height: 100% !important;
  max-height: 100%;
}

.inbox-list-container {
  height: calc(100% - 60px);
  overflow-y: scroll;
  flex-grow: 1;
}

.col-md-8 {
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>