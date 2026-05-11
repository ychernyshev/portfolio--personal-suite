// src/stores/messageStore.ts
import { defineStore } from 'pinia';
import { ref } from 'vue';
import backendApi from "@/services/backendApi";

export const useMessageStore = defineStore('messages', () => {
    const messages = ref<any[]>([]);
    const isLoading = ref(false);

    const fetchMessages = async () => {
        isLoading.value = true;
        try {
            const response = await backendApi.get('/personal/inbound-messages');
            messages.value = response.data.results || response.data;
        } catch (error) {
            console.error("Failed to fetch messages:", error);
        } finally {
            isLoading.value = false;
        }
    };

    const addMessage = (newMessage: any) => {
        messages.value.unshift(newMessage);
    };

    const initWebSocket = () => {
        const socket = new WebSocket('ws://localhost:8001/ws/inbox/');

        socket.onmessage = (event) => {
            const newMessage = JSON.parse(event.data);
            console.log("WS: New message received!", newMessage);
            addMessage(newMessage);
        };

        socket.onclose = () => {
            console.warn("WS: Connection lost. Trying to reconnect...");
            setTimeout(initWebSocket, 3000);
        };
    };

    return { messages, isLoading, fetchMessages, addMessage, initWebSocket };
});