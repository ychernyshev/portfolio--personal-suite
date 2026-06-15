// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
import ButtonComp from "@/components/personal/ButtonComp.vue";

const props = defineProps({
  isVisible: Boolean,
  estimatedTime: { type: Number, default: 40 }
});

const emit = defineEmits(['cancel', 'timeout']);

const timeLeft = ref(props.estimatedTime);
const progress = ref(0);
let timer: ReturnType<typeof setInterval> | null = null;

// SVG mathematics
const circumference = 2 * Math.PI * 45;
const strokeOffset = computed(() => circumference - (progress.value / 100) * circumference);

const statusMessage = computed(() => {
  if (progress.value < 30) return "Initializing connection...";
  if (progress.value < 70) return "Server is starting...";
  return "Last preparations...";
});

const startLoading = () => {
  progress.value = 0;
  timeLeft.value = props.estimatedTime;

  if (timer) clearInterval(timer);

  timer = setInterval(() => {
    if (timeLeft.value > 0) {
      timeLeft.value--;
      const increment = (100 - progress.value) * 0.1;
      progress.value += increment;
    } else {
      if (timer) clearInterval(timer);
      emit('timeout');
    }
  }, 1000);
};

watch(() => props.isVisible, (newVal) => {
  if (newVal) {
    startLoading();
  } else {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }
});

onUnmounted(() => {
  if (timer) clearInterval(timer);
});
</script>

<template>
  <Transition name="fade">
    <div v-if="isVisible" class="loader-overlay">
      <div class="loader-content">
        <div class="progress-ring">
          <svg viewBox="0 0 100 100">
            <circle class="bg" cx="50" cy="50" r="45" />
            <circle
                class="bar"
                cx="50" cy="50" r="45"
                :style="{ strokeDashoffset: strokeOffset }"
            />
          </svg>
          <span class="timer-text">{{ timeLeft }}с</span>
        </div>

        <h3>{{ statusMessage }}</h3>
        <p>Our server is waking up. This is a standard "cold start" procedure.</p>

        <button-comp title="Cancel" @click="$emit('cancel')" class="btn-info btn-cancel" />
      </div>
    </div>
  </Transition>
</template>

<style scoped>
.loader-overlay {
  position: fixed;
  inset: 0;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.loader-content {
  text-align: center;
  color: var(--text-color);
  max-width: 300px;
}

.progress-ring {
  position: relative;
  width: 120px;
  height: 120px;
  margin: 0 auto 20px;
}

.timer-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.5rem;
  font-weight: bold;
}

svg { transform: rotate(-90deg); }
.bg { fill: none; stroke: rgba(255,255,255,0.1); stroke-width: 8; }
.bar {
  fill: none;
  stroke: var(--sky-blue-4, #2ecc71);
  stroke-width: 8;
  stroke-linecap: round;
  transition: stroke-dashoffset 1s linear;
  stroke-dasharray: 282.7; /* 2 * PI * 45 */
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.5s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>