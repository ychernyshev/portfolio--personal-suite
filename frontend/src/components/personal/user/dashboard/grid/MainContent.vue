<script setup lang="ts">
  import Toast from "@/components/personal/user/dashboard/Toast.vue";
  import DashboardHeader from "@/components/personal/user/dashboard/grid/dashboardHeader.vue";

  const currentYear = new Date().getFullYear();
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
    <footer class="footer pt-3">
      <div class="container-fluid">
        <div class="row align-items-center justify-content-lg-between">
          <div class="col-lg-6 mb-lg-0 mb-4">
            <div class="copyright text-start text-sm text-muted text-lg-left">
              © {{ currentYear }}, the <span class="text-info">personal dev showcase</span> by
              <router-link to="/">
                <b>Yevgenii Chernyshev</b>
              </router-link>
            </div>
          </div>
          <div class="col-lg-6">
            <ul class="nav nav-footer justify-content-center justify-content-lg-end">
              <li class="nav-item">
                <router-link to="/" class="nav-link text-muted">YChernyshev</router-link>
              </li>
              <li class="nav-item">
                <a href="https://www.creative-tim.com/presentation" class="nav-link text-muted" target="_blank">About</a>
              </li>
              <li class="nav-item">
                <a href="http://blog.creative-tim.com" class="nav-link text-muted" target="_blank">Blog</a>
              </li>
              <li class="nav-item">
                <a href="https://www.creative-tim.com/license" class="nav-link pe-0 text-muted" target="_blank">License</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
  .main-content {
    flex-direction: column;
    overflow-y: hidden;
  }

  @media (min-width: 1200px) {}
</style>