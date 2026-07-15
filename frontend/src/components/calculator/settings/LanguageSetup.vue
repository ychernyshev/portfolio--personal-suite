<script setup>
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import {useUserAccountStore} from "../../../../store/useUserAccountStore.js";
  import {onMounted, ref, watch} from "vue";
  import {storeToRefs} from "pinia";

  const userLanguageStore = useUserAccountStore();
  const { currentLanguage } = storeToRefs(userLanguageStore);
  const languageValue = ref('');

  const languages = [
    {"abbr": "en", "name": "English"},
    {"abbr": "ua", "name": "Ukrainian"},
  ]

  userLanguageStore.fetchUserLanguage();

  const handleLanguageChange = async () => {
    await userLanguageStore.setUserLanguage(languageValue.value)
  }

  onMounted(async () => {
    await userLanguageStore.fetchUserLanguage();
  });

  watch(currentLanguage, (newVal) => {
    if (newVal) {
      languageValue.value = newVal;
    }
  }, { immediate: true });
</script>

<template>
  <div class="geolocation-wrapper mt-3 mb-3 text-start">
    <p class="mb-1 fw-medium text-purple">User interface language</p>
    <div class="col-12 pt-3 pb-3">
      <small class="text-muted">Set your preferred language interface</small>
      <div class="row neomorphic p-0 mt-2 d-flex align-items-center">
        <div class="col-12 col-lg-10">
          <form action="">
            <select v-model="languageValue" class="form-select bg-transparent border-0">
              <option value="" disabled>Select your language...</option>
              <option v-for="lang in languages"
                      :key="lang.abbr"
                      :value="lang.abbr">{{ lang.name }}</option>
            </select>
          </form>
        </div>
        <div class="col-12 col-lg-2 pl-lg-0 pr-lg-0">
          <button-comp @click=handleLanguageChange
                       type="button"
                       title="Set Language"
                       class="btn-blue-1 text-light w-100 h-100 border-radius-bottom-start-4 border-radius-bottom-end-4 border-radius-top-start-lg-0 border-radius-bottom-start-lg-0 border-radius-top-end-lg-4 rounded-md-4" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>