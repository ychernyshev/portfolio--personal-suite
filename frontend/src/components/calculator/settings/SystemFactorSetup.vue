<script setup>
  import ButtonComp from "@/components/personal/ButtonComp.vue";
  import {useUserAccountStore} from "../../../../store/useUserAccountStore.js";
  import {storeToRefs} from "pinia";
  import {onMounted} from "vue";

  const user_profile = useUserAccountStore();
  const { currentUser, error, loading } = storeToRefs(user_profile);

  const loadProfile = async () => {
    try {
      await user_profile.fetchUserProfile();
    } catch (err) {}
  };

  onMounted(() => {
    loadProfile();
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
          <input type="text" class="form-control" placeholder="Group name" aria-label="GroupName">
        </div>

        <div class="col-2">
          <span class="input-group-text">Username</span>
          <input v-if="currentUser"
                 type="text"
                 class="form-control"
                 aria-label="Username"
                 v-model="currentUser"
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
          <input type="text" class="form-control" placeholder="Panel area" aria-label="PanelArea">
        </div>

        <div class="col-2">
          <span class="input-group-text">Panel efficiency (%)</span>
          <input type="text" class="form-control" placeholder="Panel efficiency" aria-label="PanelEfficiency">
        </div>

        <div class="col-2">
          <span class="input-group-text">Panel tilt angle (&deg;)</span>
          <input type="text" class="form-control" placeholder="Panel tilt angle" aria-label="PanelTileAngle">
        </div>

        <div class="col-2">
          <span class="input-group-text">Azimuth (&deg;)</span>
          <input type="text" class="form-control" placeholder="Azimuth" aria-label="Azimuth">
        </div>
      </div>
    </div>
    <div class="col-12 col-xl-1 pl-0">
      <button-comp :disabled="!userProfile" title="Add" class="btn btn-primary w-100 h-100"/>
    </div>
  </div>
  <p class="pt-3 pb-1 border-bottom">Added panel/panels group</p>
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
    <tr>
      <td>1</td>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
      <td>@mdo</td>
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