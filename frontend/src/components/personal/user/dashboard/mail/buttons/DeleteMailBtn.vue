<script setup lang="ts">
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import backendApi from "@/services/backendApi.ts";
  import {useToastStore} from "@/services/personal/useToastStore.ts";
  import {useMailStore} from "@/services/personal/useMailStore.ts";
  import {ref, watch} from "vue";

  const props = defineProps<{
    messageId: number;
    isDeleteInitial: boolean;
  }>()

  const emit = defineEmits(['statusUpdated']);
  const toast = useToastStore();
  const mailStore = useMailStore();

  const is_deleted = ref(props.isDeleteInitial);
  const isLoading = ref(false);

  watch(() => props.isDeleteInitial, (newVal) => {
    is_deleted.value = newVal;
  })

  const toggleDeleteStatus = async () => {
    try {
      const nextStatus = !is_deleted.value;

      const response = await backendApi.patch(`personal/user/mail/status/${props.messageId}/change_status/`, {
        field: 'is_deleted',
        value: nextStatus,
      });

      if (response.data && response.data.success) {
        const serverStatus = response.data.value;
        const fieldStatus = response.data.field;
        is_deleted.value = serverStatus;

        mailStore.updateMessageStatus(props.messageId, fieldStatus, serverStatus)

        const textNotification = serverStatus ? 'The mail is marked as spam' : 'The mail is marked as not spam';
        toast.show(textNotification, 'success');

        emit('statusUpdated', { id: props.messageId, is_deleted: serverStatus });
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
      @click="toggleDeleteStatus"
      :disabled="isLoading"
      :title="!is_deleted ? 'Delete' : 'Deleted'"
      class="btn-warning p-1 right-angle">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
      <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
      <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
    </svg>
  </button-comp>
</template>

<style scoped>

</style>