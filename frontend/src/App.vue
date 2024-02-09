<script setup>
/**
 * @file App.vue
 * @description This is the main Vue application entry file. It imports and utilizes the HelloWorld component to demonstrate component integration within a Vue application.
 * @imports {HelloWorld} from './components/HelloWorld.vue' - Imports HelloWorld Component from the components directory to be used within this Vue application instance.
 */
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <!-- Main application template. Contains links to external resources and integrates the HelloWorld component. -->
  <div>
    <!-- External link to Vite documentation. -->
    <a href="https://vitejs.dev" target="_blank" rel="noopener noreferrer">
      <!-- Vite logo as an indicator of the technology stack used. -->
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <!-- External link to Vue.js documentation. -->
    <a href="https://vuejs.org/" target="_blank" rel="noopener noreferrer">
      <!-- Vue.js logo as an indicator of the technology stack used. -->
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <!-- HelloWorld component integration with a prop passed for demonstration purposes. -->
  <HelloWorld msg="DC Universe" />
</template>

<style scoped>
/* Scoped styles for the App.vue component. Defines styles for logos and their hover states. */
.logo {
  height: 4em; /* Sets the height of the logo images. */
  padding: 1.5em; /* Adds padding around the logo images. */
  will-change: filter; /* Optimizes animations by informing the browser of changes to the filter property. */
  transition: filter 300ms; /* Smooth transition for filter changes. */
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa); /* Adds a drop shadow effect on hover for the generic logo. */
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa); /* Adds a drop shadow effect on hover specifically for the Vue logo. */
}
</style>
