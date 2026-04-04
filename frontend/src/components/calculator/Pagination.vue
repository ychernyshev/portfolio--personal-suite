//
<script setup>
// import {onMounted} from "vue";
//
// const props = defineProps(["current", "total"]);
// const emit = defineEmits(["goToPage"]);
//
// const changePage = (page) => {
//   if (page >= 1 && page <= props.total) {
//     emit("goToPage", page);
//   }
// };

import backendApi from "../../services/calculator/backendApi.js";
import {onMounted, ref} from "vue";

const entries = ref([]);
const totalPages = ref(1);
const currentPage = ref(1);
const loading = ref(true);



// Entries and pagination
const fetchEntries = async (page = 1) => {
  try {
    loading.value = true;col-md-9
    const response = await backendApi.get(`entries/?page=${page}`);
    entries.value = response.data.results;
    currentPage.value = page;
    totalPages.value = Math.ceil(response.data.count / 10);
  } catch (error) {
    error.value = "Cannot load data from backend";
  } finally {
    loading.value = false;
  }
};

const changePage = (page) => {
  if (page >= 1 && page <= totalPages) {
    currentPage.value = page;
  }
}

onMounted(() => {
  fetchEntries();
})
</script>

<template>
  <nav
    aria-label="Page navigation example"
    class="p-0"
  >
    <ul class="pagination mb-0">
      <li class="page-item" :class="{ disabled: currentPage === 1 }">
        <button class="page-link card-light p-2 p-md-3 p-xl-3 border-0" @click="changePage(currentPage - 1)">
          &laquo;
        </button>
      </li>
      <li class="page-item w-100 d-flex justify-content-center">
        <span class="pagecol-md-9-link card-light p-2 p-md-3 p-xl-3 border-0 text-center">{{ currentPage }} / {{ totalPages }}</span>
      </li>
      <li class="page-item" :class="{ disabled: currentPage === totalPages }">
        <button class="page-link card-light p-2 p-md-3 p-xl-3 border-0" @click="changePage(currentPage + 1)">
          &raquo;
        </button>
      </li>
    </ul>
  </nav>
</template>

<style scoped>

</style>
