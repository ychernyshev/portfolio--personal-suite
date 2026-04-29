<script setup lang="ts">
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import {useContactForm} from "@/services/personal/useContactForm";

  const { formData, isSuccess, fieldsNotFilled, submitForm } = useContactForm();
</script>

<template>
<div class="collapse bg-transparent" id="collapsedForm">
  <div class="card card-body bg-transparent border-0">
    <form action="" @submit.prevent="submitForm" class="row justify-content-end">
      <div class="col-12 col-lg-4">
        <input v-model="formData.subject" class="form-control mb-1 bg-glass rounded-2 right-angle-bottom-start right-angle-bottom-end" autofocus type="text" placeholder="Subject">
      </div>
      <div class="col-12 col-lg-4">
        <input v-model="formData.email" class="form-control mb-1 bg-glass rounded-2 right-angle-bottom-start right-angle-bottom-end" type="email" placeholder="Email">
      </div>
      <div class="col-12 col-lg-4">
        <input v-model="formData.theme" class="form-control mb-1 bg-glass right-angle-bottom-start right-angle-bottom-end" type="text" placeholder="Project theme">
      </div>
      <div class="col-12">
        <textarea v-model="formData.message" class="form-control bg-glass border-0 right-angle-bottom-start right-angle-bottom-end rounded-lg-0" name="" placeholder="Tell me about your idea" id="" cols="30" rows="5"></textarea>
      </div>
      <div class="col-12 col-lg-4">
        <button type="submit" class="btn btn-success shadow w-100 rounded-2 right-angle-top-start right-angle-top-end">Let`s get discussion</button>
      </div>
    </form>
  </div>
</div>
</template>

<style scoped>
  .bg-glass {
    background: rgba(255, 255, 255, 0.8);
  }

  @media (min-width: 992px) {
    .rounded-lg-0 {
      border-radius: 0;
    }
  }
</style>