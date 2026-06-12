<script setup lang="ts">
  import Toast from "@/components/personal/user/dashboard/Toast.vue";
</script>

<template>
  <div class="collapse navbar-collapse mt-sm-0 mt-2 me-md-0 me-sm-4" id="navbar">
    <div class="ms-md-auto pe-md-3 d-flex align-items-center">
      <div class="ms-md-auto">
        <toast />
      </div>
    </div>
  </div>
  <div class="container-fluid py-2 main-content">
    <div class="row mt-4">
      <div class="col-12">
        <div class="card">
          <div class="card-header pb-4 rounded-5">
            <slot />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .main-content {
    flex-direction: column;
    overflow-y: hidden;
  }

  @media (min-width: 1200px) {}
</style>