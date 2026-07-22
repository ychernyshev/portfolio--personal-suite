import { defineStore } from 'pinia';
import { ref } from 'vue';
import backendApi from "@/services/calculator/backendApi.js";

export const useNotificationStore = defineStore('notifications', () => {
    const messages = ref([]);

    const initMessages = async () => {
        try {
            const response = await backendApi.get('calculator/system_messages/?limit=8');
            const data = response.data.results || response.data;

            if (Array.isArray(data)) {
                const dbMessages = data.slice(0, 8).map(m => ({
                    id: m.id || Date.now() + Math.random(),
                    title: m.title || 'Notification',
                    text: m.text || '',
                    level: m.level || 'info',
                    msg_type: m.msg_type || 'info',
                    isPersistent: true,
                }));
                messages.value = dbMessages;
            }
        } catch (e) {
            console.error("Помилка завантаження повідомлень з бази даних", e);
        }
    };

    const addNotification = (payload) => {
        const newMessage = {
            id: payload.id || Date.now(),
            title: payload.title || 'Notification',
            text: payload.text || '',
            level: payload.level || 'info',
            msg_type: payload.msg_type || 'info',
            isPersistent: payload.isPersistent !== undefined ? payload.isPersistent : false,
        };

        messages.value.unshift(newMessage);

        if (messages.value.length > 8) {
            messages.value.pop();
        }
    };

    const removeNotification = (id) => {
        messages.value = messages.value.filter(m => m.id !== id);
    };

    return { messages, initMessages, addNotification, removeNotification };
});


//DEPRECATED
// import { defineStore } from 'pinia';
// import { ref } from 'vue';
//
// export const useNotificationStore = defineStore('notifications', () => {
//     const messages = ref([]);
//
//     const addNotification = (payload) => {
//         const newMessage = {
//             id: Date.now(),
//             title: payload.title || 'Notification',
//             text: payload.text || '',
//             level: payload.level || 'info',
//             msg_type: payload.msg_type || 'info',
//         };
//
//         messages.value.unshift(newMessage);
//
//         if (messages.value.length > 8) {
//             messages.value.pop();
//         }
//     };
//
//     const removeNotification = (id) => {
//         messages.value = messages.value.filter(m => m.id !== id);
//     };
//
//     return { messages, addNotification};
// });