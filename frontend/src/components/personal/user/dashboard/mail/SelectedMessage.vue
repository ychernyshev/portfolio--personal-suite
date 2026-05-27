<script setup lang="ts">
import MailReply from "@/components/personal/user/dashboard/mail/MailReply.vue";
import MailForward from "@/components/personal/user/dashboard/mail/MailForward.vue";
import ButtonComp from "@/components/personal/ButtonComp.vue";
import MarkAsUnreadBtn from "@/components/personal/user/dashboard/mail/buttons/MarkAsUnreadBtn.vue";
import MoveToArchiveBtn from "@/components/personal/user/dashboard/mail/buttons/MoveToArchiveBtn.vue";
import MoveToSpamBtn from "@/components/personal/user/dashboard/mail/buttons/MoveToSpamBtn.vue";
import DeleteMailBtn from "@/components/personal/user/dashboard/mail/buttons/DeleteMailBtn.vue";

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
          <a 
              class="btn btn-success rounded-2"
              data-bs-toggle="collapse"
              href="#mailReplyBox"
              role="button"
              aria-expanded="false"
              aria-controls="mailReplyBox">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-90deg-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M1.146 4.854a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 4H12.5A2.5 2.5 0 0 1 15 6.5v8a.5.5 0 0 1-1 0v-8A1.5 1.5 0 0 0 12.5 5H2.707l3.147 3.146a.5.5 0 1 1-.708.708z"/>
            </svg>
          </a>
        </p>
        <div>
          <mark-as-unread-btn
              :message-id=props.message.id
              :is-read-initial="props.message.is_read"
          />
          <move-to-archive-btn
            :message-id=props.message.id
            :is-archive-initial="props.message.is_archived"
          />
          <delete-mail-btn
            :message-id="props.message.id"
            :is-delete-initial="props.message.is_deleted"
          />
          <move-to-spam-btn
            :message-id="props.message.id"
            :is-spam-initial="props.message.is_spam"
          />
        </div>
        <p>
          <a class="btn btn-secondary" data-bs-toggle="collapse" href="#mailForwardBox" role="button" aria-expanded="false" aria-controls="mailForwardBox">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-90deg-right" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M14.854 4.854a.5.5 0 0 0 0-.708l-4-4a.5.5 0 0 0-.708.708L13.293 4H3.5A2.5 2.5 0 0 0 1 6.5v8a.5.5 0 0 0 1 0v-8A1.5 1.5 0 0 1 3.5 5h9.793l-3.147 3.146a.5.5 0 0 0 .708.708z"/>
            </svg>
          </a>
        </p>
      </div>
      <div class="mb-3">
        <mail-reply
            :message_id="props.message.id"
            :subject_email="props.message.subject_email"
            :project_theme="props.message.project_theme"
            :mail_body="props.message.mail_body"
        />
        <mail-forward
            :message_id="props.message.id"
            :subject_email="props.message.subject_email"
            :date="props.message.created_at"
            :project_theme="props.message.project_theme"
            :mail_body="props.message.mail_body"
        />
      </div>
      <div class="select-message-container">
        {{ props.message.mail_body }}
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

.select-message-container {
  overflow-y: scroll;
}
</style>