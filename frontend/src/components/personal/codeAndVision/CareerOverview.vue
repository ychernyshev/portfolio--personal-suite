<script setup lang="ts">

import ButtonComp from "@/components/personal/ButtonComp.vue";
import CareerTimeline from "@/components/personal/codeAndVision/CareerTimeline.vue";
</script>

<template>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-fullscreen">
      <div class="modal-content border-0 neon-border rounded-2 text-light">
        <div class="modal-header border-0 d-flex justify-content-between">
          <h3 class="modal-title" id="exampleModalLabel">Personal Dev Showcase</h3>
          <button type="button" class="btn bg-transparent border-0 text-light" data-bs-dismiss="modal">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
              <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/>
            </svg>
          </button>
        </div>
        <div class="modal-body pt-0 pb-0">
          <div class="row">
            <div class="col-12 col-xl-5">
              <div class="neon-border p-0 pt-3 rounded-2 text-light">
                <p class="bg-light text-dark p-2 rounded-2 fw-bold">Code & Vision: Engineering Scalable Solutions.</p>
                <p class="p-2 p-lg-0 text-justify">I am a Full-Stack Developer specializing in the Django-REST-Vue ecosystem. My work focuses on bridging the gap between robust, secure back-end logic and high-performance, reactive front-end interfaces.</p>
                <p class="p-2 p-lg-0 text-justify">I treat every project as a unique engineering challenge, prioritizing clean architecture and a "pixel-perfect" mindset. Whether I’m architecting complex mathematical engines like the Solar Power Calculator or developing open-source NPM packages, my goal is to deliver products that are as functional as they are intuitive.</p>
                <p class="p-2 p-lg-0 text-justify">Currently, I am focused on expanding the Code & Vision ecosystem, constantly pushing the boundaries of my technical stack.</p>
                <p class="p-2 p-lg-0 text-justify">Ready to transform your vision into a high-performance reality? <a class="border-0 bg-transparent fw-bold underline-none" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">Let’s talk</a> </p>
              </div>
              <div class="col-12 col-lg-8 col-xl-12 mt-3">
                <label for="core">Core Expertise</label>
                <ul class="ps-0 ps-lg-4">
                  <li class="d-flex justify-content-start p-1">
                    <span class="text-italic my-auto">Backend: </span>
                    <span class="p-md-2 tech-wrapper">
                      <span class="tech-highline ms-2">Python/Django</span>
                      <span class="tech-highline ms-2">DRF</span>
                      <span class="tech-highline ms-2">JWT</span>
                      <span class="tech-highline ms-2">PostgreSQL</span>
                    </span>
                  </li>
                  <li class="d-flex justify-content-start p-1">
                    <span class="text-italic my-auto">Frontend: </span>
                    <span class="p-md-2 tech-wrapper">
                      <span class="tech-highline ms-2">Vue 3</span>
                      <span class="tech-highline ms-2">TypeScript</span>
                      <span class="tech-highline ms-2">Pinia</span>
                      <span class="tech-highline ms-2">Bootstrap</span>
                    </span>
                  </li>
                </ul>
                <label for="high">High-Performance Stack</label>
                <ul class="ps-0 ps-lg-4">
                  <li class="d-flex justify-content-start p-1">
                    <span class="text-italic">Asynchronous Tasks:</span>
                    <span class="tech-highline ms-2">Celery & Redis</span>
                  </li>
                  <li class="d-flex justify-content-start p-1">
                    <span class="text-italic">DevOps:</span>
                    <span class="tech-highline ms-2">Docker containers & CI/CD automation</span>
                  </li>
                  <li class="d-flex justify-content-start p-1">
                    <span class="text-italic">Architecture:</span>
                    <span class="tech-highline ms-2">Advanced TypeScript patterns</span>
                  </li>
                </ul>
              </div>
              <p class="d-flex flex-row">
                <span class="text-italic">Study & Research:</span>
                <span class="tech-highline ms-2">Completed intensive <span class="fw-bold">100+</span> hours practical courses on <span class="fw-bold">Udemy</span> (<span class="fw-bold">Django</span>, <span class="fw-bold">JavaScript</span>, <span class="fw-bold">Vue</span>)</span>
              </p>
            </div>
            <div class="col-12 col-xl-7">
              <career-timeline />
            </div>
          </div>
        </div>
        <div class="modal-footer border-0 pt-0">
          <button-comp title="Download CV" class="btn-success text-light" />
          <button-comp title="Close" class="btn-light" data-bs-dismiss="modal" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-content {
  background-image: url("../../../../public/assets/personal/dark_bg.png");
}

ul {
  line-height: 2rem;
}

.core-expertise {
  display: flex;
  justify-content: start;
}

.tech-highline {
  padding: 0 0.3rem;
  background: var(--p-light-3);
  color: var(--p-dark-2);
  border-radius: .3rem;
}

.tech-wrapper {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  -webkit-flex-wrap: wrap;
  justify-content: start;
  row-gap: 10px;
}

.modal-footer {
  justify-content: center;
}

@media (min-width: 576px) {
  .tech-wrapper {
    width: 70%;
  }

  .tech-highline {
    padding: 0 .4rem;
  }
}

@media (min-width: 768px) {
  .modal-footer {
    justify-content: end;
  }

  .core-expertise {}

  .tech-wrapper {
    width:50%;
  }
}

@media (min-width: 992px) {
  .tech-wrapper {
    width: 60%;
  }
}

@media (min-width: 1200px) {
  .tech-wrapper {
    width: 50%;
  }

  .tech-highline {
    text-align: center;
  }
}
</style>