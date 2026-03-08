<script setup></script>

<template>
    <nav class="navbar navbar-expand-lg bg-light" data-bs-theme="light">
  <div class="container-fluid p-3">
    <a class="navbar-brand bg-c-sunrise p-3 rounded-5 text-white" style="box-shadow: .5rem .5rem 1rem 0 rgba(255, 193, 7, .9)" href="{% url 'calculator:dashboard' %}">Solar Power Calculator</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarColor04">
      <div class="collapse navbar-collapse d-flex justify-content-end" id="navbarColor04">
        <div class="links weight-600 text-upper text-light">
            <a
              href="{{ url('/dashboard') }}"
              class="{{ request()->is('dashboard') ? 'text-c-primary' : '' }}"
              >Dashboard</a>
            <a
              href="{{ url('/add_entry') }}"
              class="{{ request()->is('add_entry') ? 'text-c-primary' : '' }}"
              >Add entry</a>
            <a
              href="{{ url('/settings') }}"
              class="{{ request()->is('settings') ? 'text-c-primary' : '' }}">
              Settings</a>
        </div>
    </div>
  </div>
</nav>

</template>
