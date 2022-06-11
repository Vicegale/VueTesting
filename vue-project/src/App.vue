<script setup lang="ts">
import ItemDisplay from "./components/ItemDisplay.vue";
import Counter from "./components/Counter.vue";
import axios from "axios";
import { onMounted } from "vue";
import {reactive} from "vue";

const state = reactive({'items': []});

onMounted(() => {
  axios.get('http://localhost:5000/items').then(response => {
    state.items = response.data;
  });
});

/*
const items = [
  {
    name: "Boots of Haste",
    stats: ["+30% movement speed", "+15% attack speed"],
  },
  {
    name: "Blasting Wand",
    stats: [
      "+10% increased Fire Damage",
      "+20% attack speed",
      "+20% critical strike chance",
    ],
  },
  {
    name: "Dagger",
    stats: ["+20% attack speed", "+20% critical strike chance"],
  },
];*/
</script>

<template>
  <header>
    <div class="navbar">
      <h1>Welcome to Your Vue.js App</h1>
    </div>
  </header>

  <main>
    <ItemDisplay v-for="i in state.items" :item="i"></ItemDisplay>
  </main>
</template>

<style>
@import "./assets/base.css";

header {
  background-color: #eee;
  padding: 20px;
  text-align: center;
}

.navbar {
  background-color: #eee;
  padding: 20px;
  text-align: center;
}

.navbar-button {
  background-color: #eee;
  padding: 20px;
  text-align: center;
}
</style>
