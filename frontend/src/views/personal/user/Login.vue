<script setup lang="ts">
  import { ref, reactive } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import backendApi from "@/services/backendApi.ts";
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import {useMailStore} from "@/services/personal/useMailStore.js";

  const messageStore = useMailStore();

  const route = useRoute();
  const router = useRouter();

  const credentials = reactive({
    username: '',
    password: ''
  });

  const errorMessage = ref('');

  const submitLogin = async () => {
    try {
      errorMessage.value = '';

      const response = await backendApi.post('/auth/jwt/create/', {
        username: credentials.username,
        password: credentials.password
      });

      const token = response.data.access;
      const refresh = response.data.refresh;

      localStorage.setItem('access_token', token);
      localStorage.setItem('refresh_token', refresh);

      backendApi.defaults.headers.common['Authorization'] = `Bearer ${token}`;

      messageStore.initWebSocket();

      const redirectPath = route.query.next as string || 'user/dashboard/emails/inbound';
      await router.push(redirectPath);
    } catch (err: any) {
      errorMessage.value = "You have entered an incorrect username or password";
    }
  };
</script>

<template>
  <div class="row justify-content-center align-items-center" style="height: 60vh">
    <div class="col-12 col-md-4 col-lg-3">
      <h3 class="text-light mb-4 text-center">Sentinel Access</h3>

      <form @submit.prevent="submitLogin" class="d-flex flex-column">
        <label for="username" class="text-light small mb-1">Username</label>
        <input
            v-model="credentials.username"
            class="form-control bg-dark text-light border-secondary"
            id="username"
            type="text"
            required
        />

        <label for="password" class="text-light small mt-3 mb-1">Password</label>
        <input
            v-model="credentials.password"
            class="form-control bg-dark text-light border-secondary"
            id="password"
            type="password"
            required
        />

        <p v-if="errorMessage" class="text-danger small mt-2 mb-0">{{ errorMessage }}</p>

        <button-comp
            type="submit"
            title="Sign In"
            class="btn-warning mt-4 w-100"
        ></button-comp>
      </form>
    </div>
  </div>
</template>

<style scoped>

</style>