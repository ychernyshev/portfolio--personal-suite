// SPDX-License-Identifier: AGPL-3.0-or-later
import { defineStore } from 'pinia';
import { ref } from 'vue';
import backendApi from "@/services/backendApi.ts";

export const useUserAccountStore = defineStore('userAccount', () => {
  const currentUser = ref('');
  const currentLanguage = ref('');
  const message = ref({});
  const error = ref({});
  const loading = ref(false);

  const fetchUserProfile = async () => {
    loading.value = true;
    error.value = '';
    try {
      const response = await backendApi.get('/calculator/user-profile/');
      currentUser.value = response.data.username;
    } catch (err) {
      error.value = err.response?.data?.message || "You need to log in";
      throw err;
    } finally {
      loading.value = false;
    }
  };

  // ====================================================================
  // DEFAULT USER PROFILE LANGUAGE
  // ====================================================================
  const setUserLanguage = async (langValue) => {
    try {
      loading.value = true;

      const response = await backendApi.post('/calculator/user_language/', {
        language: langValue
      });
      currentLanguage.value = response.data.language;
      message.value = {text: 'Language saved successfully!', type: 'success'};
    } catch (err) {
      message.value = { text: 'Error saving default language.', type: 'danger' };
      console.error("Error saving language:", err);
    } finally {
      loading.value = false;
    }
  }

  const fetchUserLanguage = async () => {
    loading.value = true;
    try {
      const response = await backendApi.get('/calculator/user_language/');
      const data = response.data.results || response.data;

      if (data && (Array.isArray(data) ? data.length > 0 : true)) {
        const langData = Array.isArray(data) ? data[0] : data;

        currentLanguage.value = langData.language;
      } else {
        currentLanguage.value = 'en';
      }
    } catch (err) {
      console.error("Error fetching language:", err);
    } finally {
      loading.value = false;
    }
  }

  return {
    currentUser,
    error,
    loading,
    currentLanguage,
    fetchUserProfile,
    setUserLanguage,
    fetchUserLanguage,
  };
});
