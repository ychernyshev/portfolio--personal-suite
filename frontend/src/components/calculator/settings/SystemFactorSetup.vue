<script setup>
import ButtonComp from "@/components/personal/ButtonComp.vue";
import {useUserAccountStore} from "../../../../store/useUserAccountStore.js";
import {storeToRefs} from "pinia";
import {computed, onMounted, ref} from "vue";
import {useCalculatorStore} from "../../../../store/useCalculatorStore.js";

const user_profile = useUserAccountStore();
const calculatorStore = useCalculatorStore();

const {currentUser, error, loading} = storeToRefs(user_profile);
const { panels } = storeToRefs(calculatorStore);
const groupName = ref('');
const panelArea = ref(0.0);
const panelEfficiency = ref(0.0);
const panelTileAngle = ref(0.0);
const panelAzimuth = ref(0.0);

const isFormInvalid = computed(() => {
  return groupName.value === '' || !currentUser || panelArea.value <= 0 || panelEfficiency.value <= 0 || panelTileAngle.value <= 0 || panelAzimuth.value <= 0;
});

const loadProfile = async () => {
  try {
    await user_profile.fetchUserProfile();
  } catch (err) {
  }
};

const submitPanel = async () => {
  const data = {
    name: groupName.value,
    area: panelArea.value,
    efficiency: panelEfficiency.value,
    angle: panelTileAngle.value,
    azimuth: panelAzimuth.value
  };

  try {
    await calculatorStore.addPanel(data);
    alert("Панель успішно додана!");
  } catch (e) {
    alert("Помилка при збереженні");
  }
};

onMounted(() => {
  loadProfile();
  calculatorStore.fetchPanels();
});
</script>

<template>
  <label class="title text-purple">Panel(s) system factor</label>
  <p class="pb-1 border-bottom">New panel/panels group</p>
  <div class="row">
    <div class="col-12 col-xl-11 pr-0">
      <div class="row input-group">
        <div class="col-2">
          <span class="input-group-text">Group name</span>
          <input type="text" v-model="groupName" class="form-control" placeholder="Group name" aria-label="GroupName">
        </div>

        <div class="col-2">
          <span class="input-group-text">Username</span>
          <input v-if="currentUser"
                 type="text"
                 class="form-control"
                 aria-label="Username"
                 :value="currentUser"
                 disabled>
          <input v-else
                 type="text"
                 class="form-control"
                 aria-label="Username"
                 placeholder="You didn't log in"
                 disabled
          >
        </div>

        <div class="col-2">
          <span class="input-group-text">Panel Area (m<sup>2</sup>)</span>
          <input type="number" v-model="panelArea" class="form-control" placeholder="Panel area">
        </div>

        <div class="col-2">
          <span class="input-group-text">Panel efficiency (%)</span>
          <input type="number" v-model="panelEfficiency" class="form-control" placeholder="Panel efficiency">
        </div>

        <div class="col-2">
          <span class="input-group-text">Panel tilt angle (&deg;)</span>
          <input type="number" v-model="panelTileAngle" class="form-control" placeholder="Panel tilt angle">
        </div>

        <div class="col-2">
          <span class="input-group-text">Azimuth (&deg;)</span>
          <input type="number" v-model="panelAzimuth" class="form-control" placeholder="Azimuth">
        </div>
      </div>
    </div>
    <div class="col-12 col-xl-1 pl-0">
      <button-comp
          @click="submitPanel"
          :disabled="isFormInvalid"
          title="Add"
          class="btn btn-primary w-100 h-100"
      />
    </div>
  </div>
  <p class="pt-3 pb-0">Added panel/panels group</p>
  <table class="table">
    <thead>
    <tr>
      <th scope="col">Group name</th>
      <th scope="col">Username</th>
      <th scope="col">Panel Area (m<sup>2</sup>)</th>
      <th scope="col">Panel efficiency (%)</th>
      <th scope="col">Panel tilt angle (&deg;)</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="panel in panels" :key="panel.id">
      <td>{{ panel.name }}</td>
      <td>{{ currentUser }}</td>
      <td>{{ panel.area }}</td>
      <td>{{ panel.efficiency * 100 }}%</td>
      <td>{{ panel.angle }}</td>
    </tr>
    </tbody>
  </table>
</template>

<style scoped>
.title {
  font-size: clamp(1rem, 2vw, 1.1rem);
  font-weight: 400;
}

.label-text {
  font-size: 0.75rem;
  font-weight: 300;
}
</style>