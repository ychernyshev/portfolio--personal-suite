<script setup></script>

<template>
  <nav class="navbar navbar-expand-lg bg-light" data-bs-theme="light">
    <div class="container-fluid p-3">
      <a
        class="navbar-brand bg-c-sunrise p-3 rounded-5 text-white"
        style="box-shadow: 0.5rem 0.5rem 1rem 0 rgba(255, 193, 7, 0.9)"
        href="{% url 'calculator:dashboard' %}"
        >Solar Power Calculator</a
      >
      <button
        class="navbar-toggler text-secondary"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="36"
          height="36"
          fill="currentColor"
          class="bi bi-list"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"
          />
        </svg>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div
          class="collapse navbar-collapse d-flex justify-content-end"
          id="navbarColor04"
        >
          <div class="weight-600 text-upper text-light">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item links">
                <router-link to="dashboard" class="nav-link"
                  >dashboard</router-link
                >
              </li>
              <li class="nav-item links">
                <router-link to="add_entry" class="nav-link"
                  >add entry</router-link
                >
              </li>
              <li class="nav-item links">
                <router-link to="settings" class="nav-link"
                  >settings</router-link
                >
              </li>
            </ul>
            <!-- <router-link to="dashboard" class="nav-link">Dashboard</router-link>
            <router-link to="add_entry" class="nav-link">Add entry</router-link>
            <router-link to="settings" class="nav-link">Settings</router-link> -->
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
