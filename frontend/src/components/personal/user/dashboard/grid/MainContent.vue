<script setup lang="ts">
  import Toast from "@/components/personal/user/dashboard/Toast.vue";

  const currentYear = new Date().getFullYear();
</script>

<template>
  <main class="main-content position-relative max-height-vh-100 h-100 border-radius-lg ">
    <!-- Navbar -->
    <nav class="navbar navbar-main navbar-expand-lg px-0 mx-4 border-radius-xl shadow-none" id="navbarBlur" navbar-scroll="true">
      <div class="container-fluid py-1 px-3">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
            <li class="breadcrumb-item text-sm"><a class="opacity-5 text-dark" href="javascript:;">Pages</a></li>
            <li class="breadcrumb-item text-sm text-dark active" aria-current="page">Dashboard</li>
          </ol>
          <h6 class="font-weight-bolder mb-0">Dashboard</h6>
        </nav>
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
      </div>
    </nav>
    <!-- End Navbar -->
    <div class="container-fluid py-1">
      <div class="row">
        <div class="col-lg-12">
          <div class="card z-index-2">
            <div class="card-body p-3">
              <slot />
            </div>
          </div>
        </div>
      </div>
<!--      <footer class="footer pt-3  ">-->
<!--        <div class="container-fluid">-->
<!--          <div class="row align-items-center justify-content-lg-between">-->
<!--            <div class="col-lg-6 mb-lg-0 mb-4">-->
<!--              <div class="copyright text-center text-sm text-muted text-lg-start">-->
<!--                © {{ currentYear }},-->
<!--                <a href="https://www.creative-tim.com" class="font-weight-bold" target="_blank">Personal Dev Showcase</a>-->
<!--                2.3.2-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--      </footer>-->
    </div>
  </main>
</template>

<style scoped>
  .main-content {
    height: 100vh;
    flex-direction: column;
  }

  .card-body {
    height: auto;
    overflow-y: hidden;
  }

  @media (min-width: 1200px) {
    .card-body {
      height: 80vh;
    }
  }
</style>