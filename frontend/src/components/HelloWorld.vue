<script setup>
// NOTES
// The <script setup> syntax is a new feature in
// Vue 3 that allows us to write the component's setup options in a more concise manner
// It automatically imports necessary features from Vue and provides a more streamlined syntax for defining props, reactive data, and other composition API features
// Previously, we would have to manually
// import these features and define them in the setup() function
// for tables in html, we use the <table> tag to create a table, <tr> tag to define a row,
// <th> tag to define a header cell, and <td> tag to define a data cell
/**
 * @file HelloWorld.vue
 * @description This component is designed to fetch and display data in a table format. It utilizes Vue 3's <script setup> syntax for a more concise and readable code structure. The component fetches data from an API on mount and displays it along with a message passed as a prop.
 */

// Importing Vue composition API features and fetchData method
import { ref, onMounted } from "vue";
import { fetchData } from "../fetch";

/**
 * @prop {String} msg - The message to be displayed at the top of the component.
 */
defineProps({
  msg: String,
});

/**
 * @type {Ref<Array>} data - A reactive reference to the data array fetched from the API.
 */
const data = ref([]);

/**
 * @type {Ref<Boolean>} showError - A reactive reference to a boolean value indicating whether an error occurred while fetching data.
 */
const showError = ref(false);

/**
 * Fetches data from an API on component mount and updates the `data` ref.
 */
onMounted(async () => {
  // Simulating an API request with a delay
  try {
    // Fetching data from the API
    const response = await fetchData();
    // Updating the data with the response from the API
    showError.value = false;
    data.value = response;
  } catch (error) {
    console.error("Error fetching data:", error);
    showError.value = true;
  }

});
</script>

<template>
  <div>
    <!-- The template section defines the component's markup. -->

    <!-- Displaying a message passed as a prop to the component -->
    <h1>{{ msg }}</h1>
    <!-- Conditional rendering based on the showError ref -->
    <p v-if="showError">An error occurred while fetching data.</p>
    <!-- Data table for displaying fetched data -->
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
          <td>{{ item.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
/* Scoped styles for HelloWorld component */
h1 {
  color: #42b983; /* Header color set to green */
}

table {
  width: 100%; /* Table width set to 100% of the container */
  border-collapse: collapse; /* Border collapse to remove default spacing between cells */
}
th,
td {
  border: 1px solid #ddd; /* Border for table cells */
  padding: 8px; /* Padding for table cells */
  text-align: left; /* Text alignment for table cells */
}
</style>

