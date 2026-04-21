<script setup lang="ts">

</script>

<template>
  <button type="button" class="btn-wrapper mx-auto text-light d-flex flex-column text-start mt-lg-2 mb-5" data-bs-toggle="modal" data-bs-target="#exampleModal">
      <span class="title">Career Overview</span>
    <span class="unit">For corporate job interviewers and relocation opportunities</span>
  </button>
</template>

<style scoped>
.btn-wrapper {
  position: relative;
  padding: 12px 30px;
  background-color: rgba(30, 35, 66, 1);
  backdrop-filter: blur(10px);
  border: none;
  box-shadow: 0 0 .6rem .15rem rgba(0, 0, 0, 0.2);
  border-left: .3rem solid var(--p-light-2);
  color: var(--p-light-2);
  font-weight: 600;
  overflow: hidden;
  cursor: pointer;
  transition: .8s;
}

.btn-wrapper::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(255, 255, 255, 0.1);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s ease;
  z-index: -1;
}

.btn-wrapper:hover::before {
  transform: scaleX(1);
  color: var(--p-dark-2);
}

.btn-wrapper:hover svg {
  background-color: var(--p-light-2);
  transition: 0.82s;
  color: var(--p-dark-2);
}

.title {
  font-size: clamp(1.2rem, 1vw, 1rem);
  font-weight: bold;
  color: var(--primary-emphasis-2);
  transition: .8s;
}

.unit {
  font-weight: 300;
  transition: .8s;
}
</style>