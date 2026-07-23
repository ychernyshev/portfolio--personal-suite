import { defineStore } from 'pinia';
import { ref } from 'vue';
import backendApi from "@/services/backendApi.ts";

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

    const initWebSocket = () => {
        const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
        const host = 'localhost:8001';

        const socket = new WebSocket(`${protocol}${host}/ws/calculator/events/`);

        socket.onopen = () => {
            console.log("WS: Connected to Calculator events successfully.");
        };

        socket.onmessage = (event) => {
            try {
                const data = JSON.parse(event.data);
                console.log("WS: New event received:", data);

                addNotification(data);
            } catch (e) {
                console.error("WS: Failed to parse incoming message", e);
            }
        };

        socket.onerror = (error) => {
            console.error("WS: WebSocket error observed:", error);
        };

        socket.onclose = (event) => {
            console.warn("WS: Connection lost. Trying to reconnect in 3s...", event.reason);
            setTimeout(initWebSocket, 3000);
        };
    };

    const addNotification = (eventData) => {
        const newMessage = {
            id: eventData.id || Date.now(),
            title: eventData.title || 'System Notification',
            text: eventData.payload?.message || eventData.title || '',
            level: eventData.level ? eventData.level.toLowerCase() : 'info',
            msg_type: eventData.category ? eventData.category.toLowerCase() : 'info',
            isPersistent: eventData.is_persistent,
        };

        messages.value.unshift(newMessage);

        if (messages.value.length > 8) {
            messages.value.pop();
        }
    };

    const removeNotification = (id) => {
        messages.value = messages.value.filter(m => m.id !== id);
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
        initWebSocket,
        disconnectWebSocket
    };
});