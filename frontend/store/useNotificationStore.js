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
                const formattedMessages = [];

                data.forEach(m => {
                    // 1. Якщо є записи вітру — створюємо окрему картку для вітру
                    if (m.wind_records && m.wind_records.length > 0) {
                        const windRec = m.wind_records[0];

                        let adjustedTime = windRec.event_time || m.event_time;
                        if (adjustedTime) {
                            const parts = adjustedTime.split(':');
                            let hour = parseInt(parts[0], 10) - 1;
                            if (hour < 0) hour = 23;
                            parts[0] = String(hour).padStart(2, '0');
                            adjustedTime = parts.join(':');
                        }

                        formattedMessages.push({
                            id: `wind-${m.id}-${windRec.id || Math.random()}`,
                            type: 'wind',
                            title: 'Wind Forecast',
                            level: m.level || 'info',
                            event_time: adjustedTime,
                            wind_strength: windRec.wind_strength,
                            gust_strength: windRec.gust_strength,
                            wind_direction: windRec.wind_direction,
                            isPersistent: true,
                            created_at: m.created_at
                        });
                    }

                    // 2. Якщо є пікові години — створюємо окрему картку на КОЖНУ пікову годину
                    if (m.peak_records && m.peak_records.length > 0) {
                        m.peak_records.forEach(peak => {
                            formattedMessages.push({
                                id: `peak-${m.id}-${peak.peak_hour}`,
                                type: 'peak',
                                title: peak.status === 'PEAK_START' ? 'Solar Peak Start' : 'Solar Peak End',
                                level: 'success',
                                formatted_hour: peak.formatted_hour,
                                formatted_time_range: peak.formatted_time_range,
                                status: peak.status,
                                isPersistent: true,
                                created_at: m.created_at
                            });
                        });
                    }

                    // 3. Якщо ні вітру, ні піків немає — створюємо звичайну системну картку
                    if (!m.wind_records?.length && !m.peak_records?.length) {
                        formattedMessages.push({
                            id: `system-${m.id}`,
                            type: 'system',
                            title: m.title || 'System Notification',
                            text: m.text || m.payload?.message || '',
                            level: m.level ? m.level.toLowerCase() : 'info',
                            isPersistent: true,
                            created_at: m.created_at
                        });
                    }
                });

                // Обмежуємо загальну кількість до 8 карток
                messages.value = formattedMessages.slice(0, 8);
            }
        } catch (e) {
            console.error("Помилка завантаження повідомлень з бази даних", e);
        }
    };

    const initWebSocket = () => {
        const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
        const host = 'localhost:8001';

        socket = new WebSocket(`${protocol}${host}/ws/calculator/events/`);

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
        // Тут ви можете аналогічно обробляти вебсокет, якщо він шле складені об'єкти
        const newMessage = {
            id: eventData.id || Date.now(),
            type: eventData.type || 'system',
            title: eventData.title || 'System Notification',
            text: eventData.text || eventData.payload?.message || '',
            level: eventData.level ? eventData.level.toLowerCase() : 'info',
            isPersistent: eventData.is_persistent,
            created_at: eventData.created_at || new Date().toISOString()
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


// DEPRECATED
// import { defineStore } from 'pinia';
// import { ref } from 'vue';
// import backendApi from "@/services/backendApi.ts";
//
// export const useNotificationStore = defineStore('notifications', () => {
//     const messages = ref([]);
//     let socket = null;
//
//     const initMessages = async () => {
//         try {
//             const response = await backendApi.get('calculator/system_event/?limit=8');
//             const data = response.data.results || response.data;
//
//             if (Array.isArray(data)) {
//                 const dbMessages = data.slice(0, 8).map(m => {
//                     const peakRecord = m.peak_records?.[0];
//
//                     let adjustedTime = m.event_time;
//                     if (adjustedTime) {
//                         const parts = adjustedTime.split(':');
//                         let hour = parseInt(parts[0], 10) - 1;
//                         if (hour < 0) hour = 23;
//                         parts[0] = String(hour).padStart(2, '0');
//                         adjustedTime = parts.join(':');
//                     }
//
//                     const targetHourStr = adjustedTime ? adjustedTime.slice(0, 2) : '';
//                     const currentWindRecord = m.wind_records?.find(r => r.event_time?.includes(targetHourStr)) || m.wind_records?.[0];
//
//                     let message1 = '';
//                     let message2 = '';
//
//                     if (currentWindRecord) {
//                         message1 = currentWindRecord.title || '';
//                         message2 = currentWindRecord.message || '';
//                     } else if (peakRecord) {
//                         message1 = `Hour: ${peakRecord.formatted_hour}`;
//                         message2 = `Range: ${peakRecord.formatted_time_range}`;
//                     }
//
//                     return {
//                         id: m.id || Date.now() + Math.random(),
//                         title: m.title || 'Notification',
//                         text: m.text || '',
//                         level: m.level || 'info',
//                         msg_type: m.msg_type || 'info',
//                         message1: message1,
//                         message2: message2,
//                         event_time: adjustedTime,
//                         wind_strength: currentWindRecord?.wind_strength || m.wind_strength,
//                         gust_strength: currentWindRecord?.gust_strength || m.gust_strength,
//                         wind_direction: currentWindRecord?.wind_direction || m.wind_direction,
//                         peak_time_range: m.peak_time_range,
//                         isPersistent: true,
//                         created_at: m.created_at
//                     };
//                 });
//                 // const dbMessages = data.slice(0, 8).map(m => ({
//                 //     id: m.id || Date.now() + Math.random(),
//                 //     title: m.payload?.title || 'Notification',
//                 //     text: m.payload?.message || '',
//                 //     level: m.payload?.level || 'info',
//                 //     msg_type: m.payload?.category || 'info',
//                 //     message1: m.payload?.max_wind_speed || '',
//                 //     message2: m.payload?.max_wind_gust || '',
//                 //     isPersistent: true,
//                 // }));
//
//                 messages.value = dbMessages;
//             }
//         } catch (e) {
//             console.error("Помилка завантаження повідомлень з бази даних", e);
//         }
//     };
//
//     const initWebSocket = () => {
//         const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
//         const host = 'localhost:8001';
//
//         const socket = new WebSocket(`${protocol}${host}/ws/calculator/events/`);
//
//         socket.onopen = () => {
//             console.log("WS: Connected to Calculator events successfully.");
//         };
//
//         socket.onmessage = (event) => {
//             try {
//                 const data = JSON.parse(event.data);
//                 console.log("WS: New event received:", data);
//
//                 addNotification(data);
//             } catch (e) {
//                 console.error("WS: Failed to parse incoming message", e);
//             }
//         };
//
//         socket.onerror = (error) => {
//             console.error("WS: WebSocket error observed:", error);
//         };
//
//         socket.onclose = (event) => {
//             console.warn("WS: Connection lost. Trying to reconnect in 3s...", event.reason);
//             setTimeout(initWebSocket, 3000);
//         };
//     };
//
//     const addNotification = (eventData) => {
//         const newMessage = {
//             id: eventData.id || Date.now(),
//             title: eventData.title || 'System Notification',
//             text: eventData.payload?.message || eventData.title || '',
//             level: eventData.level ? eventData.level.toLowerCase() : 'info',
//             msg_type: eventData.category ? eventData.category.toLowerCase() : 'info',
//             isPersistent: eventData.is_persistent,
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
//     const disconnectWebSocket = () => {
//         if (socket) {
//             socket.close();
//             socket = null;
//         }
//     };
//
//     return {
//         messages,
//         initMessages,
//         addNotification,
//         removeNotification,
//         initWebSocket,
//         disconnectWebSocket
//     };
// });