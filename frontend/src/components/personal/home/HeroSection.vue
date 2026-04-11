<script setup lang="ts">
import CvButton from "./CvButton.vue";
import TechIcons from "./TechIcons.vue";
</script>

<template>
  <div class="overflow-hidden mt-4">
    <div class="container-fluid col-xxl-8 hero-wrapper">
      <div class="row flex-lg-nowrap align-items-center g-5">
        <div class="order-lg-1 w-100 hero-image-block">
          <img style="clip-path: polygon(25% 0%, 100% 0%, 100% 99%, 0% 100%);" src="../../../assets/images/calc_dashboard.png" sizes="(max-width: 1080px) 100vw, 1080px" width="1160" height="568">
        </div>
        <div class="col-lg-6 col-xl-5 text-center text-lg-start pt-lg-5 mt-lg-4">
          <div class="lc-block mb-4 mb-lg-3">
            <div editable="rich">
              <h1 class="fw-bold display-3 hero-title ">
                <span class="hero-title-bg p-1">A full-stack realisation of your ideas</span>
              </h1>
            </div>
          </div>

          <div class="lc-block mb-4">
            <div editable="rich">
              <p class="rfs-8">
                <span class="hero-unit-bg hero-unit-text p-1">
                  using Django, Vue.js, Bootstrap, and other technologies
                </span>
              </p>
            </div>
          </div>

          <tech-icons />
        </div>
      </div>
      <div class="row">
        <div class="col-6 justify-content-center align-items-start">
          <cv-button/>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .hero-wrapper {
    transition: background-color 0.8s ease-in-out, all 0.8s ease;
  }

  .hero-technology {
    background: var(--p-dark-1);
  }

  .hero-image-block {
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .hero-title-bg,
  .hero-unit-bg {
    color: var(--p-light-2);
    transition: .8s;
  }

  .hero-unit-text {
    font-size: clamp(1.1rem, 1vh, 1.2rem);
    font-weight: 500;
  }

  .tech-centering {
    justify-content: center;
  }

  @media (min-width: 902px) {

  }

  @media (min-width: 992px) {
    .hero-title,
    .hero-unit-text {
      color: var(--p-light-2);
    }

    .hero-technology {
      background: var(--p-light-2);
    }

    .hero-title-bg,
    .hero-unit-bg {
      background: transparent;
    }

    .tech-centering {
      justify-content: start;
    }

    .w-lg-75 {
      width: 75%;
    }
  }
</style>