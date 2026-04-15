<script setup lang="ts">
  import {computed} from "vue";

  const props = defineProps<{
    images: { path: string; title: string }[];
  }>()

  const step = 6;

  const totalTime = computed(() => props.images.length * step);
</script>

<template>
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
</template>

<style scoped>
  .cb-slideshow {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  .cb-slideshow,
  .cb-slideshow:after {
    position: fixed;
    width: 45%;
    height: 45%;
    top: 60%;
    right: 25%;
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
    top: 0px;
    left: 0px;
    color: transparent;
    background-size: cover;
    background-position: 50% 50%;
    background-repeat: none;
    opacity: 0;
    z-index: 0;
    animation: imageAnimation linear infinite;
  }
  .cb-slideshow li div {
    z-index: 1000;
    position: absolute;
    bottom: 30px;
    left: 0px;
    width: 100%;
    text-align: center;
    opacity: 0;
    color: var(--primary-emphasis);
    animation: titleAnimation linear infinite;
  }
  .cb-slideshow li div h3 {
    position: absolute;
    bottom: 5rem;
    margin: 0;
    font-family: 'BebasNeueRegular', 'Arial Narrow', Arial, sans-serif;
    font-size: clamp(2.5rem, 2.5vw, 2.5rem);
    padding: 0;
    line-height: 3rem;
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
  @media screen and (max-width: 1140px) {
    .cb-slideshow li div h3 { font-size: 140px }
  }
  @media screen and (max-width: 600px) {
    .cb-slideshow li div h3 { font-size: 80px }
  }
</style>