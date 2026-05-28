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
      class="p-2 right-angle">
  </button-comp>
</template>

<style scoped>

</style>