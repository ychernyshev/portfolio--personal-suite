// SPDX-License-Identifier: AGPL-3.0-or-later
import { defineStore } from 'pinia';
import {computed, ref} from 'vue';
import backendApi from "@/services/backendApi.ts";
import {useUserProfileSettingsStore} from "./useUserProfileSettingsStore.js";

export const useUserAccountStore = defineStore('userAccount', () => {
  const currentUser = ref('');
  const currentLanguage = ref('');
  const currentCurrency = ref('');
  const receiveDataMethod = ref('');
  const isAutomaticActive = ref(false);
  const voucherInput = ref('');
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
  // LANGUAGE
  // ====================================================================
  const setUserLanguage = async (langValue) => {
    try {
      loading.value = true;

      const response = await backendApi.patch('/calculator/user_settings/', {
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
      const response = await backendApi.get('/calculator/user_settings/');
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

  // ====================================================================
  // CURRENCY
  // ====================================================================
  const setUserCurrency = async (currValue) => {
    try {
      loading.value = true;

      const response = await backendApi.patch('/calculator/user_settings/', {
        currency: currValue
      });
      currentCurrency.value = response.data.currency;
      message.value = {text: 'Currency saved successfully!', type: 'success'};
    } catch (err) {
      message.value = { text: 'Error saving default currency.', type: 'danger' };
      console.error("Error saving currency:", err);
    } finally {
      loading.value = false;
    }
  }

  const fetchUserCurrency = async () => {
    loading.value = true;

    try {
      const response = await backendApi.get('/calculator/user_settings/');
      const data = response.data.results || response.data;

      if (data && (Array.isArray(data) ? data.length > 0 : true)) {
        const currencyData = Array.isArray(data) ? data[0] : data;

        currentCurrency.value = currencyData.currency;
      } else {
        currentCurrency.value = "UAH";
      }
    } catch (err) {
      console.error("Error fetching currency:", err);
    } finally {
      loading.value = false;
    }
  }

  // ====================================================================
  // RECEIVE DATA METHOD
  // ====================================================================
  const setUserReceiveDataMethod = async (currValue, authCode = '') => {
    try {
      loading.value = true;

      const response = await backendApi.patch('/calculator/user_settings/', {
        receive_data_method: currValue,
        authorization_code: authCode
      });

      receiveDataMethod.value = response.data.receive_data_method;
      isAutomaticActive.value = response.data.is_automatic_active || false;

      message.value = { text: 'Settings saved successfully!', type: 'success' };
      return true;
    } catch (err) {
      // Here the backend may return an error of type: "Invalid authorization code"
      const errorMsg = err.response?.data?.authorization_code?.[0] || 'Error saving receive data method.';
      message.value = { text: errorMsg, type: 'danger' };
      console.error("Error saving receive data method:", err);
      return false;
    } finally {
      loading.value = false;
    }
  }

  const fetchUserReceiveDataMethod = async () => {
    loading.value = true;

    try {
      const response = await backendApi.get('/calculator/user_settings/');
      const data = response.data.results || response.data;

      if (data && (Array.isArray(data) ? data.length > 0 : true)) {
        const methodData = Array.isArray(data) ? data[0] : data;

        receiveDataMethod.value = methodData.receive_data_method;
      } else {
        receiveDataMethod.value = 'manual';
      }
    } catch (err) {
      console.error("Error fetching receive data method:", err);
    } finally {
      loading.value = false;
    }
  }

  return {
    currentUser,
    error,
    loading,
    currentLanguage,
    currentCurrency,
    receiveDataMethod,
    fetchUserProfile,
    setUserLanguage,
    fetchUserLanguage,
    setUserCurrency,
    fetchUserCurrency,
    setUserReceiveDataMethod,
    fetchUserReceiveDataMethod,
  };
});
