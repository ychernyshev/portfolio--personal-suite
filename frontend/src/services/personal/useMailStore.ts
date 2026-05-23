// src/stores/messageStore.ts
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import backendApi from "@/services/backendApi";

export const useMailStore = defineStore('messages', () => {
    const messages = ref<any[]>([]);
    const isLoading = ref(false);

    const unreadCount = computed(() => {
        return messages.value.filter(msg => !msg.is_read).length;
    });

    const fetchMessages = async () => {
        isLoading.value = true;
        try {
            const response = await backendApi.get('/personal/user/admin/mail/inbound');
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

    const updateMessageStatus = (id: number, isReadStatus: boolean) => {
        const msg = messages.value.find(m => m.id === id);
        if (msg) {
            msg.is_read = isReadStatus;
        }
    };

    const initWebSocket = () => {
        const socket = new WebSocket('ws://localhost:8001/ws/inbox/');

        // const websocket_host:string = import.meta.env.VITE_WEBSOCKET_URL;
        // const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
        // const socket = new WebSocket(`${protocol}${websocket_host}/ws/inbox/`);

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

    return {
        messages,
        isLoading,
        unreadCount,
        fetchMessages,
        addMessage,
        updateMessageStatus,
        initWebSocket
    };
});