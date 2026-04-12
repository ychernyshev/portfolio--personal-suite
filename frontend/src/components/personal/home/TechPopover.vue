<script setup lang="ts">
import { ref } from 'vue';

defineProps<{
  content: string;
}>();

const show = ref(false);
</script>

<template>
  <div
      class="popover-container"
      @mouseenter="show = true"
      @mouseleave="show = false"
  >
    <slot />

    <Transition name="fade">
      <div v-if="show" class="custom-popover">
        <div class="popover-arrow"></div>
        <div class="popover-content">
          {{ content }}
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.popover-container {
  position: relative;
  display: inline-block;
}

.custom-popover {
  position: absolute;
  bottom: 120%;
  left: 50%;
  transform: translateX(-50%);
  width: 250px;
  padding: 12px;
  background: rgba(20, 25, 35, 0.9);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: #fff;
  font-size: 0.9rem;
  line-height: 1.5;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
  z-index: 1000;
  pointer-events: none;
}

.popover-arrow {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-width: 8px 8px 0;
  border-style: solid;
  border-color: rgba(20, 25, 35, 0.9) transparent transparent;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateX(-50%) translateY(10px);
}
</style>