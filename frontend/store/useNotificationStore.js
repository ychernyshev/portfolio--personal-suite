import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useNotificationStore = defineStore('notifications', () => {
    const messages = ref([]);

    const addNotification = (payload) => {
        const newMessage = {
            id: Date.now(),
            title: payload.title || 'Notification',
            text: payload.text || '',
            level: payload.level || 'info',
            msg_type: payload.msg_type || 'info',
        };

        messages.value.unshift(newMessage);

        if (messages.value.length > 2) {
            messages.value.pop();
        }
    };

    const removeNotification = (id) => {
        messages.value = messages.value.filter(m => m.id !== id);
    };

    return { messages, addNotification};
});