<script setup lang="ts">
  import { useCalculatorStore } from "../../../store/useCalculatorStore";

  const store = useCalculatorStore()

</script>

<template>
  <h3>Power Generation Per Day</h3>
  <table class="table">
    <thead>
    <tr>
      <th scope="col">Day</th>
      <th scope="col">Av. Temp</th>
      <th scope="col">Weather</th>
      <th scope="col">Generation (W)</th>
      <th scope="col">Cost (UAH)</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="entre in store.entries" :key="entre.id">
      <th scope="row">1</th>
      <td>{{ entre.date }}</td>
      <td></td>
      <td>{{ entre.full_day_power.toFixed(2) }}</td>
      <td>{{ entre.full_day_cost.toFixed(2) }}</td>
    </tr>
    </tbody>
  </table>
</template>

<style scoped>

</style>