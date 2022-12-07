<template>
    <v-container fluid grid-list-xl>
        <v-layout row wrap>
          <DataTableTeacher/>
        </v-layout>
    </v-container>
</template>
  
<script>
    import DataTableTeacher from '../components/DataTableTeacher.vue';
    export default {
        data() {
            return {
                lorem: `Lorem ipsum dolor sit amet, mel at clita quando.`
        };
    },
    
    components: { DataTableTeacher }
}
</script>
  
<style>
  
</style>