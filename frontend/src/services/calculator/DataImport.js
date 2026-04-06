import {ref} from "vue";
import backendApi from "./backendApi.js";
import {useNotificationStore} from "../../../store/useNotificationStore.js";

const notificationStore = useNotificationStore();

const importFile = ref(null);

export const handleFileChange = (event) => {
    importFile.value = event.target.files[0];
};

export const importData = async () => {
    if (!importFile.value) {
        notificationStore.addNotification({ title: 'Error', text: 'Choose the file', level: 'warning' });
        return;
    }

    const formData = new FormData();
    formData.append('file', importFile.value);

    try {
        await backendApi.post('entries/import-csv/', formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
        });

        notificationStore.addNotification({
            title: 'Успіх',
            text: 'Дані імпортовано',
            level: 'success'
        });

        await fetchEntries();
    } catch (error) {
        console.error(error);
        notificationStore.addNotification({ title: 'Import error', level: 'danger' });
    }
};