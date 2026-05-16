<script setup lang="ts">
  import ButtonComp from "@/components/personal/ButtonComp.vue";

  const props = defineProps<{
    subject_email: string;
    project_theme: string;
    mail_body: string;
  }>()
</script>

<template>
  <p>
    <a class="btn btn-success rounded-2" data-bs-toggle="collapse" href="#mailReplyBox" role="button" aria-expanded="false" aria-controls="collapseExample">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-90deg-left" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M1.146 4.854a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 4H12.5A2.5 2.5 0 0 1 15 6.5v8a.5.5 0 0 1-1 0v-8A1.5 1.5 0 0 0 12.5 5H2.707l3.147 3.146a.5.5 0 1 1-.708.708z"/>
      </svg>
    </a>
  </p>
  <div class="collapse" id="mailReplyBox">
    <div class="card card-body text-start">
      <form action="">
        <input type="text" class="form-control rounded-2" :value="props.subject_email">
        <input type="text" class="form-control rounded-2" placeholder="Copy...">
        <input type="text" :value="props.project_theme" class="form-control rounded-2">
        <textarea rows="5" cols="5" class="form-control form-control-sm border-0" />
        <button-comp title="Reply" class="btn btn-outline-success"></button-comp>
      </form>
    </div>
  </div>
</template>

<style scoped>

</style>