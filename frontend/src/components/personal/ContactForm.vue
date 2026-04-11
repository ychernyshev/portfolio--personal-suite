<script setup lang="ts">

</script>

<template>
  <div class="offcanvas offcanvas-end my-auto height-0 offcanvas-wrapper" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
    <div class="offcanvas-body row">
      <div class="col-12 col-lg-1 p-3">
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="col-lg-5 p-3">
        <div class="d-flex flex-column">
          <span class="text-muted text-uppercase contact-unit">i`m here to help you</span>
          <p class="offcanvas-title contact-title" id="offcanvasRightLabel">
            <b class="text-primary-emphasis">Discuss</b>
            Your Project Solution Needs</p>
          <span class="text-muted mt-4">Are you looking for a programmer to realize your project ideas? Reach out to me</span>
          <div class="row mt-4">
            <div class="col-2">
              <svg xmlns="http://www.w3.org/2000/svg" width="46" height="46" fill="currentColor" class="bi bi-mailbox-flag text-primary-emphasis" viewBox="0 0 16 16">
                <path d="M10.5 8.5V3.707l.854-.853A.5.5 0 0 0 11.5 2.5v-2A.5.5 0 0 0 11 0H9.5a.5.5 0 0 0-.5.5v8zM5 7c0 .334-.164.264-.415.157C4.42 7.087 4.218 7 4 7s-.42.086-.585.157C3.164 7.264 3 7.334 3 7a1 1 0 0 1 2 0"/>
                <path d="M4 3h4v1H6.646A4 4 0 0 1 8 7v6h7V7a3 3 0 0 0-3-3V3a4 4 0 0 1 4 4v6a1 1 0 0 1-1 1H1a1 1 0 0 1-1-1V7a4 4 0 0 1 4-4m0 1a3 3 0 0 0-3 3v6h6V7a3 3 0 0 0-3-3"/>
              </svg>
            </div>
            <div class="col-10 d-flex flex-column">
              <span class="text-muted small">Email:</span>
              <span class="small">eugene_chernyshev@yahoo.com</span>
            </div>
          </div>
          <div class="row mt-4">
            <div class="col-2">
              <svg xmlns="http://www.w3.org/2000/svg" width="46" height="46" fill="currentColor" class="bi bi-telephone text-primary-emphasis" viewBox="0 0 16 16">
                <path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.6 17.6 0 0 0 4.168 6.608 17.6 17.6 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.68.68 0 0 0-.58-.122l-2.19.547a1.75 1.75 0 0 1-1.657-.459L5.482 8.062a1.75 1.75 0 0 1-.46-1.657l.548-2.19a.68.68 0 0 0-.122-.58zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.68.68 0 0 0 .178.643l2.457 2.457a.68.68 0 0 0 .644.178l2.189-.547a1.75 1.75 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.6 18.6 0 0 1-7.01-4.42 18.6 18.6 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877z"/>
              </svg>
            </div>
            <div class="col-10 d-flex flex-column">
              <span class="text-muted small">Phone:</span>
              <div class="d-flex flex-row">
                <span class="small">+38 063 227 96 70</span>
                <span class="small">+38 066 117 57 07</span>
              </div>
            </div>
          </div>
          <div class="row mt-4">
            <span class="text-muted small">Social:</span>
            <div class="col-5 d-flex flex-row justify-content-between m-0">
                <a href="https://www.linkedin.com/in/ychernyshev/" class="shadow text-primary-emphasis underline-none w-100 p-1 d-flex justify-content-around align-items-center" target="_blank">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="40" class="bi bi-linkedin media-socials text-primary-emphasis" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"></path>
                  </svg>
                  <span>/ychernyshev</span>
                </a>
            </div>
            <div class="col-5 d-flex flex-row justify-content-between m-0">
              <a href="https://github.com/ychernyshev?tab=repositories" class="shadow text-primary-emphasis underline-none w-100 p-1 d-flex justify-content-around align-items-center" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
                  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
                </svg>
                <span>/ychernyshev</span>
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-5 p-3 mx-auto">
        <div class="card border-0 shadow p-5 rounded-3">
          <form action="">
            <input class="form-control mb-3 bg-body-tertiary rounded-0" autofocus type="text" placeholder="Subject">
            <input class="form-control mb-3 bg-body-tertiary rounded-0" type="email" placeholder="Email">
            <input class="form-control mb-3 bg-body-tertiary rounded-0" type="text" placeholder="Project theme">
            <textarea class="form-control mb-3 bg-body-tertiary rounded-0" name="" placeholder="Tell me about your idea" id="" cols="30" rows="10"></textarea>
            <button type="button" class="btn btn-success border-0 shadow w-100 rounded-0">Let`s get discussion</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .offcanvas-wrapper {
    background-color: #F5F6F8;
    box-shadow: 0 0 6rem .6rem rgba(255, 255, 255, 0.4);
    border-top-left-radius: 1.5rem;
    border-bottom-left-radius: 1.5rem;
  }

  .contact-unit {
    font-size: clamp(1.1rem, 1vw, .9rem);
    font-weight: 500;
  }

  .contact-title {
    font-size: clamp(2.5rem, 1vw, 2.5rem);
    font-weight: 400;
  }

  @media (min-width: 960px) {
    .offcanvas-wrapper {
      //background-color: rgba(0, 0, 0, 0.5);
      width: 55%;
      height: 68vh;
    }

    .contact-title {
      width: 80%;
    }
  }
</style>