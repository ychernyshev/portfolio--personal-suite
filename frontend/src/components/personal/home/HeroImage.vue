<script setup lang="ts">

import ButtonComp from "../ButtonComp.vue";
</script>

<template>
  <div class="order-lg-1 w-100 hero-image-block">
    <img
        class="hero-image"
        src="../../../assets/images/calc_dashboard.png"
        sizes="(max-width: 1080px) 100vw, 1080px"
        width="1160"
        height="568"
    >
    <div class="get-live-wrapper d-flex flex-column align-items-center">
      <p>Live dashboard preview — energy generation, weather, and tariff indicators.</p>
      <div class="d-flex flex-row justify-content-around align-items-center w-100">
        <button-comp title="Live Preview" class="btn-warning d-flex flex-row align-items-center">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
            <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>
          </svg>
         </button-comp>
        <button-comp title="Source Code" class="btn-light d-flex flex-row align-items-center">
          <template #left>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-code" viewBox="0 0 16 16">
              <path d="M5.854 4.854a.5.5 0 1 0-.708-.708l-3.5 3.5a.5.5 0 0 0 0 .708l3.5 3.5a.5.5 0 0 0 .708-.708L2.707 8zm4.292 0a.5.5 0 0 1 .708-.708l3.5 3.5a.5.5 0 0 1 0 .708l-3.5 3.5a.5.5 0 0 1-.708-.708L13.293 8z"/>
            </svg>
          </template>
          <template #right>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-code-slash" viewBox="0 0 16 16">
              <path d="M10.478 1.647a.5.5 0 1 0-.956-.294l-4 13a.5.5 0 0 0 .956.294zM4.854 4.146a.5.5 0 0 1 0 .708L1.707 8l3.147 3.146a.5.5 0 0 1-.708.708l-3.5-3.5a.5.5 0 0 1 0-.708l3.5-3.5a.5.5 0 0 1 .708 0m6.292 0a.5.5 0 0 0 0 .708L14.293 8l-3.147 3.146a.5.5 0 0 0 .708.708l3.5-3.5a.5.5 0 0 0 0-.708l-3.5-3.5a.5.5 0 0 0-.708 0"/>
            </svg>
          </template>
         </button-comp>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-image-block {
  position: relative;
  width: 100%;
  transition: all 2.5s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 6rem 4rem 3rem 1rem rgba(0, 0, 0, 0.4);
}

.hero-image {
  width: 98%;
  height: 98%;
  clip-path: polygon(25% 0%, 100% 0%, 100% 99%, 0% 100%);
  transition: .9s ease-in-out;
}

.get-live-wrapper {
  position: absolute;
  bottom: 35%;
  right: 40%;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 35%;
  height: 30%;
  padding: 25px;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  box-shadow: 0 0 6rem .6rem rgba(0, 0, 0, 0.1);
  color: var(--primary-emphasis);
  font-size: clamp(1.2rem, 1vw, 1.5rem);
  font-weight: 600;
  text-align: center;
  opacity: 0;
  transition: opacity 0.9s ease;
}

.hero-image-block:hover .get-live-wrapper {
  opacity: 1;
}

.hero-image-block:hover {
  box-shadow: 2rem 2rem 5rem 1rem rgba(0, 0, 0, 0.6);
  transition: 2.5s ;
}

.hero-image-block:hover .hero-image {
  transform: scale(1.03);
  clip-path: polygon(0% 0%, 100% 0%, 100% 99%, 0% 100%);
  transition: .9s ease-in-out;
}

.btn-transform {
  transition: .3s ease-in-out;
}

.btn-transform:hover {
  transform: scale(1.05);
  transition: .3s ease-in-out;
}
</style>
