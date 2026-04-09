<script setup lang="ts">

</script>

<template>
  <div class="overflow-hidden mt-4">
    <div class="container-fluid col-xxl-8 hero-wrapper">
      <div class="row flex-lg-nowrap align-items-center g-5">
        <div class="order-lg-1 w-100 hero-image-block">
          <img style="clip-path: polygon(25% 0%, 100% 0%, 100% 99%, 0% 100%);" src="../../../assets/images/calc_dashboard.png" sizes="(max-width: 1080px) 100vw, 1080px" width="1160" height="568">
        </div>
        <div class="col-lg-6 col-xl-5 text-center text-lg-start pt-lg-5 mt-lg-4">
          <div class="lc-block mb-4 mb-lg-3">
            <div editable="rich">
              <h1 class="fw-bold display-3 hero-title ">
                <span class="hero-title-bg p-1">A full-stack realisation of your ideas</span>
              </h1>
            </div>
          </div>

          <div class="lc-block mb-4">
            <div editable="rich">
              <p class="rfs-8">
                <span class="hero-unit-bg hero-unit-text p-1">
                  using Django, Vue.js, Bootstrap, and other technologies
                </span>
              </p>
            </div>
          </div>

          <div class="row tech-centering">
            <div class="d-flex flex-row flex-wrap w-75 mb-4 tech-centering">
              <div class="lc-block col-2 col-lg-3 m-1"><img class="img-fluid wp-image-975" src="https://www.svgrepo.com/show/353657/django-icon.svg" width="" height="100" srcset="" sizes="" alt=""></div>
              <div class="lc-block col-2 col-lg-3 m-1"><img class="img-fluid wp-image-977" src="https://icon-icons.com/download-file?file=https%3A%2F%2Fimages.icon-icons.com%2F2415%2FPNG%2F512%2Fvuejs_original_wordmark_logo_icon_146305.png&id=146305&pack_or_individual=pack" width="" height="100" srcset="" sizes="" alt=""></div>
              <div class="lc-block col-2 col-lg-3 m-1"><img class="img-fluid wp-image-974" src="https://images.icon-icons.com/2415/PNG/512/typescript_plain_logo_icon_146316.png" width="" height="100" srcset="" sizes="" alt=""></div>
              <div class="lc-block col-2 col-lg-3 m-1"><img class="img-fluid wp-image-967" src="https://app.ibracilinks.com/assets/images/blog/posts/1605445072.png" width="" height="100" srcset="" sizes="" alt=""></div>
              <div class="lc-block col-2 col-lg-3 m-1"><img class="img-fluid wp-image-967" src="https://avatars.githubusercontent.com/u/82210087?s=200&v=4" width="" height="100" srcset="" sizes="" alt=""></div>
              <div class="lc-block col-2 col-lg-3 m-1"><img class="img-fluid wp-image-967" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPBjbXwcjW7lVBJ6AdOSDiXKrc-op8UBAw4A&s" width="" height="100" srcset="" sizes="" alt=""></div>
              <div class="lc-block col-2 col-lg-3 m-1"><img class="img-fluid wp-image-967" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpAq2i0YoBpm512rJCWDRZulLbATRWtcR3ug&s" width="" height="100" srcset="" sizes="" alt=""></div>
              <div class="lc-block col-2 col-lg-3 m-1"><img class="img-fluid wp-image-967" src="https://w7.pngwing.com/pngs/711/388/png-transparent-redis-plain-logo-icon.png" width="" height="100" srcset="" sizes="" alt=""></div>
              <div class="lc-block col-2 col-lg-3 m-1"><img class="img-fluid wp-image-967" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTePxAF_PER6j4gJ6K2y7smMwRBTKjYryflRg&s" width="" height="100" srcset="" sizes="" alt=""></div>
            </div>
          </div>
        </div>

<!--        <div class="lc-block mb-6"><a class="btn btn-primary px-4 me-md-2 btn-lg" href="#" role="button">Get it now</a>-->
<!--        </div>-->

<!--        <div class="lc-block">-->
<!--          <div editable="rich">-->
<!--            <p class="fw-bold"> Business collaboration based on trust:</p>-->
<!--          </div>-->
<!--        </div>-->

      </div><!-- /lc-block -->
    </div>
  </div>



</template>

<style scoped>
  .hero-wrapper {
    transition: background-color 0.8s ease-in-out, all 0.8s ease;
  }

  .hero-technology {
    background: var(--p-dark-1);
  }

  .hero-image-block {
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .hero-title-bg,
  .hero-unit-bg {
    color: var(--p-light-2);
    transition: .8s;
  }

  .hero-unit-text {
    font-size: clamp(1.1rem, 1vh, 1.2rem);
    font-weight: 500;
  }

  .tech-centering {
    justify-content: center;
  }

  @media (min-width: 902px) {

  }

  @media (min-width: 992px) {
    .hero-title,
    .hero-unit-text {
      color: var(--p-light-2);
    }

    .hero-technology {
      background: var(--p-light-2);
    }

    .hero-title-bg,
    .hero-unit-bg {
      background: transparent;
    }

    .tech-centering {
      justify-content: start;
    }

    .w-lg-75 {
      width: 75%;
    }
  }
</style>