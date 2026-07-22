// SPDX-License-Identifier: AGPL-3.0-or-later
<script setup>
import {onMounted, onUnmounted} from "vue";
import { storeToRefs } from "pinia";
import { useNotificationStore } from "../../../store/useNotificationStore.js";

// Icons
import successIcon from '../../../public/assets/calculator/images/icons/messages/success.png';
import infoIcon from '../../../public/assets/calculator/images/icons/messages/info.png';
import warningIcon from '../../../public/assets/calculator/images/icons/messages/warning.png';
import errorIcon from '../../../public/assets/calculator/images/icons/messages/error.png';

const notificationStore = useNotificationStore();
const { messages } = storeToRefs(notificationStore);

const getIcon = (type) => {
  const icons = {
    'weather': '',
    'storm': 'bi-cloud-lightning-rain',
    'success': new URL(successIcon, import.meta.url).href,
    'warning': new URL(warningIcon, import.meta.url).href,
    'info': new URL(infoIcon, import.meta.url).href,
    'error': new URL(errorIcon, import.meta.url).href,
  };
  return icons[type] || 'bi-bell';
};

onMounted(async () => {
  await notificationStore.initMessages();

  notificationStore.connectWebSocket();
});

onUnmounted(() => {
  notificationStore.disconnectWebSocket();
});

const pushLocalMessage = (newMsg) => {
  notificationStore.addNotification(newMsg);
};

defineExpose({ pushLocalMessage });
</script>

<template>
  <div class="notification-stack w-100 pl-4 pr-1">
    <transition-group name="list" tag="div">
      <div v-for="msg in messages" :key="msg.id" class="msg-card shadow-sm rounded-2" :class="msg.level">
        <div class="d-flex align-items-center">
          <img :src="getIcon(msg.msg_type)" class="me-2 text-dark icon" alt=""/>
          <div>
            <h6 class="mb-0 text-dark">{{ msg.title }}</h6>
            <small class="text-muted">{{ msg.text }}</small>
          </div>
        </div>
      </div>
    </transition-group>
  </div>
</template>

<style scoped>
.notification-stack {
  position: absolute;
  top: -20rem;
  right: 10px;
  z-index: 1000;
  width: 1400px;
}

.msg-card {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 12px;
  margin-bottom: 8px;
  transition: all 0.5s ease;
}

.icon {
  width: 24px;
  height: 24px;
  filter: drop-shadow(0 0 2px rgba(0,0,0,0.2));
}

@media (min-width: 1200px) {
  .notification-stack {
    width: 390px;
  }
}

