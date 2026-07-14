<script setup>
import ButtonComp from "@/components/personal/ButtonComp.vue";

const currency = [
  {"abbr": "uah", "symbol": "₴"},
  {"abbr": "eur", "symbol": "€"},
  {"abbr": "dol", "symbol": "$"},
]

const setCurrency = async () => {
  console.log("Currency has been set up");
}
</script>

<template>
  <div class="geolocation-wrapper mt-3 mb-3 text-start">
    <p class="mb-1 fw-medium text-purple">Set a default currency</p>
    <div class="col-12 pt-3 pb-3">
      <small class="text-muted">Choose your currency</small>
      <div class="row neomorphic p-0 mt-2 d-flex align-items-center">
        <div class="col-12 col-lg-10">
          <form action="">
            <select class="form-select bg-transparent border-0">
              <option v-for="cur in currency"
                      :key="cur.abbr"
                      :value="cur.symbol">{{ cur.symbol }}</option>
            </select>
          </form>
        </div>
        <div class="col-12 col-lg-2 pl-lg-0 pr-lg-0">
          <button-comp @click=setCurrency
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