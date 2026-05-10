<script setup lang="ts">
import { ref, onMounted } from 'vue';
import api from "@/services/backendApi";

import '@/assets/personal/css/personal.css';

interface Message {
  id: number;
  subject_name: string;
  subject_email: string;
  project_theme: string;
  mail_body: string;
  created_at: string;
  is_read: boolean; // Не забудь додати це в Django модель, як ми обговорювали!
}

const messages = ref<Message[]>([]);
const selectedMessage = ref<Message | null>(null);
const isLoading = ref(false);

const fetchMessages = async () => {
  isLoading.value = true;
  try {
    const response = await api.get('/personal/inbound-messages');
    messages.value = response.data.results;
  } catch (error) {
    console.error("Failed to fetch messages", error);
  } finally {
    isLoading.value = false;
  }
};

const selectMessage = (msg: Message) => {
  selectedMessage.value = msg;
  // Тут пізніше додамо запит на бекенд mark_as_read
};

onMounted(fetchMessages);
</script>

<template>
  <div class="admin-layout-wrapper bg-dark min-vh-100">
    <nav class="navbar navbar-dark bg-black border-bottom border-secondary mb-3">
      <div class="container-fluid">
        <span class="navbar-brand text-warning font-monospace">SENTINEL_HUB</span>
      </div>
    </nav>

    <main class="container-fluid">
      <slot />
    </main>
  </div>
</template>

<style scoped>
.admin-layout-wrapper {
  background-color: #0f172a;
}
</style>