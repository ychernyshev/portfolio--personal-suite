import { defineStore } from 'pinia';
import { ref } from 'vue';
import backendApi from "@/services/calculator/backendApi.js";

export const useNotificationStore = defineStore('notifications', () => {
    const messages = ref([]);
    let socket = null;

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

    // Підключення до WebSocket бекенду
    const connectWebSocket = () => {
        if (socket && socket.readyState === WebSocket.OPEN) return;

        const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
        const host = window.location.host; 

        socket = new WebSocket(`${protocol}${host}/ws/inbox/`);

        socket.onopen = () => {
            console.log("WebSocket підключено до inbox_updates");
        };

        socket.onmessage = (event) => {
            try {
                const data = JSON.parse(event.data);
                // Щойно бекенд через сигнал пушить дані — додаємо їх у стейт!
                addNotification(data);
            } catch (e) {
                console.error("Помилка парсингу WebSocket повідомлення", e);
            }
        };

        socket.onclose = () => {
            console.log("WebSocket з'єднання закрите. Спроба перепідключення через 5 сек...");
            setTimeout(connectWebSocket, 5000); // Автоматичний реконект
        };

        socket.onerror = (error) => {
            console.error("WebSocket помилка:", error);
            socket.close();
        };
    };

    const disconnectWebSocket = () => {
        if (socket) {
            socket.close();
            socket = null;
        }
    };

    return {
        messages,
        initMessages,
        addNotification,
        removeNotification,
        connectWebSocket,
        disconnectWebSocket
    };
});