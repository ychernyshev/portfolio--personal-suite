<script setup lang="ts">
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import backendApi from "@/services/backendApi.ts";
  import {useToastStore} from "@/services/personal/useToastStore";
  import {useMailStore} from "@/services/personal/useMailStore.ts";
  import {ref} from "vue";

  const props = defineProps<{
    messageId: number;
    isArchiveInitial: boolean;
  }>();

  const emit = defineEmits(['statusUpdated']);
  const toast = useToastStore();
  const mailStore = useMailStore();

  const is_archived = ref(props.isArchiveInitial);
  const isLoading = ref(false);

  const toggleArchiveStatus = async () => {
    if (isLoading.value) return;

    isLoading.value = true;
    try {
      const nextStatus = !is_archived.value;

      const response = await backendApi.patch(`personal/user/mail/status/${props.messageId}/change_status/`, {
        field: 'is_archived',
        value: nextStatus,
      });

      if (response.data && response.data.success) {
        const serverStatus = response.data.value;
        is_archived.value = nextStatus;

        mailStore.updateMessageStatus(props.messageId, serverStatus)

        const textNotification = serverStatus ? 'The mail is marked as archived' : 'The mail is marked as not archived';
        toast.show(textNotification, 'success');

        emit('statusUpdated', { id: props.messageId, is_archived: serverStatus });
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
      @click="toggleArchiveStatus"
      :disabled="isLoading"
      :title="is_archived ? 'In archive' : 'Archived'"
      class="btn-secondary p-1 right-angle">
    <svg v-if="is_archived" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-archive" viewBox="0 0 16 16">
      <path d="M0 2a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1v7.5a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 1 12.5V5a1 1 0 0 1-1-1zm2 3v7.5A1.5 1.5 0 0 0 3.5 14h9a1.5 1.5 0 0 0 1.5-1.5V5zm13-3H1v2h14zM5 7.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5"/>
    </svg>
    <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-archive-fill" viewBox="0 0 16 16">
      <path d="M12.643 15C13.979 15 15 13.845 15 12.5V5H1v7.5C1 13.845 2.021 15 3.357 15zM5.5 7h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1 0-1M.8 1a.8.8 0 0 0-.8.8V3a.8.8 0 0 0 .8.8h14.4A.8.8 0 0 0 16 3V1.8a.8.8 0 0 0-.8-.8z"/>
    </svg>
  </button-comp>
</template>

<style scoped>

</style>