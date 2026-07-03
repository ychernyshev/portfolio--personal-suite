// SPDX-License-Identifier: AGPL-3.0-or-later
import { defineStore } from 'pinia';
import { ref } from 'vue';
import backendApi from "@/services/backendApi.ts";

export const useUserAccountStore = defineStore('userAccount', () => {
  const currentUser = ref('');
  const error = ref('');
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

  return { currentUser, error, loading, fetchUserProfile };
});
