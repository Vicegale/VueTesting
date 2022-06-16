<script setup lang="ts">
import { ref, inject } from "vue";
defineProps(["item"]);

const deleteItem: any = inject('deleteItem');
</script>

<template>
  <div class="itemframe-parent">
    <div class="itemframe-header">
      <h1 class="itemname">{{ item.name }}</h1>
      <div>
        <button class="itemframe-delete" @click="deleteItem(item)">X</button>
      </div>
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
.itemframe-delete {
  background-color: red;
  border-radius: 10px;
  width: 30px;
  font-weight: 900;
  font-size: large;
  float: right;
  align-self: flex-end;
}
</style>
