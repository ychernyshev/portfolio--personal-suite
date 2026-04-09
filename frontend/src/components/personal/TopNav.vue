<script setup lang="ts">

</script>

<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <a class="navbar-brand d-flex flex-column d-lg-none" href="#">
        Yevhenii Chernyshev
        <span class="small text-muted">Personal Programmer</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 mx-lg-auto w-100 d-lg-flex justify-content-around">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">
              Introducing
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">CV</a>
          </li>
          <div class="navbar-brand row d-none d-lg-block">
            <div class="col-12">Yevhenii Chernyshev</div>
            <div class="col-12 small text-muted text-center">Personal Programmer</div>
          </div>
          <li class="nav-item">
            <a class="nav-link">Examples</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">Contacts</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

  <style scoped>
    /* Твій кастомний стиль, який ТОЧНО спрацює */
    .hero-bg {
      min-height: 80vh;
      background-color: #111827; /* Темний колір як у Tailwind */
      background-image: radial-gradient(circle at center, #1f2937 0%, #111827 100%);
    }

    .btn-primary {
      background-color: #3b82f6;
      border-color: #3b82f6;
    }

    .btn-primary:hover {
      background-color: #2563eb;
    }
  </style>

<style scoped>
</style>