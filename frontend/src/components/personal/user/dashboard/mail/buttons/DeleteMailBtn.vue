// SPDX-License-Identifier: AGPL-3.0-or-later
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
      :class="{ '': !is_deleted, 'btn-secondary': is_deleted }"
      :title="!is_deleted ? 'Delete' : 'Deleted'"
      class="p-1 right-angle">
  </button-comp>
</template>

<style scoped>

</style>