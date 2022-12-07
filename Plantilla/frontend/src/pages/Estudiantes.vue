<template>
    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        
          <DataTableStudent/>
        
      </v-layout>
    </v-container>
  </template>
  
  <script>
import DataTableStudent from '../components/DataTableStudent.vue';



  export default {
    data() {
        return {
            lorem: `Lorem ipsum dolor sit amet, mel at clita quando.`
        };
    },
    components: { DataTableStudent }
}
  </script>
  
  <style>
  
  </style>