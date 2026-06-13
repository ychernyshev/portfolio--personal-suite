<script setup lang="ts">
import {computed, ref, watch} from "vue";
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import backendApi from "@/services/backendApi.ts";
  import {useToastStore} from "@/services/personal/useToastStore";
  import { useMailStore } from "@/services/personal/useMailStore";

  const props = defineProps<{
    messageId: number;
    isReadInitial: boolean;
  }>();

  const emit = defineEmits(['statusUpdated']);
  const toast = useToastStore();
  const mailStore = useMailStore();

  const isRead = ref(props.isReadInitial);
  const isLoading = ref(false);

  watch(() => props.isReadInitial, (newVal) => {
    isRead.value = newVal;
  });

  const buttonText = computed(() => isRead.value ? 'Is unread' : 'Is read');

  const toggleReadStatus = async () => {
    if (isLoading.value) return;

    isLoading.value = true;
    try {
      const nextStatus = !isRead.value;

      const response = await backendApi.patch(`personal/user/mail/status/${props.messageId}/change_status/`, {
        field: 'is_read',
        value: nextStatus,
      });

      if (response.data && response.data.success) {
        const serverStatus = response.data.value;
        const fieldStatus = response.data.field;
        isRead.value = serverStatus;

        mailStore.updateMessageStatus(props.messageId, fieldStatus, serverStatus);

        const textNotification = serverStatus ? 'The mail is marked as read' : 'The mail is marked as unread';
        toast.show(textNotification,'success');

        emit('statusUpdated', { id: props.messageId, is_read: serverStatus });
      }
    } catch (error) {
      console.error("Can not change the mail status:", error);
      toast.show('Can not change the mail status','danger');
    } finally {
      isLoading.value = false;
    }
  };
</script>

<template>
  <button-comp
      @click="toggleReadStatus"
      :disabled="isLoading"
      class="p-1 right-angle"
      :class="{ '': isRead, 'btn-secondary': !isRead }"
      :title="isRead ? 'Is unread' : 'Is read'"
  >
  </button-comp>
</template>

<style scoped>

</style>