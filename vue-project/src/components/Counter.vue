<script setup lang="ts">
//import ref
import { ref } from "vue";

//create a ref counter and its increment and decrement functions
const counter = ref(0);
const increment = () => {
  counter.value++;
};
const decrement = () => {
  counter.value--;
};
</script>

<template>
  <!--display a counter inside a button-->
  <div class="navbar-button">
    <button @click="increment">+</button>
    <button @click="decrement">-</button>
    <h1>{{ counter }}</h1>
  </div>
</template>

<style></style>
