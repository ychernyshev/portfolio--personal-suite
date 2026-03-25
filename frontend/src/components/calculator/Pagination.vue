//
<script setup>
const props = defineProps(["current", "total"]);
const emit = defineEmits(["goToPage"]);

const changePage = (page) => {
  if (page >= 1 && page <= props.total) {
    emit("goToPage", page);
  }
};
</script>

<template>
  <nav
    aria-label="Page navigation example"
    class="mb-0"
  >
    <ul class="pagination">
      <li class="page-item" :class="{ disabled: current === 1 }">
        <button class="page-link card-light p-2 border-0" @click="changePage(current - 1)">
          &laquo;
        </button>
      </li>
      <li class="page-item w-75">
        <span class="page-link card-light p-2 border-0 text-center">{{ current }} / {{ total }}</span>
      </li>
      <li class="page-item" :class="{ disabled: current === total }">
        <button class="page-link card-light p-2 border-0" @click="changePage(current + 1)">
          &raquo;
        </button>
      </li>
    </ul>
  </nav>
</template>
