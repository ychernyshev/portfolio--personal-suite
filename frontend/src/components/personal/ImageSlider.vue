<script setup lang="ts">
  const props = defineProps<{
    images: { path: string; title: string }[];
  }>()
</script>

<template>
  <ul class="cb-slideshow">
    <li v-for="img in images" :key="img">
      <span :style="{
        backgroundImage: `url(${img.path})`
      }"></span>
      <div>
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
    bottom: 0;
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
    animation: imageAnimation 36s linear infinite 0s;
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
    animation: titleAnimation 36s linear infinite 0s;
  }
  .cb-slideshow li div h3 {
    margin: 0;
    font-family: 'BebasNeueRegular', 'Arial Narrow', Arial, sans-serif;
    font-size: clamp(5rem, 5vw, 5rem);
    padding: 0;
    line-height: 5rem;
  }

  .cb-slideshow li:nth-child(1) span {
    background-image: url("@/assets/images/solar_power_calculator/calc_dashboard.png");
  }
  .cb-slideshow li:nth-child(2) span {
    background-image: url(https://images.unsplash.com/photo-1584957109774-c9b6d1ba9d4b?crop=entropy&cs=srgb&fm=jpg&ixid=M3wzMjM4NDZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTkxODM0NjV8&ixlib=rb-4.0.3&q=85&width=1600);
    animation-delay: 6s;
  }
  .cb-slideshow li:nth-child(3) span {
    background-image: url(https://images.unsplash.com/photo-1509067917181-3ec8d8ef5170?crop=entropy&cs=srgb&fm=jpg&ixid=M3wzMjM4NDZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTkxODM2MDZ8&ixlib=rb-4.0.3&q=85&q=85&width=1600);
    animation-delay: 12s;
  }
  .cb-slideshow li:nth-child(4) span {
    background-image: url(https://images.unsplash.com/photo-1462392246754-28dfa2df8e6b?crop=entropy&cs=srgb&fm=jpg&ixid=M3wzMjM4NDZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTkxODM2MDZ8&ixlib=rb-4.0.3&q=85&width=1600);
    animation-delay: 18s;
  }
  .cb-slideshow li:nth-child(5) span {
    background-image: url(https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?crop=entropy&cs=srgb&fm=jpg&ixid=M3wzMjM4NDZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTkxODM3MTd8&ixlib=rb-4.0.3&q=85&width=1600);
    animation-delay: 24s;
  }
  .cb-slideshow li:nth-child(6) span {
    background-image: url(https://images.unsplash.com/photo-1470010762743-1fa2363f65ca?crop=entropy&cs=srgb&fm=jpg&ixid=M3wzMjM4NDZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTkxODM3NzB8&ixlib=rb-4.0.3&q=85&width=1600);
    animation-delay: 30s;
  }
  .cb-slideshow li:nth-child(2) div {
    animation-delay: 6s;
  }
  .cb-slideshow li:nth-child(3) div {
    animation-delay: 12s;
  }
  .cb-slideshow li:nth-child(4) div {
    animation-delay: 18s;
  }
  .cb-slideshow li:nth-child(5) div {
    animation-delay: 24s;
  }
  .cb-slideshow li:nth-child(6) div {
    animation-delay: 30s;
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