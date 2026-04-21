<script setup lang="ts">
import { ref } from 'vue';
import { timeline, type CareerItem } from '@/static-data/careerData';
import TechIconsLib from '@/components/personal/TechIconsLib.vue';
import ButtonComp from "@/components/personal/ButtonComp.vue";

const scrollToExperience = (id: string) => {
  const element = document.getElementById(id);
  if (element) {
    element.scrollIntoView({
      behavior: 'smooth',
      block: 'start',
    });
  }
};
</script>

<template>
  <div class="career-modal-wrapper">
    <div class="timeline-navigation col-3 col-xl-3">
      <div class="timeline-line">
        <div
            v-for="(item, index) in timeline"
            :key="item.id"
            class="timeline-dot-wrapper"
            @click="scrollToExperience(item.id)"
            :style="{ top: (index * (100 / (timeline.length - 1))) + '%' }"
        >
          <div class="timeline-dot"></div>
          <span class="timeline-date-label timeline-date">{{ item.date }}</span>
        </div>
      </div>
    </div>

    <div class="timeline-content">
      <div
          v-for="item in timeline"
          :key="item.id"
          :id="item.id"
          class="timeline-card"
      >
        <div class="card-header">
          <span class="card-date">{{ item.date }}</span>
          <h3>{{ item.title }}</h3>
          <p v-if="item.currentOccupation" class="row current-pos">
            <span class="badge-status text-light col-12 col-lg-4 fw-bold">current occupation:</span>
            <span class="fw-bold col-12 col-lg-8">{{ item.currentOccupation }}</span>
          </p>
          <p v-if="item.occupationDescription" class="row current-pos">
            <span class="badge-status text-light col-12 col-lg-4 fw-bold">occupation description:</span>
            <span class="fw-bold col-12 col-lg-8">{{ item.occupationDescription }}</span>
          </p>
          <span v-if="item.occupationDescription" class="row current-pos">
            <span class="badge-status text-light col-12 col-lg-4 fw-bold mb-3">
              Acquiring programming skills since...</span>
          </span>
          <div v-if="item.techStack" class="tech-icon-wrapper">
            <TechIconsLib
                v-for="tech in item.techStack"
                :key="tech"
                :name="tech"
                :tech-name="tech"
                class="tech-icon-size"
            />
          </div>
          <div v-for="project in item.projects" class="row card-example rounded-2 mt-3">
            <p class="example-title">{{ project.title }}</p>
            <p class="example-description">{{ project.description }}</p>
              <div v-if="project.title && project.description" class="d-flex flex-row p-0 example-button-group-wrapper">
                <button-comp
                    v-if="project.livePreviewUrl"
                    :to="project.livePreviewUrl"
                    title="Live Preview"
                    class="btn-warning w-50 rounded-0 rounded-start"></button-comp>
                <button-comp v-if="project.sourceCodeUrl" :href="project.sourceCodeUrl" title="Source Code" class="btn-light w-50 rounded-0 rounded-end"></button-comp>
              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .career-modal-wrapper {
    display: flex;
    height: 85vh;
    overflow: hidden;
  }

  .timeline-navigation {
    position: relative;
    display: flex;
    justify-content: start;
    border-right: 1px solid rgba(0, 243, 255, 0.1);
    height: 100%;
    overflow-y: auto;
  }

  .timeline-line {
    position: absolute;
    top: 31px;
    left: 5px;
    bottom: 40px;
    width: 2px;
    background: var(--primary-emphasis-2);
    box-shadow: 0 0 10px var(--primary-emphasis);
    opacity: 0.3;
  }

  .timeline-dot-wrapper {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .timeline-dot {
    width: 16px;
    height: 16px;
    background: var(--neon-blue-1);
    border: 2px solid var(--primary-emphasis);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--primary-emphasis);
    transition: all 0.3s ease;
    z-index: 10;
  }

  .timeline-dot-wrapper:hover .timeline-dot {
    transform: scale(1.3);
    background: var(--primary-emphasis-4);
    box-shadow: 0 0 20px var(--primary-emphasis);
  }

  .timeline-date-label {
    position: absolute;
    top: -5px;
    left: 25px;
    word-wrap: break-word;
    font-size: 0.7rem;
    color: var(--p-light-3);
    margin-top: 5px;
  }

  .timeline-content {
    flex: 1;
    height: 100%;
    overflow-y: auto;
    padding: 20px;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
  }

  .timeline-content::-webkit-scrollbar {
    width: 6px;
  }

  .timeline-content::-webkit-scrollbar-track {
    background: transparent;
  }

  .timeline-content::-webkit-scrollbar-thumb {
    background-color: var(--neon-blue-1);
    border-radius: 20px;
    border: 1px solid transparent;
  }

  .timeline-content::-webkit-scrollbar-thumb:hover {
    background-color: var(--primary-emphasis);
  }

  .timeline-card {
    margin-bottom: 40px;
    padding-top: 10px;
  }

  .tech-icon-wrapper {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    -webkit-flex-wrap: wrap;
  }

  .tech-icon-size {
    width: 33%;
    transition: 0.8s;
  }

  .current-pos {
    font-size: 0.9rem;
    color: var(--p-light-3);
    margin-top: 4px;
    font-style: italic;
  }

  .badge-status {
    background: rgba(0, 243, 255, 0.1);
    color: var(--primary-emphasis);
    padding: 2px 8px;
    border-radius: 4px;
    margin-right: 5px;
    font-style: normal;
    font-size: clamp(1rem, 1vw, 0.7rem);
    text-transform: uppercase;
  }

  .card-example {
    background: rgba(255, 255, 255, 0.1);
  }

  .example-title {
    padding: 0.3rem 0.5rem;
    background-color: rgba(30, 35, 66, 1);
    backdrop-filter: blur(10px);
    font-size: clamp(1rem, 1vw, 1rem);
    font-weight: 600;
    text-transform: uppercase;
    color: var(--p-light-3);
  }

  .example-description {
    padding: 0.3rem 0.5rem;
  }

  @media (min-width: 400px) {
    .tech-icon-size {
      width: 30%;
    }
  }

  @media (min-width: 480px) {
    .tech-icon-size {
      width: 27%;
    }
  }

  @media (min-width: 575px) {
    .tech-icon-size {
      width: 20%;
    }
  }
  
  @media (min-width: 720px) {
    .timeline-date-label {
      white-space: nowrap;
    }

    .example-button-group-wrapper {
      width: 75%;
    }
  }

  @media (min-width: 766px) {
    .tech-icon-size {
      width: 15%;
    }
  }

  @media (min-width: 990px) {
    .tech-icon-size {
      width: 10%;
    }
  }

  @media (min-width: 1200px) {
    .tech-icon-size {
      width: 13%;
    }
  }

  @media (min-width: 1396px) {
    .tech-icon-size {
      width: 11%;
    }
  }

  @media (min-width: 1600px) {
    .tech-icon-size {
      width: 9%;
    }
  }
</style>