.msg-card.success { border-left: 4px solid #198754; }
.msg-card.warning { border-left: 4px solid #ffc107; }
.msg-card.danger  { border-left: 4px solid #dc3545; }
.msg-card.info    { border-left: 4px solid #0dcaf0; }

.list-enter-from {
  opacity: 0;
  transform: translateX(30px);
}
.list-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}
.list-leave-active {
  position: absolute;
  width: 100%;
}
</style>


<!--DEPRECATED-->
<!--<script setup>-->
<!--import {ref, onMounted, computed, isMemoSame} from "vue";-->
<!--import backendApi from "../../services/calculator/backendApi.js";-->
<!--import { storeToRefs } from "pinia";-->
<!--import { useNotificationStore } from "../../../store/useNotificationStore.js";-->

<!--// Icons-->
<!--import successIcon from '../../../public/assets/calculator/images/icons/messages/success.png';-->
<!--import infoIcon from '../../../public/assets/calculator/images/icons/messages/info.png';-->
<!--import warningIcon from '../../../public/assets/calculator/images/icons/messages/warning.png';-->
<!--import errorIcon from '../../../public/assets/calculator/images/icons/messages/error.png';-->

<!--const notificationStore = useNotificationStore();-->
<!--const { messages } = storeToRefs(notificationStore);-->

<!--// Icons-->
<!--const getIcon = (type) => {-->
<!--  const icons = {-->
<!--    'weather': '',-->
<!--    'storm': 'bi-cloud-lightning-rain',-->
<!--    'success': new URL(successIcon, import.meta.url).href,-->
<!--    'warning': new URL(warningIcon, import.meta.url).href,-->
<!--    'info': new URL(infoIcon, import.meta.url).href,-->
<!--    'error': new URL(errorIcon, import.meta.url).href,-->
<!--  };-->
<!--  return icons[type] || 'bi-bell';-->
<!--};-->

<!--// const fetchLatestMessages = async () => {-->
<!--//   try {-->
<!--//     const response = await backendApi.get('system-messages/?limit=2');-->
<!--//     messages.value = response.data;-->
<!--//   } catch (e) {-->
<!--//     console.error("Помилка завантаження повідомлень", e);-->
<!--//   }-->
<!--// };-->

<!--const pushLocalMessage = (newMsg) => {-->
<!--  messages.value.unshift({-->
<!--    id: Date.now(),-->
<!--    ...newMsg-->
<!--  });-->
<!--  if (messages.value.length > 2) {-->
<!--    messages.value.pop();-->
<!--  }-->
<!--};-->

<!--defineExpose({ pushLocalMessage });-->
<!--// defineExpose({ fetchLatestMessages, pushLocalMessage });-->

<!--// onMounted(fetchLatestMessages);-->
<!--</script>-->

<!--<template>-->
<!--  <div class="notification-stack w-100 pl-4 pr-1">-->
<!--    <transition-group name="list" tag="div">-->
<!--      <div v-for="msg in messages" :key="msg.id" class="msg-card shadow-sm rounded-2" :class="msg.level">-->
<!--        <div class="d-flex align-items-center">-->
<!--          <img :src="getIcon(msg.msg_type)" class="me-2 text-dark icon"  alt=""/>-->
<!--          <div>-->
<!--            <h6 class="mb-0 text-dark">{{ msg.title }}</h6>-->
<!--            <small class="text-muted">{{ msg.text }}</small>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </transition-group>-->
<!--  </div>-->
<!--</template>-->

<!--<style scoped>-->
<!--.notification-stack {-->
<!--  position: absolute;-->
<!--  top: -20rem;-->
<!--  right: 10px;-->
<!--  z-index: 1000;-->
<!--  width: 1400px;-->
<!--}-->

<!--.msg-card {-->
<!--  background: rgba(255, 255, 255, 0.6);-->
<!--  backdrop-filter: blur(10px);-->
<!--  -webkit-backdrop-filter: blur(10px);-->
<!--  border: 1px solid rgba(255, 255, 255, 0.3);-->
<!--  padding: 12px;-->
<!--  margin-bottom: 8px;-->
<!--  transition: all 0.5s ease;-->
<!--}-->

<!--.icon {-->
<!--  width: 24px;-->
<!--  height: 24px;-->
<!--  filter: drop-shadow(0 0 2px rgba(0,0,0,0.2));-->
<!--}-->


<!--@media (min-width: 1200px) {-->
<!--  .notification-stack {-->
<!--    width: 390px;-->
<!--  }-->
<!--}-->

<!--.msg-card.success { border-left: 4px solid #198754; }-->
<!--.msg-card.warning { border-left: 4px solid #ffc107; }-->
<!--.msg-card.danger  { border-left: 4px solid #dc3545; }-->
<!--.msg-card.info    { border-left: 4px solid #0dcaf0; }-->

<!--.list-enter-from {-->
<!--  opacity: 0;-->
<!--  transform: translateX(30px);-->
<!--}-->
<!--.list-leave-to {-->
<!--  opacity: 0;-->
<!--  transform: translateY(-30px);-->
<!--}-->
<!--.list-leave-active {-->
<!--  position: absolute;-->
<!--  width: 100%;-->
<!--}-->
<!--</style>-->