<script setup lang="ts">
  import {computed} from "vue";

  const props = defineProps<{
    images: { path: string; title: string }[];
  }>()

  const step = 6;

  const totalTime = computed(() => props.images.length * step);
</script>

<template>
  <div class="cb-slideshow-wrapper">
    <ul class="cb-slideshow">
      <li v-for="(img, index) in images" :key="index">
      <span :style="{
        backgroundImage: `url(${img.path})`,
        animationDuration: `${totalTime}s`,
        animationDelay: `${index * 6}s`
      }"></span>
        <div :style="{
        animationDuration: `${totalTime}s`,
        animationDelay: `${index * 6}s`
      }">
          <h3>{{ img.title }}</h3>
        </div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
  .cb-slideshow-wrapper {
    position: relative;
    width: 100%;
    height: 30vh;
    overflow: hidden;
    z-index: 1;
  }

  .cb-slideshow {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }

  .cb-slideshow,
  .cb-slideshow:after {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    z-index: 0;
  }

  .cb-slideshow:after {
    content: '';
    background-size: 5px 5px;
  }

  .cb-slideshow li span {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    color: transparent;
    background-size: cover;
    background-position: 50% 50%;
    background-repeat: no-repeat;
    opacity: 0;
    z-index: 0;
    animation: imageAnimation linear infinite;
  }
  .cb-slideshow li div {
    z-index: 1000;
    position: absolute;
    bottom: 30px;
    left: 0;
    width: 100%;
    text-align: center;
    opacity: 0;
    color: var(--primary-emphasis);
    animation: titleAnimation linear infinite;
  }
  .cb-slideshow li div h3 {
    position: absolute;
    bottom: 0;
    margin: 0;
    left: 1rem;
    font-family: 'BebasNeueRegular', 'Arial Narrow', Arial, sans-serif;
    font-size: clamp(1.4rem, 2.5vw, 3.5rem);
    padding: 0;
    line-height: 1.5rem;
  }

  /* imageAnimation 1 */
  @keyframes imageAnimation1 {
    0% { opacity: 0; animation-timing-function: ease-in; }
    8% { opacity: 1; animation-timing-function: ease-out; }
    17% { opacity: 1 }
    25% { opacity: 0 }
    100% { opacity: 0 }
  }

  /* imageAnimation 2 */
  @keyframes imageAnimation {
    0% {
      opacity: 0;
      animation-timing-function: ease-in;
    }
    8% {
      opacity: 1;
      transform: scale(1.05);
      animation-timing-function: ease-out;
    }
    17% {
      opacity: 1;
      transform: scale(1.1) rotate(3deg);
    }
    25% {
      opacity: 0;
      transform: scale(1.1) rotate(3deg);
    }
    100% { opacity: 0 }
  }
  /* titleAnimation 1 */
  @keyframes titleAnimation1 {
    0% { opacity: 0 }
    8% { opacity: 1 }
    17% { opacity: 1 }
    19% { opacity: 0 }
    100% { opacity: 0 }
  }
  /* titleAnimation 2 */
  @keyframes titleAnimation {
    0% {
      opacity: 0;
      transform: translateX(200px);
    }
    8% {
      opacity: 1;
      transform: translateX(0px);
    }
    17% {
      opacity: 1;
      transform: translateX(0px);
    }
    19% {
      opacity: 0;
      transform: translateX(-400px);
    }
    25% { opacity: 0 }
    100% { opacity: 0 }
  }

  @media (min-width: 992px) {
    .cb-slideshow-wrapper {
      position: relative;
      width: 50vw;
      height: 60vh;
      overflow: hidden;
      z-index: 1;
    }

    .cb-slideshow,
    .cb-slideshow:after {
      position: absolute;
      width: 100%;
      height: 100%;
      top: 0;
      right: 0;
      z-index: 0;
    }

    .cb-slideshow li div {
      bottom: 10rem;
    }
  }

  @media (min-width: 1200px) {
    .cb-slideshow-wrapper {
      position: relative;
      overflow: auto;
      width: 100%;
      height: 100%;
    }

    .cb-slideshow,
    .cb-slideshow:after {
      position: fixed;
      width: 45%;
      height: 45%;
      top: 64%;
      right: 25%;
      z-index: 0;
    }

    .cb-slideshow li div {
      bottom: 5rem;
    }

    .cb-slideshow {
      list-style-type: none;
      margin: 0;
      padding: 0;
    }

    .cb-slideshow li span {
      background-size: cover;
    }

    .cb-slideshow li div h3 {
      bottom: 4rem;
      line-height: 3rem;
    }
  }

  @media (min-width: 1377px) {
    .cb-slideshow,
    .cb-slideshow:after {
      top: 60%;
    }
  }

  @media (min-width: 1400px) {
    .cb-slideshow,
    .cb-slideshow:after {
      top: 58%;
    }

    .cb-slideshow li div {
      bottom: 5rem;
    }
  }

  @media (min-width: 1600px) {
    .cb-slideshow,
    .cb-slideshow:after {
      top: 60%;
    }
  }
</style>