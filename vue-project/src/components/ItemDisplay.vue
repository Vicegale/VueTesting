<script setup lang="ts">
import { ref } from "vue";
defineProps(["item"]);
</script>

<template>
  <div class="itemframe-parent">
    <div class="itemframe-header">
      <h1 class="itemname">{{ item.name }}</h1>
    </div>
    <div class="itemframe-body">
      <ul class="stat" v-for="stat in item.stats">
        {{
          stat
        }}
      </ul>
    </div>
  </div>
</template>

<style>
.itemframe-parent {
  display: flex;
  flex-direction: column;
  /*justify-content: center;*/
  /*set rounded border with black bg*/
  border-radius: 10px;
  background-color: #000000;
  /*set margins*/
  margin: 30px;
  height: 30%;
  border-color: green;
}
.itemframe-header {
  display: flex;
  flex-direction: row;
  /*justify-content: center;*/
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  background-color: darkslategray;
  border-color: green;
}
.itemframe-body {
  display: flex;
  flex-direction: column;
  /*justify-content: center;*/
  height: 100%;
  border-color: green;
}
.itemname {
  font-size: 1.5em;
  color: white;
  margin-left: 10px;
  font-family: "Courier New", Courier, monospace;
}
.stat {
  font-size: 1em;
  color: white;
  margin-left: 10px;
  font-family: "Courier New", Courier, monospace;
}
</style>
