// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup lang="ts">
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import backendApi from "@/services/backendApi.ts";
  import {useToastStore} from "@/services/personal/useToastStore";
  import {useMailStore} from "@/services/personal/useMailStore.ts";
  import {ref, watch} from "vue";

  const props = defineProps<{
    messageId: number;
    isArchiveInitial: boolean;
  }>();

  const emit = defineEmits(['statusUpdated']);
  const toast = useToastStore();
  const mailStore = useMailStore();

  const is_archived = ref(props.isArchiveInitial);
  const isLoading = ref(false);

  watch(() => props.isArchiveInitial, (newVal) => {
    is_archived.value = newVal;
  });

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
        const fieldStatus = response.data.field;
        is_archived.value = serverStatus;

        mailStore.updateMessageStatus(props.messageId, fieldStatus, serverStatus)

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
      :class="{ '': is_archived, 'btn-secondary': !is_archived }"
      :title="is_archived ? 'To archive' : 'Is archived'"
      class="p-1 right-angle">
  </button-comp>
</template>

<style scoped>

</style>