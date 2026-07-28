import { defineStore } from 'pinia';
import { ref } from 'vue';
import backendApi from "@/services/backendApi.ts";

export const useNotificationStore = defineStore('notifications', () => {
    const messages = ref([]);
    let socket = null;

    const initMessages = async () => {
        try {
            const response = await backendApi.get('calculator/system_event/?limit=8');
            const data = response.data.results || response.data;

            if (Array.isArray(data)) {
                const dbMessages = data.slice(0, 8).map(m => {
                    const windRecord = m.wind_records?.[0];
                    const peakRecord = m.peak_records?.[0];

                    let message1 = '';
                    let message2 = '';

                    if (windRecord) {
                        message1 = windRecord.title || '';
                        message2 = windRecord.message || '';
                    } else if (peakRecord) {
                        message1 = `Hour: ${peakRecord.formatted_hour}`;
                        message2 = `Range: ${peakRecord.formatted_time_range}`;
                    }

                    return {
                        id: m.id || Date.now() + Math.random(),
                        title: m.title || 'Notification',
                        text: m.text || '',
                        level: m.level || 'info',
                        msg_type: m.msg_type || 'info',
                        message1: message1,
                        message2: message2,
                        wind_strength: m.wind_strength,
                        gust_strength: m.gust_strength,
                        wind_direction: m.wind_direction,
                        isPersistent: true,
                    };
                });
                // const dbMessages = data.slice(0, 8).map(m => ({
                //     id: m.id || Date.now() + Math.random(),
                //     title: m.payload?.title || 'Notification',
                //     text: m.payload?.message || '',
                //     level: m.payload?.level || 'info',
                //     msg_type: m.payload?.category || 'info',
                //     message1: m.payload?.max_wind_speed || '',
                //     message2: m.payload?.max_wind_gust || '',
                //     isPersistent: true,
                // }));

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