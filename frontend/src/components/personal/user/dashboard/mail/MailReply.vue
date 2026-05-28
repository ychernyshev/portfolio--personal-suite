<script setup lang="ts">
import {ref, watch} from "vue";
import ButtonComp from "@/components/personal/ButtonComp.vue";
import backendApi from "@/services/backendApi.ts";

const props = defineProps<{
  message_id: number;
  subject_email: string;
  project_theme: string;
  mail_body: string;
}>();

interface Reply {
  parent_id: number;
  to_email: string;
  cc_email?: string;
  subject: string;
  body: string;
}

const formatReplyBody = (originalBody: string) => {
  return `\n\n\n--- On ${new Date().toLocaleDateString()} wrote:\n> ${originalBody.replace(/\n/g, '\n> ')}`;
};

const replyText = ref(formatReplyBody(props.mail_body));
const isSending = ref(false);
const isVisible = ref(false);
const ccEmail = ref("");

watch(() => props.mail_body, (newBody) => {
  replyText.value = formatReplyBody(newBody);
});

const sendReply = async () => {
  if (!replyText.value.trim()) return;

  isSending.value = true;
  try {
    const token = localStorage.getItem('access_token');

    const replyData: Reply = {
      parent_id: props.message_id,
      to_email: props.subject_email,
      subject: props.project_theme.toLowerCase().startsWith('re:')
          ? props.project_theme
          : `Re: ${props.project_theme}`,
      body: replyText.value
    };

    if (ccEmail.value.trim()) {
      replyData.cc_email = ccEmail.value.trim();
    }

    const response = await backendApi.post("personal/user/dashboard/mail/inbound/reply/", replyData, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (response.status === 201 || response.data?.success) {
      alert("Mail sent successfully!");
      isVisible.value = false; // ховаємо форму
    }
  } catch (error) {
    console.error("Sending error:", error);
    alert("Failed to send email.");
  } finally {
    isSending.value = false;
  }
};
</script>

<template>
  <div class="collapse" id="mailReplyBox">
    <div class="card card-body text-start answer-container border-secondary text-light">
      <form @submit.prevent="sendReply">
        <div class="mb-2">
          <label class="small text-muted">To:</label>
          <input type="text" class="form-control form-control-sm bg-transparent text-light border-secondary rounded-2"
                 :value="props.subject_email">
        </div>
        <div class="mb-2">
          <input
              v-model="ccEmail"
              type="text"
              class="form-control form-control-sm bg-transparent text-light border-secondary rounded-2"
              placeholder="Send copy to...">
        </div>
        <div class="mb-2">
          <label class="small text-muted">Theme:</label>
          <input type="text" :value="'Re: ' + props.project_theme"
                 class="form-control form-control-sm bg-transparent text-light border-secondary rounded-2">
        </div>
        <div class="mb-3">
          <textarea
              v-model="replyText"
              rows="8"
              class="form-control form-control-sm answer-container border-secondary rounded-2 reply-area"
              :disabled="isSending"
          ></textarea>
        </div>
        <button-comp
            :title="isSending ? 'Sending...' : 'Reply'"
            class="btn btn-outline-success"
            :disabled="isSending"
        ></button-comp>
      </form>
    </div>
  </div>
</template>

<style scoped>
.answer-container {
  background: var(--deep-ocean-rgba-1);
  border-top-left-radius: 1.2rem;
  color: var(--p-light-2);
}

input::placeholder {
  color: var(--p-light-1);
  opacity: 1;
}

.reply-area {
  font-family: 'Courier New', Courier, monospace;
  line-height: 1.5;
}
</style>