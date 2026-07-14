<script setup>
  import ButtonComp from "@/components/personal/ButtonComp.vue";

  const languages = [
    {"abbr": "en", "name": "English"},
    {"abbr": "ua", "name": "Ukrainian"},
  ]

  const setLanguage = async () => {
    console.log("language has been set up");
  }
</script>

<template>
  <div class="geolocation-wrapper mt-3 mb-3 text-start">
    <p class="mb-1 fw-medium text-purple">User interface language</p>
    <div class="col-12 pt-3 pb-3">
      <small class="text-muted">Set your preferred language interface</small>
      <div class="row neomorphic p-0 mt-2 d-flex align-items-center">
        <div class="col-12 col-lg-10">
          <form action="">
            <select class="form-select bg-transparent border-0">
              <option v-for="lang in languages"
                      :key="lang.abbr"
                      :value="lang.name">{{ lang.name }}</option>
            </select>
          </form>
        </div>
        <div class="col-12 col-lg-2 pl-lg-0 pr-lg-0">
          <button-comp @click=handleSave
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