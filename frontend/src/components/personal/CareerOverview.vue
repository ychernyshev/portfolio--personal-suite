<script setup lang="ts">

import ButtonComp from "@/components/personal/ButtonComp.vue";
import CareerTimeline from "@/components/personal/home/CareerTimeline.vue";
</script>

<template>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-fullscreen">
      <div class="modal-content border-0 neon-border rounded-2 text-light">
        <div class="modal-header border-0 d-flex justify-content-between">
          <h3 class="modal-title" id="exampleModalLabel">Career Overview</h3>
          <button type="button" class="btn bg-transparent border-0 text-light" data-bs-dismiss="modal">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
              <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/>
            </svg>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-12 col-xl-5">
              <div class="neon-border p-3 rounded-2 text-light">
                <p class="bg-light text-dark p-2 rounded-2 fw-bold">Code & Vision: Engineering Scalable Solutions.</p>
                <p>I am a Full-Stack Developer specializing in the Django-REST-Vue ecosystem. My work focuses on bridging the gap between robust, secure back-end logic and high-performance, reactive front-end interfaces.</p>
                <p>I treat every project as a unique engineering challenge, prioritizing clean architecture and a "pixel-perfect" mindset. Whether I’m architecting complex mathematical engines like the Solar Power Calculator or developing open-source NPM packages, my goal is to deliver products that are as functional as they are intuitive.</p>
                <p>Currently, I am focused on expanding the Code & Vision ecosystem, constantly pushing the boundaries of my technical stack.</p>
                <p>Ready to transform your vision into a high-performance reality? <a class="border-0 bg-transparent fw-bold underline-none" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">Let’s talk</a> </p>
              </div>
              <div class="col-12 col-lg-8 mt-3">
                <label for="core">Core Expertise</label>
                <ul>
                  <li class="d-flex justify-content-between p-1">
                    <span class="text-italic">Backend: </span>
                    <span class="tech-highline">Python/Django</span>
                    <span class="tech-highline">REST API (DRF)</span>
                    <span class="tech-highline">JWT Auth</span>
                    <span class="tech-highline">PostgreSQL</span>
                  </li>
                  <li class="d-flex justify-content-between p-1">
                    <span class="text-italic">Frontend: </span>
                    <span class="tech-highline">Vue 3 (Composition API)</span>
                    <span class="tech-highline">TypeScript</span>
                    <span class="tech-highline">Pinia</span>
                    <span class="tech-highline">SCSS</span>
                  </li>
                </ul>
                <label for="high">High-Performance Stack</label>
                <ul>
                  <li class="d-flex justify-content-start p-1">
                    <span class="text-italic">Asynchronous Tasks:</span>
                    <span class="tech-highline">Celery & Redis (Background processing)</span>
                  </li>
                  <li class="d-flex justify-content-start p-1">
                    <span class="text-italic">DevOps:</span>
                    <span class="tech-highline">Docker containers & CI/CD automation</span>
                  </li>
                  <li class="d-flex justify-content-start p-1">
                    <span class="text-italic">Architecture:</span>
                    <span class="tech-highline">Advanced TypeScript patterns</span>
                  </li>
                </ul>
              </div>
              <p class="d-flex flex-row">
                <span class="text-italic">Study & Research:</span>
                <span class="tech-highline">Completed intensive <span class="fw-bold">100+</span> hours practical courses on <span class="fw-bold">Udemy</span> (<span class="fw-bold">Django</span>, <span class="fw-bold">JavaScript</span>, <span class="fw-bold">Vue</span>)</span>
              </p>
            </div>
            <div class="col-12 col-xl-7">
              <career-timeline />
            </div>
          </div>
        </div>
        <div class="modal-footer border-0">
          <button-comp title="Download CV" class="btn-success text-light" />
          <button-comp title="Close" class="btn-light" data-bs-dismiss="modal" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-content {
  background-image: url("../../../public/assets/personal/dark_bg.png");
}

ul {
  line-height: 2rem;
}

.tech-highline {
  background: var(--p-light-3);
  color: var(--p-dark-2);
  border-radius: .3rem;
}

.modal-footer {
  justify-content: center;
}

@media (min-width: 520px) {
  .tech-highline {
    padding: 0 .1rem;
  }
}

@media (min-width: 768px) {
  .modal-footer {
    justify-content: end;
  }
}
</style>