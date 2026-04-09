<script setup lang="ts">

</script>

<template>
  <nav class="navbar navbar-expand-lg bg-light p-0 m-0">
    <div class="container-fluid">
      <a class="navbar-brand d-flex flex-column d-lg-none m-0 p-0" href="#">
        <div class="col-12">
          <h4>Yevhenii Chernyshev</h4>
        </div>
        <div class="col-12">
          <router-link to="/introducing" class="small text-light bg-success p-2 w-100">Personal Programmer</router-link>
        </div>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 mx-lg-auto w-100 d-lg-flex justify-content-around align-items-lg-center">
          <li class="nav-item">
            <router-link to="/introducing" class="nav-link active" aria-current="page">
              Introducing
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/cv" class="nav-link">CV</router-link>
          </li>
          <div class="navbar-brand row d-none d-lg-block p-0 m-0">
            <div class="col-12">
              <h3>Yevhenii Chernyshev</h3>
            </div>
            <div class="col-12 small text-white text-center">
              <span class="bg-success p-2 nav-unit-text">Personal Programmer</span>
            </div>
          </div>
          <li class="nav-item">
            <router-link to="/projects" class="nav-link">Projects</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/contacts" class="nav-link">Contacts</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

  <style scoped>
    .nav-unit-text {
      font-size: clamp(1rem, 1.7vw, 1.4rem);
    }
  </style>

<style scoped>
</style>