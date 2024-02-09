<script setup>
// NOTES
// The <script setup> syntax is a new feature in 
// Vue 3 that allows us to write the component's setup options in a more concise manner
// It automatically imports necessary features from Vue and provides a more streamlined syntax for defining props, reactive data, and other composition API features
// Previously, we would have to manually 
// import these features and define them in the setup() function
// for tables in html, we use the <table> tag to create a table, <tr> tag to define a row, 
// <th> tag to define a header cell, and <td> tag to define a data cell

// Importing necessary Vue composition API feature
import { ref, onMounted } from 'vue'
import { fetchData } from '../fetch';


// Defining component props
// msg prop is used to display a message at the top of the component
defineProps({
  msg: String,
})
const data = ref([])

// Fetching data from an API
onMounted(async () => {
  // Simulating an API request with a delay
  const response = await fetchData()
  // Updating the data with the response from the API
  data.value = response
})


</script>

<template>
  <!-- The template section is used to define the component's markup -->

  <!-- Displaying a message passed as a prop to the component -->
  <h1>{{ msg }}</h1>
  <!-- Data table for displaying superhero characters -->
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Text</th>
      </tr>
    </thead>
    <tbody>
      <!-- Dynamically rendering rows based on the data array -->
      <tr v-for="item in data" :key="item.ID">
        <td>{{ item.id }}</td>
        <td>{{ item.hero }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
/* Scoped styles for HelloWorld component */
h1 {
  color: #42b983; /* Header color set to green */
}
.read-the-docs {
  color: #888; /* Placeholder style for demonstration purposes */
}
table {
  width: 100%; /* Table width set to 100% of the container */
  border-collapse: collapse;  /* Border collapse to remove default spacing between cells */
}
th, td {
  border: 1px solid #ddd; /* Border for table cells */
  padding: 8px; /* Padding for table cells */
  text-align: left; /* Text alignment for table cells */
}
</style>


