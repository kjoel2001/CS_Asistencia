<template>
    <v-row justify="center">
        <v-card-title>  
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Buscar"
          single-line
          hide-details
        ></v-text-field>
        <v-spacer></v-spacer>
        <v-row align="center" justify="space-around">
        <v-btn
          tile
          color="primary"
          @click="show_dialog=true"
        >
            <v-icon center>
                mdi-pencil
                </v-icon>
            Agregar docente
        </v-btn>
      </v-row>
      </v-card-title>
        <v-data-table
        class="user"
        :headers="headers"
        :items="users" 
        :rows-per-page-items="[10, 25]">
        <template slot="items" slot-scope="props">
            <td class="text-xs-left">{{ props.item.usr_dni }}</td>
            <td class="text-xs-left">{{ props.item.usr_name }}</td>
            <td class="text-xs-left">{{ props.item.usr_last_name }}</td>
            <td class="text-xs-left">{{ props.item.usr_dob }}</td>
            <td class="text-xs-left">{{ props.item.usr_email }}</td>
            <td class="text-xs-left">{{ props.item.tea_cat }}</td>
            <td class="text-xs-left">{{ props.item.tea_type }}</td>
            <v-row align="center" justify="space-around">
                <v-btn
                  tile
                  color="error"
                  @click="deleteTeacher(props.item)"
                >
                    <v-icon center>
                        mdi-pencil
                    </v-icon>
                    Eliminar
                  </v-btn>
                  <v-btn
                  tile
                  color="success"
                  @click="updateTeacher(props.item)"
                >
                    <v-icon center>
                        mdi-pencil
                    </v-icon>
                    Editar
                  </v-btn>
            </v-row>
        </template>
    </v-data-table>   
        <v-row justify="center">
            <v-dialog
                v-model="show_dialog"
                persistent
                max-width="700px"
            >
        <v-card>
          <v-card-title>
            <h2 class="text-h5" justify="center">Datos del Docente</h2>
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
                    v-model="newUser.usr_name"
                    label="Nombre*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    v-model="newUser.usr_last_name"
                    label="Apellidos*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                </v-col>
                </v-row>
            </v-container>
            <small>*Indica campo requerido</small>
          </v-card-text>
          <v-card-actions>
            
            <v-spacer></v-spacer>
            <v-btn
              color="blue darken-1"
              text
              @click="show_dialog = false"
            >
              Cerrar
            </v-btn>
            <v-btn
              color="blue darken-1"
              text
              @click="addUserTeacher"
            >
              Guardar
                </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-row>    
        
    </v-row>
</template>

<script>  
  export default {
    data() {
      return {
        filePhoto: null,
        date: null,
        menu: false,
        show_dialog: false,
        update_index: -1,
        teacher_id: '',
        user_id: '',
        teachers: [],
        users: [],
        newUser:{},
        newTeacher:{},
        postURL: 'http://127.0.0.1:5000',
        config_request: {
                  'x-access-token': 'token-value',
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*'
                  
        },          
        headers: [
          {
                text: 'DNI',
                align: 'start',
                sortable: true,
                value: 'usr_dni',
                },
                { text: 'Nombre', value: 'usr_name' },
                { text: 'Apellido', value: 'usr_last_name' },
                { text: 'Fecha de nacimiento', value: 'usr_dob' },
                { text: 'Correo electronico', value: 'usr_email' },
                { text: 'Categoria', value: 'tea_cat' },
                { text: 'Tipo', value: 'tea_type' },
          ]
      }
    },
    watch: {
      menu (val) {
        val && setTimeout(() => (this.activePicker = 'YEAR'))
      },
    },
    methods: {
        save (date) {
            this.$refs.menu.save(date)
        },
     
        previewFiles: function(files) {
            console.log(files)
        },
        addUserTeacher(){ 
            this.newUser['ust_id'] = 1;
            console.log(this.filePhoto)
            this.axios.post(this.postURL + '/user/create_user', this.file, this.newUser, this.config_request)
            .then(res => {                                         
              this.users.push(res.data);
              console.log(res.data);
            })
            .catch((error) => {
              console.log(error)
            });
            console.log("fin");
            this.newUser = {}; 

            this.axios.post(this.postURL + '/teacher/create_teacher', {usr_id:this.newUser.usr_id},
                                                                      {tea_type:this.newTeacher.tea_type},
                                                                      {tea_cat:newTeacher.tea_cat},
                                                                      this.config_request)
            .then(res => {                                         
            this.teachers.push(res.data);
            console.log(res.data);
            })
            .catch((error) => {
              console.log(error)
            });
            console.log("fin");
            this.newTeacher = {}; 

            this.show_dialog=false;
          
      },
      deleteTeacher(teacher) {
            this.axios.post(this.postURL + '/user/delete_user', {usr_id:teacher.usr_id}, this.config_request, )
                    .then(res => {      
                        this.courses.splice(this.users.indexOf(teacher), 1);                    
                    })
                    .catch((error) => {      
                        console.log(error)
                    });  
            this.axios.post(this.postURL + '/teacher/delete_teacher', {tea_id:teacher.tea_id}, this.config_request, )
                    .then(res => {      
                        console.log("Docente eliminado")                  
                    })
                    .catch((error) => {      
                        console.log(error)
                    });  
        },
        addRow(){
          if (this.update_index > -1) {
            this.editTeacher()
          } else {
            this.addUserTeacher();
          }
        },
        updateTeacher(teacher) {
            this.show_dialog=true;
            this.update_index = this.users.indexOf(teacher)
            this.teacher_id = teacher.usr_id
            this.newUser.usr_name      = teacher.usr_name
            this.newUser.usr_last_name = teacher.usr_last_name
            this.newUser.usr_email     = teacher.usr_email
            this.newUser.usr_dob       = teacher.usr_dob
            this.newUser.usr_pass      = teacher.usr_pass
            //this.teacher.usr_name = teacher.usr_photo
            //this.teacher.usr_name = teacher.tea_name
            //this.teacher.usr_name = teacher.tea_name
        },
        editTeacher() {
          this.axios.post(this.postURL + '/user/update_user', this.newUser, this.config_request)
            .then(res => {                                         
              this.users.push(res.data);
              console.log(res.data);
            })
            .catch((error) => {
              console.log(error)
            });
            console.log("fin");
            this.newUser = {}; 

            this.axios.post(this.postURL + '/teacher/create_teacher', {usr_id:this.teacher_id},
                                                                      {tea_type:this.newTeacher.tea_type},
                                                                      {tea_cat:newTeacher.tea_cat},
                                                                      this.config_request)
            .then(res => {                                         
            this.teachers.push(res.data);
            console.log(res.data);
            })
            .catch((error) => {
              console.log(error)
            });
            console.log("fin");
            this.newTeacher = {}; 

            this.show_dialog=false;
        }
    },
    created() {
      this.axios.get(this.postURL + '/user/teachers')
              .then((res) => { this.users = res.data; })
              .catch((error) => { console.log(error) })
      },
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
  