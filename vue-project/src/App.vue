<script setup lang="ts">
import ItemDisplay from "./components/ItemDisplay.vue";
import Counter from "./components/Counter.vue";
import axios from "axios";
import { onMounted, provide } from "vue";
import { reactive } from "vue";
import ItemCreate from "./components/ItemCreate.vue";

const state = reactive({ items: [] as any[] });

onMounted(() => {
  axios.get("http://localhost:5000/items").then((response) => {
    state.items = response.data;
  });
});

provide("addItem", addItem);

function addItem(item: any) {
  state.items.push(item);
}
</script>

<template>
  <header>
    <div class="navbar">
      <h1>Welcome to Your Vue.js App</h1>
    </div>
  </header>

  <main>
    <ItemCreate />
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
