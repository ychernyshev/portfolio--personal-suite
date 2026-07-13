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
  <div class="row neomorphic rounded-4 p-0">
    <div class="col-12 col-xl-12 pr-md-0">
      <div class="row">
        <div class="col-12 col-md-11">
          <div class="row input-group mx-auto">
            <div class="col-12 col-md-4 mb-4 mb-md-2 mb-md-0">
              <div class="col-12">
                <span class="input-group-text bg-transparent text-purple border-0 p-3">Group name</span>
              </div>
              <div class="col-12">
                <input type="text" v-model="groupName" class="form-control bg-transparent border-0" placeholder="Group name" aria-label="GroupName">
              </div>
            </div>

            <div class="col-12 col-md-2 mb-2 mb-md-0">
              <span class="input-group-text bg-transparent border-0 p-3">Panel Area (m<sup>2</sup>)</span>
              <input type="number" v-model="panelArea" class="form-control text-purple border-0 bg-transparent" placeholder="Panel area">
            </div>

            <div class="col-12 col-md-2 mb-2 mb-md-0">
              <span class="input-group-text bg-transparent border-0 p-3">Panel efficiency (%)</span>
              <input type="number" v-model="panelEfficiency" class="form-control text-purple border-0 bg-transparent" placeholder="Panel efficiency">
            </div>

            <div class="col-12 col-md-2 mb-2 mb-md-0">
              <span class="input-group-text bg-transparent border-0 p-3">Panel tilt angle (&deg;)</span>
              <input type="number" v-model="panelTileAngle" class="form-control text-purple border-0 bg-transparent" placeholder="Panel tilt angle">
            </div>

            <div class="col-12 col-md-2 mb-2 mb-md-0">
              <span class="input-group-text bg-transparent border-0 p-3">Azimuth (&deg;)</span>
              <input type="number" v-model="panelAzimuth" class="form-control text-purple border-0 bg-transparent" placeholder="Azimuth">
            </div>
          </div>
        </div>
        <div class="col-12 col-md-1 pl-sm-0 pr-sm-0 pr-lg-3">
          <button-comp
              type="button"
              @click="submitPanel"
              :disabled="isFormInvalid"
              title="Add"
              class="btn-blue-1 text-light w-100 h-100 border-radius-bottom-start-4 border-radius-bottom-end-4 border-radius-top-start-lg-0 border-radius-bottom-start-lg-0 border-radius-top-end-lg-4 rounded-md-4 ml-md-1 p-2 p-lg-0"
          />
        </div>
      </div>
    </div>
  </div>
  <p class="pt-3 pb-0">Added panel/panels group</p>
  <table class="table">
    <thead>
    <tr>
      <th scope="col">Group name</th>
      <th scope="col">Panel Area (m<sup>2</sup>)</th>
      <th scope="col">Panel efficiency (%)</th>
      <th scope="col">Panel tilt angle (&deg;)</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="panel in panels" :key="panel.id">
      <td>{{ panel.name }}</td>
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