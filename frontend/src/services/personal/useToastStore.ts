// stores/toast.ts
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useToastStore = defineStore('toast', () => {
    const isVisible = ref(false);
    const message = ref('');
    const type = ref<'success' | 'danger'>('success');

    function show(msg: string, toastType: 'success' | 'danger' = 'success') {
        message.value = msg;
        type.value = toastType;
        isVisible.value = true;
        setTimeout(() => {
            isVisible.value = false;
        }, 3000);
    }

    return { isVisible, message, type, show };
});