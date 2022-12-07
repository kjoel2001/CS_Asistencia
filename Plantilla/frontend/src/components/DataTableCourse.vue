<template>
  <v-card>
    <v-card-title>
      Cursos
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>

  <v-data-table
    class="table"
    :headers="headers"
    :items="courses"
    :rows-per-page-items="[10, 25]">
    <template slot="items" slot-scope="props">
      <td class="text-xs-left">{{ props.item.cur_id }}</td>
      <td class="text-xs-left">{{ props.item.cur_name }}</td>
      <td class="text-xs-left">{{ props.item.cur_des }}</td>
      <v-row align="center" justify="space-around">
                <v-btn
                  tile
                  color="error"
                  @click="deleteCourse(props.item),snackbar = true"
                >
      <v-icon center>
        mdi-pencil
      </v-icon>
      Eliminar
    </v-btn>
    <v-snackbar
      v-model="snackbar"
      :timeout="timeout"
    >
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="blue"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-row>
  <v-row justify="center">
    <v-dialog
      v-model="editar"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          editar
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Editar Curso</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newCourse.cur_name"
                  label="Nombre del Curso"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newCourse.cur_des"
                  label="Descripcion"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="editar = false"
          >
            Cerrar
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="(updateCourse(props.item),editar = false)"
          >
            Guardar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
    </template>
  </v-data-table>

  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Agregar nuevo curso
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Agregar Curso</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newCourse.cur_name"
                  label="Nombre del Curso*"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newCourse.cur_des"
                  label="Descripcion"
                  hint="example of helper text only on focus"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Cerrar
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="(addCourse(),dialog = false)"
          >
            Guardar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    
  </v-row>
</v-card>

</template>

<script>

import axios from 'axios'
export default {
  data() {
    return {
      snackbar: false,
      text: 'Se elimino de la tabla',
      timeout: 2000,
      courses: [],
      dialog: false,
      editar: false,
      course_id:'',
      newCourse: {},
      postURL: 'http://127.0.0.1:5000',
      headers: [
      {
          text: 'Id Curso',
          value: 'cur_id',
          align: 'left',
          sortable: true
        },
        {
          text: 'Nombre Curso',
          value: 'cur_name',
          align: 'left',
          sortable: true
        },
        {
          text: 'Descripcion',
          value: 'cur_des',
          align: 'left',
          sortable: true
        }
      ]
    }
  },

  methods: {
    deleteCourse(course){ 
      this.axios.post(this.postURL + '/course/delete_course', {cur_id:course.cur_id}, this.config_request, )
      .then(res => {      
          this.courses.splice(this.courses.indexOf(course), 1);                    
      })
      .catch((error) => {      
          console.log(error)
      });                   
    },
    updateCourse(course) {
      console.log(this.newCourse);
      this.axios.post(this.postURL + '/course/update_course',{cur_id:course.cur_id,
      cur_name:this.newCourse.cur_name,cur_des:this.newCourse.cur_des},this.config_request)
    },
    addCourse(){ 
        console.log(this.newCourse.cur_name);
        console.log(this.newCourse.cur_des);  
        this.axios.post(this.postURL + '/course/create_course', this.newCourse, this.config_request)
        .then(res => {                                         
          this.courses.push(res.data);
          console.log(res.data);
        })
        this.newCourse = {}; 
        this.step = 1
    },
  },

  created(){ 
        axios.get(this.postURL + '/course/courses')
            .then((res) => { this.courses = res.data; })
            .catch((error) => { console.log(error) })
    }
  
}
</script>

<style>
  .table {
    border-radius: 3px;
    background-clip: border-box;
    border: 1px solid rgba(0, 0, 0, 0.125);
    box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.21);
    background-color: transparent;
  }
</style>
