<script setup lang="ts">
import { reactive, ref, inject } from "vue";
import axios from "axios";
const item = reactive({
  name: "",
  stats: [],
});

const { addItem } = inject("addItem");

const newStat = ref("");

function createItem() {
  if (item.name.length > 0) {
    axios.post("http://localhost:5000/items", {
      name: item.name,
      stats: item.stats,
    });
  }
  addItem({
    name: item.name,
    stats: item.stats,
  });
  item.name = "";
  item.stats = [];
}

function addStat() {
  item.stats.push(newStat.value);
  newStat.value = "";
}

function removeStat(stat: string) {
  item.stats = item.stats.filter((t) => t !== stat);
}
</script>

<template>
  <h1>Create a new Item</h1>
  <div>
    <div>
      <h2>Item Name</h2>
      <input type="text" v-model="item.name" placeholder="Item Name" />
    </div>
    <div>
      <h2>Item Stats</h2>
      <div v-for="stat in item.stats" class="newStat">
        <p>{{ stat }}</p>
        <button @click="removeStat(stat)">x</button>
      </div>

      <div>
        <input type="text" v-model="newStat" placeholder="Item Stats" />
        <button @click="addStat">+</button>
      </div>
    </div>
    <button @click="createItem">Create</button>
  </div>
</template>

<style>
.newStat {
  display: flex;
  flex-direction: row;
}
</style>
