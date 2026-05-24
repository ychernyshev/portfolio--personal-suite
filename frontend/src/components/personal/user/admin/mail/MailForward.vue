<script setup lang="ts">
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import {ref, watch} from "vue";
  import backendApi from "@/services/backendApi.ts";

  const props = defineProps<{
    message_id: number;
    subject_email: string;
    date: string;
    project_theme: string;
    mail_body: string;
  }>()

  interface Forward {
    parent_id: number;
    to_email: string;
    subject: string;
    body: string;
  }

  const formatForwardBody = (originalBody: string) => {
    return `\n\n\n---------- Forwarded message ---------\nFrom: ${props.subject_email} \nDate: ${props.date} \nSubject: ${props.project_theme}  \n\n
    On ${new Date().toLocaleDateString()} wrote:\n> ${originalBody.replace(/\n/g, '\n> ')}`;
  };

  const forwardText = ref(formatForwardBody(props.mail_body));
  const isSending = ref(false);
  const isVisible = ref(false);
  const forwardEmail = ref("");

  watch(() => props.mail_body, (newBody) => {
    forwardText.value = formatForwardBody(newBody);
  });

  const doMailForward = async () => {
    if (!forwardText.value.trim()) return;

    isSending.value = true;

    try {
      const token = localStorage.getItem('access_token');

      const forwardData: Forward = {
        parent_id: props.message_id,
        to_email: forwardEmail.value.trim(),
        subject: props.project_theme.toLowerCase().startsWith('fwd:')
            ? props.project_theme
            : `Fwd: ${props.project_theme}`,
        body: forwardText.value
      };

      const response = await backendApi.post("personal/user/admin/mail/inbound/forward/", forwardData, {
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
  <div class="collapse" id="mailForwardBox">
    <div class="card card-body text-start answer-container border-secondary text-light">
      <form @submit.prevent="doMailForward">
        <div class="">
          <input v-model="forwardEmail" type="text" class="form-control form-control-sm bg-transparent text-light border-secondary rounded-2" placeholder="Forward to...">
        </div>
        <div class="mb-2">
          <label class="small text-muted">Theme:</label>
          <input type="text" :value="'Fwd: ' + props.project_theme" class="form-control form-control-sm bg-transparent text-light border-secondary rounded-2">
        </div>
        <div class="mb-3">
          <textarea
              v-model="forwardText"
              rows="8"
              class="form-control form-control-sm answer-container border-secondary rounded-2 reply-area"
              :disabled="isSending"
          ></textarea>
        </div>
        <button-comp
            :title="isSending ? 'Sending...' : 'Forward'"
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

input::placeholder{
  color: var(--p-light-1);
  opacity: 1;
}

.reply-area {
  font-family: 'Courier New', Courier, monospace;
  line-height: 1.5;
}
</style>