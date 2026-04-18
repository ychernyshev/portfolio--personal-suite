<script setup lang="ts">
import CvButton from "@/components/personal/home/CvButton.vue";
import TechIconsLib from "@/components/personal/TechIconsLib.vue";
import HeroImage from "@/components/personal/home/HeroImage.vue";
import CareerOverview from "@/components/personal/codeAndVision/CareerOverview.vue";

const techStack: string[] = ['python', 'django', 'drf', 'vue', 'pinia', 'ts', 'bootstrap', 'celery', 'redis', 'docker'];

</script>

<template>
  <div class="overflow-hidden mt-4">
    <div class="container-fluid col-xxl-8 hero-wrapper">
      <div class="row flex-lg-nowrap align-items-center g-5">
        <hero-image />
        <div class="col-lg-6 col-xl-5 text-center text-lg-start pt-lg-5 mt-lg-5 left-content">
          <div class="lc-block mb-3 mb-lg-3">
            <div editable="rich">
              <h1 class="fw-bold display-3 hero-title ">
                <span class="hero-title-bg p-1">A full-stack realisation of your ideas</span>
              </h1>
            </div>
          </div>

          <div class="lc-block">
            <div editable="rich">
              <p class="rfs-8">
                <span class="hero-unit-bg hero-unit-text p-1">
                  using Django, Vue.js, Bootstrap, and other technologies
                </span>
              </p>
            </div>
          </div>

          <div class="tech-icon-wrapper">
            <tech-icons-lib v-for="tech in techStack" :key="tech" :techName="tech" class="mt-3 col-3 col-lg-2"/>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12 justify-content-center align-items-start mt-3">
          <cv-button/>
          <career-overview />
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

  .hero-title-bg,
  .hero-unit-bg {
    color: var(--p-light-2);
    transition: .8s;
  }

  .hero-unit-text {
    font-size: clamp(1.1rem, 1vh, 1.2rem);
    font-weight: 500;
  }

  .left-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .tech-icon-wrapper {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    width: 80%;
  }

  @media (min-width: 768px) {
    .left-content {
      align-items: start;
    }

    .tech-icon-wrapper {
      width: 80%;
    }
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

    .w-lg-75 {
      width: 75%;
    }
  }
</style>