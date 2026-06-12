<script setup lang="ts">
  import Toast from "@/components/personal/user/dashboard/Toast.vue";
  import DashboardHeader from "@/components/personal/user/dashboard/grid/dashboardHeader.vue";
</script>

<template>
  <div class="collapse navbar-collapse mt-sm-0 mt-2 me-md-0 me-sm-4" id="navbar">
    <div class="ms-md-auto pe-md-3 d-flex align-items-center">
      <div class="ms-md-auto">
        <toast />
      </div>
      <div class="input-group">
              <span class="input-group-text text-body">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                  <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
                </svg>
              </span>
        <input type="text" class="form-control" placeholder="Type here...">
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