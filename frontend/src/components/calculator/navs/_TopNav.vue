<script setup>
</script>

<template>
  <header class="header row">
    <div class="col-xxl-3 col-xs-12 col-sm-12 col-md-6 logo-container">
      <div class="logo">Solar Power Calculator</div>
    </div>
    <div class="col-xxl-8 col-xs-12 col-sm-12 col-md-6">
      <nav class="nav-links header-links my-md-auto">
        <div class="d-flex flex-row">
          <a href="https://github.com/ychernyshev/Solar-Power-Calculator"
             target="_blank" class="nav-item my-auto text-primary d-flex align-items-center">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-github mr-1"
                viewBox="0 0 16 16"
            >
              <path
                  d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"
              />
            </svg>
            Source code
          </a>
          <a href="#" class="nav-item my-auto fw-bold text-success d-flex align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-envelope-fill mr-1" viewBox="0 0 16 16">
              <path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/>
            </svg>
            Contact me
          </a>
        </div>
        <div class="card border-0 neomorphic text-purple text-center w-50 align-items-center d-none d-xl-block">
          Developed with Django & Vue 3
        </div>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  grid-area: header;
  margin-bottom: 1.4rem;
}

.header-links {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: center;
  align-items: center;
}

.logo-container {
  display: flex;
  justify-content: center;
}

.logo {
  width: 80%;
  padding: 1rem 2rem 1rem;
  text-align: center;
  background: linear-gradient(var(--sunrise-yelow), var(--sunset-yelow));
  border-radius: 3.3rem;
  color: var(--shadow-light);
  font-weight: 300;
  font-size: 1.2rem;
  box-shadow: 0.5rem 0.5rem 1.5rem 0 var(--sunset-yelow);
}

@media (min-width: 1200px) {
  .logo-container {
    justify-content: start;
  }

  .logo {
    width: 33%;
  }

  .header-links {
    justify-content: space-between;
  }
}
@media (min-width: 1400px) {}
</style>