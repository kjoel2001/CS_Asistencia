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
    :items="schedulles"
    :rows-per-page-items="[10, 25]">
    <template slot="items" slot-scope="props">
      <td class="text-xs-left">{{ props.item.sch_id }}</td>
      <td class="text-xs-left">{{ props.item.sch_begin }}</td>
      <td class="text-xs-left">{{ props.item.sch_end }}</td>
      <td class="text-xs-left">{{ props.item.sch_day }}</td>
      <td class="text-xs-left">{{ props.item.gru_id }}</td>
      <v-row align="center" justify="space-around">
                <v-btn
                  tile
                  color="error"
                  @click="deleteSchedulle(props.item),snackbar = true"
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
          <span class="text-h5">Editar Horario</span>
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
                  v-model="newSchedulle.sch_begin"
                  label="Hora inicio"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newSchedulle.sch_end"
                  label="Hora final"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newSchedulle.sch_day"
                  label="Dia"
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
            @click="(updateSchedulle(props.item),editar = false)"
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
          Agregar nuevo horario
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Agregar Horaio</span>
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
                  v-model="newSchedulle.sch_begin"
                  label="Hora inicio"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newSchedulle.sch_end"
                  label="Hora final"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newSchedulle.sch_day"
                  label="Dia"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newSchedulle.gru_id"
                  label="Grupo"
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
            @click="(addSchedulle(),dialog = false)"
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
      schedulles: [],
      dialog: false,
      editar: false,
      course_id:'',
      newSchedulle: {},
      postURL: 'http://127.0.0.1:5000',
      
      headers: [
      {
          text: 'Id',
          value: 'sch_id',
          align: 'left',
          sortable: true
        },
      {
          text: 'Inicio',
          value: 'sch_begin',
          align: 'left',
          sortable: true
        },
        {
          text: 'Final',
          value: 'sch_end',
          align: 'left',
          sortable: true
        },
        {
          text: 'dia',
          value: 'sch_day',
          align: 'left',
          sortable: true
        },
        {
          text: 'grupo',
          value: 'gru_id',
          align: 'left',
          sortable: true
        }
      ]
    }
  },

  methods: {
    deleteSchedulle(schedulle){ 
      this.axios.post(this.postURL + '/schedulle/delete_schedulle', {sch_id:schedulle.sch_id}, this.config_request, )
      .then(res => {      
          this.schedulles.splice(this.schedulles.indexOf(schedulle), 1);                    
      })
      .catch((error) => {      
          console.log(error)
      });                   
    },
    updateSchedulle(schedulle) {
      console.log(this.newSchedulle);
      this.axios.post(this.postURL + '/schedulle/update_schedulle',{sch_id:schedulle.sch_id,
        sch_begin:this.newSchedulle.sch_begin,sch_end:this.newSchedulle.sch_end,
        sch_day:this.newSchedulle.sch_day},this.config_request)
    },
    addSchedulle(){  
        this.axios.post(this.postURL + '/schedulle/create_schedulle', this.newSchedulle, this.config_request)
        .then(res => {                                         
          this.schedulles.push(res.data);
          console.log(res.data);
        })
        this.newSchedulle = {}; 
        this.step = 1
    },
  },

  created(){ 
        axios.get(this.postURL + '/schedulle/schedulles')
            .then((res) => { this.schedulles = res.data; })
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
