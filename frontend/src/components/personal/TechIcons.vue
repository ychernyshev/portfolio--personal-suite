<script setup lang="ts">
import TechPopover from "@/components/personal/TechPopover.vue";

interface Icon {
  id: string;
  path: string;
  description: string;
}

const props = defineProps<{
  techName: string;
}>();

type IconName =
    | "django"
    | "drf"
    | "celery"
    | "js"
    | "typescript"
    | "bootstrap"
    | "docker"
    | "vue"
    | "redis"
    | "pinia";

type TechIconSet = Record<IconName, Icon>;

const icons: TechIconSet = {
  django: {
    id: "django",
    path: new URL('@/assets/images/tech-icons/django.png', import.meta.url).href,
    description: 'Django is an open-source and high-level Python-based web framework that runs on a web server and is traditionally used as a project backend.'
  },
  drf: {
    id: "drf",
    path: new URL('@/assets/images/tech-icons/drf.png', import.meta.url).href,
    description: 'Django REST Framework (DRF) is a powerful toolkit built on top of Django for creating Web APIs. Allowing your project to communicate with mobile gadgets, local, and dedicated services, etc.'
  },
  vue: {
    id: "vue",
    path: new URL('@/assets/images/tech-icons/vue.png', import.meta.url).href,
    description: "Vue (pronounced /vjuː/, like view) is a JavaScript framework for building user interfaces."
  },
  typescript: {
    id: "typescript",
    path: new URL('@/assets/images/tech-icons/typescript.png', import.meta.url).href,
    description: "TypeScript (TS) is a high-level programming language that adds static typing with optional type annotations to JavaScript. Needed for the much cleaner code."
  },
  js: {
    id: "js",
    path: new URL('@/assets/images/tech-icons/js.png', import.meta.url).href,
    description: "JavaScript (JS) is a high-level, multi-paradigm programming language that serves as a core technology of the World Wide Web alongside HTML and CSS."
  },
  bootstrap: {
    id: "bootstrap",
    path: new URL('@/assets/images/tech-icons/bootstrap.png', import.meta.url).href,
    description: "Bootstrap is an HTML, CSS and JS library that focuses on visual style development of web pages."
  },
  pinia: {
    id: "pinia",
    path: new URL('@/assets/images/tech-icons/pinia.png', import.meta.url).href,
    description: "Pinia is a store library for Vue that allows sharing a state across components/pages. Logins, counts, and other information that is needed in different project components like cards, accounts, favorite lists, etc."
  },
  celery: {
    id: "celery",
    path: new URL('@/assets/images/tech-icons/celery.png', import.meta.url).href,
    description: "Celery is an asynchronous task queue/job or job queue. It is used for executing tasks in the background. Sending an email to the client after registration, for example."
  },
  redis: {
    id: "redis",
    path: new URL('@/assets/images/tech-icons/redis.png', import.meta.url).href,
    description: "Redis (/ˈrɛdɪs/; Remote Dictionary Server) is an in-memory key–value database, used as a distributed cache and message broker, with optional durability. For example, instantly get data that is often used"
  },
  docker: {
    id: "docker",
    path: new URL('@/assets/images/tech-icons/docker.png', import.meta.url).href,
    description: "Docker is a set of products that uses operating system-level virtualization to deliver software in packages called containers, with the components needed to build projects using it as a constructor. Container with backend - Django, container with frontend - Vue, container with database - PostgreSQL, etc. It ensures that the project works the same way on the computer, on the server, and everywhere else. For testing and developing, the project runs with one command. The system does preparation, launch, and everything else automatically."
  }
}

const iconEntries = Object.entries(icons) as [string, Icon][];
</script>

<template>
  <div v-if="!techName" class="row tech-centering">
    <div class="d-flex flex-row flex-wrap w-75 mb-4 tech-centering">
      <tech-popover
          v-for="[name, icon] in iconEntries"
          :key="name"
          :content="icon.description"
          class="lc-block col-2 col-lg-3 m-1 tech-icon"
      >
          <img
              :src="icon.path"
              class="img-fluid wp-image-975"
              width=""
              height="100"
              srcset=""
              sizes=""
              alt="">
      </tech-popover>
    </div>
  </div>
  <div v-else-if="icons[techName as IconName]" class="d-inline-block">
    <tech-popover
        :content="icons[techName as IconName].description"
        class="tech-icon d-inline-block m-1"
    >
      <img
          :src="icons[techName as IconName].path"
          class="img-fluid"
          style="width: 40px; height: 40px; object-fit: contain;"
          :alt="techName"
      >
    </tech-popover>
  </div>
</template>

<style scoped>
  .tech-icon {
    filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.3));
    transition: all 0.3s ease;
  }
  .tech-icon:hover {
    transform: translateY(-5px);
    filter: drop-shadow(0 8px 12px rgba(0, 0, 0, 0.5));
  }
</style>