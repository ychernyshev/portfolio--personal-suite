<script setup lang="ts">

</script>

<template>
  <h3 class="text-center text-light mt-4">Code & Vision </h3>
  <div id="carouselExampleControls" class="carousel carousel-wrapper slide mt-5" data-bs-ride="carousel">
    <div class="carousel-inner carousel-child">
      <div class="carousel-item active">
        <button type="button" class="btn btn-warning collapse-2">Live Preview</button>
        <button type="button" class="btn btn-light collapse-2">Source Code</button>
        <img src="../../assets/images/calc_dashboard.png" class="d-block w-50" alt="...">
      </div>
      <div class="carousel-item">
        <img src="..." class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="..." class="d-block w-100" alt="...">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<style scoped>
  .carousel-wrapper {
    position: relative;
  }

  .carousel-child {
    position: absolute;
    top: 0;
    left: 25%;
  }
</style>