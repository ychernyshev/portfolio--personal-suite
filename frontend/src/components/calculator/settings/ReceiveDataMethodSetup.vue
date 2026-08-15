<script setup>
import { useUserAccountStore } from "../../../../store/useUserAccountStore";
import { storeToRefs } from "pinia";
import { onMounted, ref, watch } from "vue";
import ButtonComp from "@/components/personal/ButtonComp.vue";

const userReceiveDataMethodStore = useUserAccountStore();
const { receiveDataMethod } = storeToRefs(userReceiveDataMethodStore);

const dataMethodValue = ref('');
const method = [
  { "id": 1, "method": "manual" },
  { "id": 2, "method": "automatic" },
];

const handleReceiveDataMethod = async () => {
  await userReceiveDataMethodStore.setUserReceiveDataMethod(dataMethodValue.value);
};

onMounted(async () => {
  await userReceiveDataMethodStore.fetchUserReceiveDataMethod();
});

watch(receiveDataMethod, (newVal) => {
  if (newVal) {
    dataMethodValue.value = newVal;
  }
}, { immediate: true });
</script>

<template>
  <div class="geolocation-wrapper mt-3 mb-3 text-start">
    <p class="mb-1 fw-medium text-purple">Receive Data Method</p>
    <div class="col-12 pt-3 pb-3">
      <small class="text-muted">Set your receive data method: <strong>manual</strong> or <strong>automatic</strong></small>
      <div class="row neomorphic p-0 mt-2 d-flex align-items-center">
        <div class="col-12 col-lg-10">
          <form @submit.prevent>
            <select v-model="dataMethodValue" class="form-select bg-transparent border-0">
              <option value="" disabled>Select receive data method...</option>
              <option v-for="item in method"
                      :key="item.id"
                      :value="item.method">{{ item.method }}</option>
            </select>
          </form>
        </div>
        <div class="col-12 col-lg-2 pl-lg-0 pr-lg-0">
          <button-comp @click="handleReceiveDataMethod"
                       :disabled="!dataMethodValue"
                       type="button"
                       title="Set Receive Method"
                       class="btn-blue-1 text-light w-100 h-100 border-radius-bottom-start-4 border-radius-bottom-end-4 border-radius-top-start-lg-0 border-radius-bottom-start-lg-0 border-radius-top-end-lg-4 rounded-md-4" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>