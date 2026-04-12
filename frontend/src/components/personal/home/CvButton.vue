<script setup lang="ts">

</script>

<template>
  <button type="button" class="btn-wrapper text-light d-flex flex-column text-start mt-lg-2">
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
  border-left: .3rem solid var(--p-light-2);
  color: var(--p-light-2);
  font-weight: 600;
  overflow: hidden;
  cursor: pointer;
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
}

.unit {
  font-weight: 300;
  font-style: italic;
}

</style>