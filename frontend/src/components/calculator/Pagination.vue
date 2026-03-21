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
    class="d-flex justify-content-center mt-2"
  >
    <ul class="pagination">
      <ul class="pagination">
        <li class="page-item" :class="{ disabled: current === 1 }">
          <button class="page-link" @click="changePage(current - 1)">
            &laquo;
          </button>
        </li>
        <li class="page-item">
          <span class="page-link">{{ current }} / {{ total }}</span>
        </li>
        <li class="page-item" :class="{ disabled: current === total }">
          <button class="page-link" @click="changePage(current + 1)">
            &raquo;
          </button>
        </li>
      </ul>
    </ul>
  </nav>
</template>
