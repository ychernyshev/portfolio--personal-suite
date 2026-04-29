// src/composables/useContactForm.ts
import { ref, reactive } from 'vue';
import backendApi from "@/services/backendApi";

export function useContactForm() {
    const isSuccess = ref(false);
    const fieldsNotFilled = ref(false);

    const formData = reactive({
        subject: '',
        email: '',
        theme: '',
        message: ''
    });

    const submitForm = async () => {
        if (!formData.email || !formData.message) {
            fieldsNotFilled.value = true;
            setTimeout(() => { fieldsNotFilled.value = false; }, 4000);
            return;
        }

        try {
            const response = await backendApi.post('personal/contact/', {
                name: formData.subject,
                email: formData.email,
                theme: formData.theme,
                message: formData.message
            });

            if (response.data.status === 'success') {
                isSuccess.value = true;
                // Очищення форми
                formData.subject = '';
                formData.email = '';
                formData.theme = '';
                formData.message = '';

                setTimeout(() => { isSuccess.value = false; }, 6000);
            }
        } catch (error) {
            console.error("Sending error:", error);
        }
    };

    return {
        formData,
        isSuccess,
        fieldsNotFilled,
        submitForm
    };
}