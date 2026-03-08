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
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarColor04">
        <div
          class="collapse navbar-collapse d-flex justify-content-end"
          id="navbarColor04"
        >
          <div class="links weight-600 text-upper text-light">
            <router-link to="dashboard">Dashboard</router-link>
            <router-link to="add_entry">Add entry</router-link>
            <router-link to="settings">Settings</router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
