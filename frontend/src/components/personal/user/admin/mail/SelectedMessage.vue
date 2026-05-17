<script setup lang="ts">
import MailReply from "@/components/personal/user/admin/mail/MailReply.vue";
import MailAnswer from "@/components/personal/user/admin/mail/MailAnswer.vue";
import ButtonComp from "@/components/personal/ButtonComp.vue";

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
  <div v-if="props.message" class="d-flex flex-column mail-body-container mt-3 ms-3 pt-3 ps-3 pe-3 h-75">
    <div class="pb-3 mb-3">
      <h2 class="text-warning">{{ props.message.project_theme }}</h2>
      <div class="d-flex justify-content-between">
        <span class="text-info">From: {{ props.message.subject_email }}</span>
        <span class="text-info-emphasis bg-body-tertiary ps-2 pe-2 rounded-2">{{ new Date(props.message.created_at).toLocaleString() }}</span>
      </div>
    </div>
    <div class="flex-grow-1 p-3 rounded border-0 mail-body">
      <div class="d-flex flex-row justify-content-between">
        <p>
          <a class="btn btn-success rounded-2" data-bs-toggle="collapse" href="#mailReplyBox" role="button" aria-expanded="false" aria-controls="mailReplyBox">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-90deg-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M1.146 4.854a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 4H12.5A2.5 2.5 0 0 1 15 6.5v8a.5.5 0 0 1-1 0v-8A1.5 1.5 0 0 0 12.5 5H2.707l3.147 3.146a.5.5 0 1 1-.708.708z"/>
            </svg>
          </a>
        </p>
        <div>
          <button-comp title="Mark as New" class="btn-success p-1 right-angle"></button-comp>
          <button-comp title="To archive" class="btn-secondary p-1 right-angle">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-archive" viewBox="0 0 16 16">
              <path d="M0 2a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1v7.5a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 1 12.5V5a1 1 0 0 1-1-1zm2 3v7.5A1.5 1.5 0 0 0 3.5 14h9a1.5 1.5 0 0 0 1.5-1.5V5zm13-3H1v2h14zM5 7.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5"/>
            </svg>
          </button-comp>
          <button-comp title="Delete" class="btn-warning p-1 right-angle">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
              <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
              <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
            </svg>
          </button-comp>
          <button-comp title="Spam" class="btn-danger p-1 right-angle">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fire" viewBox="0 0 16 16">
              <path d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16m0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15"/>
            </svg>
          </button-comp>
        </div>
        <p>
          <a class="btn btn-secondary" data-bs-toggle="collapse" href="#mailAnswerBox" role="button" aria-expanded="false" aria-controls="mailAnswerBox">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-90deg-right" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M14.854 4.854a.5.5 0 0 0 0-.708l-4-4a.5.5 0 0 0-.708.708L13.293 4H3.5A2.5 2.5 0 0 0 1 6.5v8a.5.5 0 0 0 1 0v-8A1.5 1.5 0 0 1 3.5 5h9.793l-3.147 3.146a.5.5 0 0 0 .708.708z"/>
            </svg>
          </a>
        </p>
      </div>
      {{ props.message.mail_body }}
      <div class="mt-5">
        <mail-reply
            :subject_email="props.message.subject_email"
            :project_theme="props.message.project_theme"
            :mail_body="props.message.mail_body"
        />
        <mail-answer
            :project_theme="props.message.project_theme"
            :mail_body="props.message.mail_body"
        />
      </div>
    </div>
  </div>

  <div v-else class="h-100 d-flex align-items-center justify-content-center border-0 rounded text-muted">
    Select a message to view details
  </div>
</template>

<style scoped>
.mail-body-container {
  background: var(--p-light-2);
  border-top-left-radius: 1.2rem;
  color: var(--primary-emphasis);
}

.mail-body {
  white-space: pre-wrap;
  font-family: 'Courier New', Courier, monospace;
  line-height: 1.6;
  overflow: scroll;
}
</style>