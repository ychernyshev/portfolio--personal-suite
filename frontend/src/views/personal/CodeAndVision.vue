<script setup lang="ts">
import ButtonComp from "@/components/personal/ButtonComp.vue";
import ImageSlider from "@/components/personal/ImageSlider.vue";
import TechIcons from "@/components/personal/TechIcons.vue";
import GithHubRepoInfo from "@/components/personal/GithHubRepoInfo.vue";

interface ProjectImage {
  path: string;
  title: string;
}

interface TechSteck {
  name: string;
}

interface KeyFutures {
  name: string;
}

interface Project {
  id: string;
  name: string;
  description: string;
  unit: string;
  status: string
  last_update: string;
  key_futures: KeyFutures[];
  techSteck: TechSteck[];
  images: ProjectImage[];
  liveUrl?: string;
  repoUrl?: string;
}

const projects: Project[] = [
  {
    id: 'solar-calculator',
    name: 'Solar Power Calculator',
    description: "A web application dashboard that calculates solar power generation and cost savings. The app allows adding the accumulated charging level in percentages and the current power cost from energy meters. These parameters need to be entered 2-3 times per day, as the app calculates the power that the solar system generates throughout the day and how much money this power costs",
    unit: "\"Created for myself to explore and analyze the capacity and productivity of my own solar power station\"",
    status: "MVP",
    last_update: "12.04.2026",
    key_futures: ['Reactive UI', 'Real-time calculations'],
    techStack: ['django', 'vue', 'js', 'bootstrap'],
    images: [
      {
        path: new URL('@/assets/images/solar_power_calculator/calc_dashboard.png', import.meta.url).href,
        title: 'Single screen Dashboard',
      },
      {
        path: new URL('@/assets/images/solar_power_calculator/calc_dashboard.png', import.meta.url).href,
        title: 'Record Data and Reactive Reload',
      },
      {
        path: new URL('@/assets/images/solar_power_calculator/calc_dashboard.png', import.meta.url).href,
        title: 'Setup your app',
      },
      {
        path: new URL('@/assets/images/solar_power_calculator/calc_dashboard.png', import.meta.url).href,
        title: 'Controlling power and cost inficators ont the graphics',
      }
    ]
  }
];
</script>

<template>
  <div class="row justify-content-center align-items-center mt-4">
    <div class="col-12 col-xl-4">
      <ul class="nav nav-tabs border-0" id="myTab" role="tablist">
        <li class="nav-item p-1 w-50" role="presentation">
          <button class="nav-link active w-100" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Projects</button>
        </li>
        <li class="nav-item p-1 w-50" role="presentation">
          <button class="nav-link w-100" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Packages</button>
        </li>
      </ul>
    </div>
  </div>
  <div class="tab-content" id="myTabContent">
    <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
      <div id="carouselExampleControls" class="carousel carousel-wrapper slide mt-4" data-bs-ride="carousel">
        <div class="carousel-inner carousel-child">
          <div
              class="carousel-item active"
              v-for="(project, index) in projects"
              :key="project.id"
              :class="['carousel-item', { active: index === 0 }]"
          >
            <div class="col-12">
              <p class="project-title text-center display-5">{{ project.name }}</p>
            </div>
            <div class="row justify-content-center">
              <div class="col-lg-6">
                <p class="project-unit text-end">
                  {{ project.description }}
                </p>
                <p class="text-italic text-end text-light">{{ project.unit }}</p>
                <div class="row justify-content-end mt-lg-3">
                  <div class="col-xl-3 d-flex justify-content-end">
                    <TechIcons
                        v-for="techName in project.techStack"
                        :key="techName"
                        :techName="techName"
                    />
                  </div>
                  <div class="col-4 col-xl-7">
                    <div class="row p-1 border-start">
                      <div class=" col-8 col-lg-4 col-xl-6 d-flex align-items-center">
                        <button-comp title="Live Preview" class="btn-warning d-flex flex-row justify-content-center align-items-center w-100" >
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
                            <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>
                          </svg>
                        </button-comp>
                      </div>
                      <div class=" col-8 col-lg-4 col-xl-6 mt-2 mt-lg-0 d-flex align-items-center">
                        <button-comp title="Source Code" class="btn-light d-flex flex-row justify-content-center align-items-center w-100" >
                          <template #left>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-code" viewBox="0 0 16 16">
                              <path d="M5.854 4.854a.5.5 0 1 0-.708-.708l-3.5 3.5a.5.5 0 0 0 0 .708l3.5 3.5a.5.5 0 0 0 .708-.708L2.707 8zm4.292 0a.5.5 0 0 1 .708-.708l3.5 3.5a.5.5 0 0 1 0 .708l-3.5 3.5a.5.5 0 0 1-.708-.708L13.293 8z"/>
                            </svg>
                          </template>
                          <template #right>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-code-slash" viewBox="0 0 16 16">
                              <path d="M10.478 1.647a.5.5 0 1 0-.956-.294l-4 13a.5.5 0 0 0 .956.294zM4.854 4.146a.5.5 0 0 1 0 .708L1.707 8l3.147 3.146a.5.5 0 0 1-.708.708l-3.5-3.5a.5.5 0 0 1 0-.708l3.5-3.5a.5.5 0 0 1 .708 0m6.292 0a.5.5 0 0 0 0 .708L14.293 8l-3.147 3.146a.5.5 0 0 0 .708.708l3.5-3.5a.5.5 0 0 0 0-.708l-3.5-3.5a.5.5 0 0 0-.708 0"/>
                            </svg>
                          </template>
                        </button-comp>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-1 d-flex flex-column">
                <span v-if="project.status === 'Production'" class="bg-success rounded-2 w-100 p-2 text-center small">Production</span>
                <span v-else-if="project.status === 'MVP'" class="bg-info rounded-2 w-100 p-2 text-center small">MVP</span>
                <span v-else-if="project.status === 'In Development'" class="bg-warning rounded-2 w-100 p-2 text-center small">In Development</span>
                <div class="update-wrapper">
                  <span class="text-light rounded-2 w-100 small mt-xl-2 p-xl-2">Last update:</span>
                  <span class="fw-bold updating-data small p-xl-2">{{ project.last_update }}</span>
                </div>
                <div class="mt-xl-2">
                  <span class="badge bg-secondary text-start p-2 mt-xl-1" v-for="future in project.key_futures" :key="future">
                  {{ future }}
                </span>
                </div>
                <div class="col-12">
                  <gith-hub-repo-info class="border-1 rounded-2 p-2" />
                </div>
              </div>
            </div>
            <div class="row justify-content-center mt-5">
              <div class="col-12 col-lg-4 col-xl-12">
                <image-slider :images="project.images"/>
              </div>
            </div>
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
    </div>
    <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">...</div>
  </div>

<!--  <h3 class="text-center text-light mt-5">Code & Vision </h3>-->
</template>

<style scoped>
  .carousel-wrapper {
    position: relative;
  }

  .carousel-child {
    position: absolute;
    top: 0;
  }

  .project-title {
    font-weight: 500;
    color: var(--primary-emphasis-2);
  }

  .project-unit {
    font-size: clamp(1.2rem, 1.2vw, 1.2rem);
    font-weight: 300;
    color: var(--p-light-3);
  }

  @media (min-width: 1200px) {
    .update-wrapper {
      display: flex;
      flex-direction: column;
      justify-content: start;
      line-height: .5rem;
    }

    .updating-data {
      color: var(--p-light-3);
    }
  }
</style>