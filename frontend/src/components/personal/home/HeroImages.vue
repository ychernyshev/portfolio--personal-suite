<script setup lang="ts">

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
      <div class="d-flex flex-row align-items-center">
        <button class="btn btn-warning">Live Preview</button>
        <button class="btn btn-light">Source Code</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-image-block {
  position: relative;
  width: 100%;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.hero-image {
  width: 98%;
  height: 98%;
  clip-path: polygon(25% 0%, 100% 0%, 100% 99%, 0% 100%);
  transition: .9s ease-in-out;
}

.get-live-wrapper {
  position: absolute;
  bottom: 1%;
  right: 20%;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 35%;
  height: 20%;
  background-color: rgba(255, 255, 255, 0.5);
  color: var(--p-dark-1);
  font-size: clamp(1.2rem, 1vw, 1.5rem);
  text-align: center;
  opacity: 0;
  transition: opacity 0.9s ease;
}

.hero-image-block:hover .get-live-wrapper {
  opacity: 1;
}

.hero-image-block:hover .hero-image {
  width: 102%;
  height: 102%;
  clip-path: polygon(0% 0%, 100% 0%, 100% 99%, 0% 100%);
  transition: .9s ease-in-out;
}
</style>
