// SPDX-License-Identifier: AGPL-3.0-or-later
//
<script setup>
import { useCalculatorStore } from "../../../store/useCalculatorStore";
const store = useCalculatorStore();

const changePage = (page) => {
  if (page >= 1 && page <= totalPages) {
    currentPage.value = page;
  }
}
</script>

<template>
  <nav
    aria-label="Page navigation example"
    class="p-0"
  >
    <ul class="pagination mb-0">
      <li class="page-item" :class="{ disabled: store.currentPage === 1 }">
        <button class="page-link btn btn-transform card-shadow neomorphic text-purple p-md-3 p-xl-3 border-0"
                @click="store.setPage(store.currentPage - 1)">
          &laquo;
        </button>
      </li>
      <li class="page-item w-100 d-flex justify-content-center">
        <span class="pagecol-md-9-link card-light p-3 p-md-3 p-xl-3 border-0 text-center">
          {{ store.currentPage }} / {{ store.totalPages }}
        </span>
      </li>
      <li class="page-item" :class="{ disabled: store.currentPage === store.totalPages }">
        <button class="page-link btn btn-transform card-shadow neomorphic text-purple p-md-3 p-xl-3 border-0"
                @click="store.setPage(store.currentPage + 1)">
          &raquo;
        </button>
      </li>
    </ul>
  </nav>
</template>

<style scoped>

</style>
