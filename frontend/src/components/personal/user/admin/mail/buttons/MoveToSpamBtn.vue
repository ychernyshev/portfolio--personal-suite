<script setup lang="ts">
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import backendApi from "@/services/backendApi.ts";
  import {useToastStore} from "@/services/personal/useToastStore.ts";
  import {useMailStore} from "@/services/personal/useMailStore.ts";
  import {ref, watch} from "vue";

  const props = defineProps<{
    messageId: number;
    isSpamInitial: boolean;
  }>()

  const emit = defineEmits(['statusUpdated']);
  const toast = useToastStore();
  const mailStore = useMailStore();

  const is_spam = ref(props.isSpamInitial);
  const isLoading = ref(false);

  watch(() => props.isSpamInitial, (newVal) => {
    is_spam.value = newVal;
  })

  const toggleSpamStatus = async () => {
    try {
      const nextStatus = !is_spam.value;

      const response = await backendApi.patch(`personal/user/mail/status/${props.messageId}/change_status/`, {
        field: 'is_spam',
        value: nextStatus,
      });

      if (response.data && response.data.success) {
        const serverStatus = response.data.value;
        const fieldStatus = response.data.field;
        is_spam.value = serverStatus;

        mailStore.updateMessageStatus(props.messageId, fieldStatus, serverStatus)

        const textNotification = serverStatus ? 'The mail is marked as spam' : 'The mail is marked as not spam';
        toast.show(textNotification, 'success');

        emit('statusUpdated', { id: props.messageId, is_spam: serverStatus });
      }
    }catch (error) {
      console.error("Can not change the mail status:", error);
      toast.show('Can not change the mail status','danger');
    } finally {
      isLoading.value = false;
    }
  };
</script>

<template>
  <button-comp
      @click="toggleSpamStatus"
      :disabled="isLoading"
      :title="!is_spam ? 'Add to spam' : 'Added to spam'"
      class="btn-danger p-1 right-angle">
    <svg v-if="!is_spam" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fire" viewBox="0 0 16 16">
      <path d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16m0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15"/>
    </svg>
  </button-comp>
</template>

<style scoped>

</style>