<script setup lang="ts">
import ButtonComp from "@/components/personal/ButtonComp.vue";
import ImageSlider from "@/components/personal/ImageSlider.vue";
import TechIconsLib from "@/components/personal/TechIconsLib.vue";
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
  techStack: TechSteck[];
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
        <li class="nav-item p-0 w-50" role="presentation">
          <button class="nav-link active w-100" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Projects</button>
        </li>
        <li class="nav-item p-0 w-50" role="presentation">
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
            <div class="row project-description-wrapper">
              <div class="col-12 col-lg-6 col-xl-6">
                <p class="project-title p-0 m-0 mt-lg-5 mt-xl-0 display-4">{{ project.name }}</p>
                <div class="row justify-content-center mt-5 d-block d-lg-none">
                  <div class="col-12 col-lg-4 col-xl-12">
                    <image-slider :images="project.images"/>
                  </div>
                </div>
                <p class="project-unit">
                  <span class="project-unit-bg">{{ project.description }}</span>
                </p>
                <p class="project-unit-comment">
                  <span class="unit-comment-bg">
                    {{ project.unit }}
                  </span>
                </p>
                <div class="row project-icon-wrapper mt-lg-3 m-lg-0 p-lg-0">
                  <div class="col-12 col-md-5 col-lg-12 col-xl-3 col-xxl-4 project-tech-icon">
                    <TechIconsLib
                        v-for="techName in project.techStack"
                        :key="techName"
                        :techName="techName"
                    />
                  </div>
                  <div class="col-12 col-md-7 col-lg-12 col-xl-6 col-xxl-8 mt-lg-3 mt-xl-0">
                    <div class="row p-1 border-lg-start align-items-center">
                      <div class=" col-6 col-lg-6 col-xl-6 d-flex align-items-center">
                        <button-comp title="Live Preview" class="btn-warning text-primary-emphasis d-flex flex-row justify-content-center align-items-center w-100" >
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
                            <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>
                          </svg>
                        </button-comp>
                      </div>
                      <div class=" col-6 col-lg-6 col-xl-6 mt-2 mt-lg-0 d-flex align-items-center">
                        <button-comp title="Source Code" class="btn-light text-primary-emphasis d-flex flex-row justify-content-center align-items-center w-100" >
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
              <div class="col-lg-6 d-none d-lg-block d-xl-none">
                <div class="row justify-content-center mt-5  d-none d-lg-block">
                  <div class="col-12 col-lg-4 col-xl-12">
                    <image-slider :images="project.images"/>
                  </div>
                </div>
              </div>
              <div class="col-12 col-md-11 col-lg-12 col-xl-1 d-flex flex-column mb-4 mb-lg-0 mt-2 mt-lg-3 p-0 p-lg-1 mx-auto mx-lg-0 badges-wrapper">
                <span v-if="project.status === 'Production'" class="bg-success rounded-2 project-status-badge p-2 text-center small">Production</span>
                <span v-else-if="project.status === 'MVP'" class="bg-info rounded-2 project-status-badge p-2 text-center small">MVP</span>
                <span v-else-if="project.status === 'In Development'" class="bg-warning rounded-2 project-status-badge p-2 text-center small">In Development</span>
                <div class="col-12 update-wrapper mt-3 mt-xl-2">
                  <span class="update-title rounded-2 p-1 p-xl-2">Last update:</span>
                  <span class="update-data fw-bold p-1 p-xl-2">{{ project.last_update }}</span>
                </div>
                <div class="col-md-5 mt-xl-2 mt-3 mt-xl-0 badge-future">
                  <span class="badge bg-secondary text-start p-2 mt-xl-1" v-for="future in project.key_futures" :key="future">
                    {{ future }}
                  </span>
                </div>
                <div class="col-12 mt-3 github-badge">
                  <gith-hub-repo-info class="border-1 rounded-2 p-2" repoName="portfolio--personal-suite"/>
                </div>
              </div>
            </div>
            <div class="row justify-content-center mt-5 d-none d-xl-block">
              <div class="col-12 col-lg-4 col-xl-12">
                <image-slider :images="project.images"/>
              </div>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev mt-3" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next mt-3" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
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
    text-align: center;
  }

  .project-unit {
    font-size: clamp(1.2rem, 1.2vw, 1.6rem);
    font-weight: 300;
    color: var(--p-light-3);
    text-align: justify;
  }

  .project-unit-comment {
    font-style: italic;
    text-align: justify;
    font-size: clamp(1.2rem, 1.2vw, 1.6rem);
    color: var(--p-light-3);
  }

  .project-unit-bg {
    padding: 5px 0;
    background: var(--p-darker-1);
    line-height: 2rem;
  }

  .unit-comment-bg {
    padding: 5px 10px;
    background-color: var(--p-darker-1);
  }

  .update-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    line-height: 3rem;
  }

  .update-title {
    color: var(--p-light-3);
    background-color: var(--p-darker-1);
    font-size: clamp(1.2rem, 1.2vw, 1.6rem);
  }

  .update-data {
    font-size: clamp(1.2rem, 1.2vw, 1.6rem);
  }

  .badge-future {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    -webkit-flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    width: 100%;
    column-gap: 10px;
  }

  .github-badge {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    -webkit-flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 0.25rem;
    font-size: clamp(1.4rem, 1.5vw, 1.6rem);
  }

  .project-icon-wrapper {
    display: flex;
    -webkit-flex-wrap: wrap;
    justify-content: center;
  }

  .project-tech-icon {
    display: flex;
    justify-content: center;
    width: 80%;
    transition: 0.8s;
  }

  .project-status-badge {
    width: 100%;
  }

  @media (min-width: 389px) {
    .project-title {
      display: flex;
      justify-content: center;

    }
  }

  @media (min-width: 570px) {
    .project-tech-icon {
      width: 60%;
    }
  }

  @media (min-width: 760px) {
    .project-tech-icon {
      width: 45%;
    }
  }

  @media (min-width: 768px) {
    .project-title {
      display: block;
      width: auto;
      text-align: center;
    }

    .project-unit {
      text-align: justify;
      line-height: 2.2rem;
    }

    .project-unit-bg {
      background-color: var(--p-darker-1);
    }

    .border-lg-start {
      border-left: .1rem solid var(--p-light-3);
    }

    .update-wrapper {
      text-align: center;
    }

    .update-title {
      color: var(--p-light-3);
      background-color: var(--p-darker-1);
    }

    .badge-future {
      justify-content: center;
      font-size: clamp(1.2rem, 1.2vw, 1.6rem);
    }

    .github-badge {
      justify-content: center;
    }

    .project-icon-wrapper {
      justify-content: center;
    }

    .project-tech-icon {
      width: 33%;
    }
  }

  @media (min-width: 946px) {
    .project-unit-bg {
      background-color: var(--p-darker-2);
    }
  }

  @media (min-width: 992px) {
    .project-unit-bg {
      background: transparent;
    }

    .project-tech-icon {
      width: 55%;
    }

    .border-lg-start {
      border-left: none;
    }

    .badges-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .project-status-badge {
      width: 20%;
    }
  }

  @media (min-width: 1056px) {
    .unit-comment-bg {
      background: transparent;
    }
  }

  @media (min-width: 1200px) {
    .project-description-wrapper {
      justify-content: center;
    }

    .project-title {
      text-align: end;
    }

    .project-unit-comment {
      text-align: end;
    }

    .update-data {
      width: 100%;
      color: var(--p-light-3);
    }

    .update-wrapper {
      flex-direction: column;
      align-items: start;
      line-height: .5rem;
      text-align: start;
    }

    .update-title {
      background-color: transparent;
      line-height: 1rem;
    }

    .badge-future {
      justify-content: start;
    }

    .github-badge {
      justify-content: start;
    }

    .project-icon-wrapper {
      justify-content: end;
      align-items: center;
    }

    .project-tech-icon {
      width: 50%;
    }

    .border-lg-start {
      border-left: .1rem solid var(--p-light-3);
    }

    .project-status-badge {
      width: 100%;
    }
  }

  @media (min-width: 1400px) {
    .project-tech-icon {
      width: 33%;
    }

  }

  @media (min-width: 1600px) {
    .project-tech-icon {
      width: 30%;
    }
  }
</style>