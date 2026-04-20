<script setup lang="ts">
import { computed } from "vue";
import { useRouter } from "vue-router";

import ButtonComp from "../ButtonComp.vue";

const router = useRouter();

const canUseRouter = computed(() => {
  return router.getRoutes().some((route) => route.path === "/calculator");
});
</script>

<template>
  <div class="order-lg-1 w-100 hero-image-block">
    <img
      class="hero-image"
      src="@/assets/images/solar_power_calculator/calc_dashboard.png"
      sizes="(max-width: 1080px) 100vw, 1080px"
      width="1160"
      height="568"
    />
    <div class="get-live-wrapper d-flex flex-column align-items-center">
      <p class="get-live-title">
        Live dashboard preview — energy generation, weather, and tariff
        indicators.
      </p>
      <div
        class="d-flex flex-row justify-content-around align-items-center w-100"
      >
        <button-comp
            to="/calculator"
            class="btn-warning text-primary-emphasis d-flex flex-row align-items-center get-live-button"
            title="Live preview"
        >
          <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-play-fill"
              viewBox="0 0 16 16"
          >
            <path
                d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"
            />
          </svg>
        </button-comp>
        <button-comp
            href="https://github.com/ychernyshev/portfolio--personal-suite/tree/main"
            class="btn-light text-primary-emphasis d-flex flex-row align-items-center get-live-button"
            title="Source Code"
        >
          <template #left>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-code"
              viewBox="0 0 16 16"
            >
              <path
                d="M5.854 4.854a.5.5 0 1 0-.708-.708l-3.5 3.5a.5.5 0 0 0 0 .708l3.5 3.5a.5.5 0 0 0 .708-.708L2.707 8zm4.292 0a.5.5 0 0 1 .708-.708l3.5 3.5a.5.5 0 0 1 0 .708l-3.5 3.5a.5.5 0 0 1-.708-.708L13.293 8z"
              />
            </svg>
          </template>
          <template #right>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-code-slash"
              viewBox="0 0 16 16"
            >
              <path
                d="M10.478 1.647a.5.5 0 1 0-.956-.294l-4 13a.5.5 0 0 0 .956.294zM4.854 4.146a.5.5 0 0 1 0 .708L1.707 8l3.147 3.146a.5.5 0 0 1-.708.708l-3.5-3.5a.5.5 0 0 1 0-.708l3.5-3.5a.5.5 0 0 1 .708 0m6.292 0a.5.5 0 0 0 0 .708L14.293 8l-3.147 3.146a.5.5 0 0 0 .708.708l3.5-3.5a.5.5 0 0 0 0-.708l-3.5-3.5a.5.5 0 0 0-.708 0"
              />
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
  box-shadow: 0 0 5rem 0.1rem rgba(0, 0, 0, 0.1);
}

.hero-image {
  width: 98%;
  height: 98%;
  clip-path: polygon(25% 0%, 100% 0%, 100% 99%, 0% 100%);
  transition: 0.9s ease-in-out;
}

.hero-image-block:hover .get-live-wrapper {
  opacity: 1;
}

.hero-image-block:hover {
  box-shadow: 0 0 5rem 0.1rem rgba(0, 0, 0, 0.1);
  transition: 2.5s;
}

.hero-image-block:hover .hero-image {
  transform: scale(1.03);
  clip-path: polygon(0% 0%, 100% 0%, 100% 99%, 0% 100%);
  transition: 0.9s ease-in-out;
}

.get-live-wrapper {
  position: absolute;
  bottom: 14%;
  right: 13%;
  width: 75%;
  height: 71%;
  padding: 10px 0;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  box-shadow: 0 0 6rem 0.6rem rgba(0, 0, 0, 0.1);
  color: var(--primary-emphasis);
  font-size: clamp(1.2rem, 1vw, 1.5rem);
  font-weight: 600;
  text-align: center;
  opacity: 0;
  transition: opacity 0.9s ease;
}

.get-live-title {
  font-size: clamp(0.9rem, 1vw, 1.5rem);
  transition: 0.8s;
}

.get-live-button {
  font-size: clamp(0.9rem, 0.9vw, 1rem);
  transition: 0.8s;
}

.btn-transform {
  transition: 0.3s ease-in-out;
}

.btn-transform:hover {
  transform: scale(1.05);
  transition: 0.3s ease-in-out;
}

@media (min-width: 480px) {
  .get-live-wrapper {
    bottom: 20%;
    right: 14%;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 75%;
    height: 60%;
    padding: 25px;
    transition: 0.8s;
  }
}

@media (min-width: 530px) {
  .get-live-wrapper {
    right: 18%;
    width: 65%;
    transition: 0.8s;
  }
}

@media (min-width: 600px) {
  .get-live-wrapper {
    bottom: 25%;
    right: 19%;
    height: 50%;
    transition: 0.8s;
  }
}

@media (min-width: 650px) {
  .get-live-wrapper {
    bottom: 25%;
    right: 25%;
    width: 55%;
    height: 50%;
    transition: 0.8s;
  }
}

@media (min-width: 768px) {
  .get-live-wrapper {
    bottom: 30%;
    right: 28%;
    width: 45%;
    height: 40%;
    transition: 0.8s;
  }
}

@media (min-width: 946px) {
  .get-live-wrapper {
    bottom: 31%;
    right: 29%;
    width: 40%;
    height: 35%;
    transition: 0.8s;
  }
}

@media (min-width: 992px) {
  .get-live-wrapper {
    bottom: 30%;
    left: 8%;
    width: 35%;
    height: 30%;
    transition: 0.8s;
  }
}

@media (min-width: 1200px) {
  .get-live-wrapper {
    bottom: 35%;
    left: 15%;
    width: 30%;
    height: 25%;
    transition: 0.8s;
  }
}

@media (min-width: 1400px) {
  .get-live-wrapper {
    bottom: 32%;
    left: 21.4%;
    width: 38%;
    height: 30%;
    transition: 0.8s;
  }

  .hero-image-block {
    position: relative;
    width: 100%;
    transition: all 2.5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 6rem 4rem 3rem 1rem rgba(0, 0, 0, 0.4);
  }

  .hero-image-block:hover {
    box-shadow: 2rem 2rem 5rem 1rem rgba(0, 0, 0, 0.6);
    transition: 2.5s;
  }
}
</style>
