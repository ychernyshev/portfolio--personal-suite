<script setup>
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import {useUserAccountStore} from "../../../../store/useUserAccountStore.js";
  import {onMounted, ref, watch} from "vue";
  import {storeToRefs} from "pinia";

  const userCurrencyStore = useUserAccountStore();
  const { currentCurrency } = storeToRefs(userCurrencyStore);
  const currencyValue = ref('');

  const currency = [
    {"abbr": "UAH", "symbol": "₴"},
    {"abbr": "EUR", "symbol": "€"},
    {"abbr": "USD", "symbol": "$"},
  ]

  const handleCurrencyChange = async () => {
    await userCurrencyStore.setUserCurrency(currencyValue.value)
  }

  onMounted(async () => {
    await userCurrencyStore.fetchUserCurrency();
  });

  watch(currentCurrency, (newVal) => {
    if (newVal && newVal !== '') {
      currencyValue.value = newVal;
    }
  }, { immediate: true })
</script>

<template>
  <div class="geolocation-wrapper mt-3 mb-3 text-start">
    <p class="mb-1 fw-medium text-purple">Set a default currency</p>
    <div class="col-12 pt-3 pb-3">
      <small class="text-muted">Choose your currency</small>
      <div class="row neomorphic p-0 mt-2 d-flex align-items-center">
        <div class="col-12 col-lg-10">
          <form action="">
            <select v-model="currencyValue" class="form-select bg-transparent border-0">
              <option value="" disabled>Select your local currency...</option>
              <option v-for="cur in currency"
                      :key="cur.abbr"
                      :value="cur.abbr">{{ cur.symbol }}</option>
            </select>
          </form>
        </div>
        <div class="col-12 col-lg-2 pl-lg-0 pr-lg-0">
          <button-comp @click=handleCurrencyChange
                       :disabled="!currentCurrency"
                       type="button"
                       title="Set Currency"
                       class="btn-blue-1 text-light w-100 h-100 border-radius-bottom-start-4 border-radius-bottom-end-4 border-radius-top-start-lg-0 border-radius-bottom-start-lg-0 border-radius-top-end-lg-4 rounded-md-4" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>