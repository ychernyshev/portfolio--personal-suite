<script setup lang="ts">
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import {ref, watch} from "vue";

  const props = defineProps<{
    project_theme: string;
    mail_body: string;
  }>()

  const formatAnswerBody = (originalBody: string) => {
    return `\n\n\n--- On ${new Date().toLocaleDateString()} wrote:\n> ${originalBody.replace(/\n/g, '\n> ')}`;
  };

  const answerText = ref(formatAnswerBody(props.mail_body));

  watch(() => props.mail_body, (newBody) => {
    answerText.value = formatAnswerBody(newBody);
  });
</script>

<template>
  <div class="collapse" id="mailAnswerBox">
    <div class="card card-body text-start answer-container border-secondary text-light">
      <form @submit.prevent>
        <div class="mb-2">
          <label class="small text-muted">From:</label>
          <input type="text" class="form-control form-control-sm bg-transparent text-light border-secondary rounded-2" value="communicate@ychenyshev-dev.com">
        </div>
        <div class="mb-2">
          <input type="text" class="form-control form-control-sm bg-transparent text-light border-secondary rounded-2" placeholder="Send copy to...">
        </div>
        <div class="mb-2">
          <label class="small text-muted">Theme:</label>
          <input type="text" :value="'Re: ' + props.project_theme" class="form-control form-control-sm bg-transparent text-light border-secondary rounded-2">
        </div>
        <div class="mb-3">
          <textarea
              v-model="answerText"
              rows="8"
              class="form-control form-control-sm answer-container border-secondary rounded-2 reply-area"
          ></textarea>
        </div>
        <button-comp title="Reply" class="btn btn-outline-success"></button-comp>
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