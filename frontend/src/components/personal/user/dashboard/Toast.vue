// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup lang="ts">
  import { useToastStore } from '@/services/personal/useToastStore.ts';
  const toast = useToastStore();
</script>

<template>
  <Transition name="fade-toast">
    <div v-if="toast.isVisible" class="soft-toast" :class="toast.type">
      <div class="toast-icon">
        <i class="fas" :class="toast.type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'"></i>
      </div>
      <div class="toast-content">
        {{ toast.message }}
      </div>
    </div>
  </Transition>
</template>

<style scoped>
.soft-toast {
  position: fixed;
  bottom: 30px;
  right: 30px;
  display: flex;
  align-items: center;
  backdrop-filter: blur(8px);
  border-radius: 8px;
  padding: 12px 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-left: 4px solid #4caf50;
  z-index: 9999;
}
.soft-toast.danger {
  border-left-color: #f44336;
}

.fade-toast-enter-active, .fade-toast-leave-active {
  transition: all 0.4s ease;
}
.fade-toast-enter-from, .fade-toast-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
</style>