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
    :items="participations"
    :rows-per-page-items="[10, 25]">
    <template slot="items" slot-scope="props">
      <td class="text-xs-left">{{ props.item.par_id }}</td>
      <td class="text-xs-left">{{ props.item.par_date }}</td>
      <td class="text-xs-left">{{ props.item.par_val }}</td>
      <td class="text-xs-left">{{ props.item.gru_id }}</td>
      <td class="text-xs-left">{{ props.item.std_id }}</td>
      <v-row align="center" justify="space-around">
                <v-btn
                  tile
                  color="error"
                  @click="deleteParticipation(props.item),snackbar = true"
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
          <span class="text-h5">Editar participacion</span>
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
                  v-model="newParticipation.par_date"
                  label="fecha"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newParticipation.par_val"
                  label="Valor"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newParticipation.gru_id"
                  label="Grupo"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newParticipation.std_id"
                  label="Id estudiante"
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
            @click="(updateParticipation(props.item),editar = false)"
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
          Agregar nuevo participacion
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Agregar participacion</span>
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
                  v-model="newParticipation.par_date"
                  label="fecha"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newParticipation.par_val"
                  label="Valor"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newParticipation.gru_id"
                  label="Grupo"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  v-model="newParticipation.std_id"
                  label="Id estudiante"
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
            @click="(addParticipation(),dialog = false)"
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
      participations: [],
      dialog: false,
      editar: false,
      course_id:'',
      newParticipation: {},
      postURL: 'http://127.0.0.1:5000',
      headers: [
        {
          text: 'Id participacion',
          value: 'par_id',
          align: 'left',
          sortable: true
        },
        {
          text: 'Fecha',
          value: 'par_date',
          align: 'left',
          sortable: true
        },
        {
          text: 'participacion',
          value: 'par_val',
          align: 'left',
          sortable: true
        },
        {
          text: 'grupo',
          value: 'gru_id',
          align: 'left',
          sortable: true
        },
        {
          text: 'id estudiante',
          value: 'std_id',
          align: 'left',
          sortable: true
        }
      ]
    }
  },

  methods: {
    deleteParticipation(participation){ 
      this.axios.post(this.postURL + '/participation/delete_participation', {par_id:participation.par_id}, this.config_request, )
      .then(res => {      
          this.participations.splice(this.participations.indexOf(participation), 1);                    
      })
      .catch((error) => {      
          console.log(error)
      });                   
    },
    updateParticipation(participation) {
      this.axios.post(this.postURL + '/participation/update_participation',{par_id:participation.par_id,
      par_date:this.newParticipation.par_date,par_val:this.newParticipation.par_val,gru_id:this.newParticipation.gru_id,
      std_id:this.newParticipation.std_id},this.config_request)
    },
    addParticipation(){  
        this.axios.post(this.postURL + '/participation/create_participation', this.newParticipation, this.config_request)
        .then(res => {                                         
          this.participations.push(res.data);
          console.log(res.data);
        })
        this.newParticipation = {}; 
        this.step = 1
    },
  },

  created(){ 
        axios.get(this.postURL + '/participation/participations')
            .then((res) => { this.participations = res.data; })
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
