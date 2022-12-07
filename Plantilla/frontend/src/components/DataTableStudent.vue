<template>
    <v-data-table
        class="user"
        :headers="headers"
        :items="users, students" 
        :rows-per-page-items="[10, 25]">
        <template slot="items" slot-scope="props">
          <td class="text-xs-left">{{ props.item.usr_dni }}</td>
          <td class="text-xs-left">{{ props.item.usr_name }}</td>
          <td class="text-xs-left">{{ props.item.usr_last_name }}</td>
          <td class="text-xs-left">{{ props.item.usr_dob }}</td>
          <td class="text-xs-left">{{ props.item.usr_email }}</td>
          <td class="text-xs-left">{{ props.item.std_year }}</td>
          <td class="text-xs-left">{{ props.item.std_regular }}</td>
          <v-row align="center" justify="space-around">
      </v-row>
        </template>
      </v-data-table>
</template>
      
    <script>
      export default {
      data() {
        return {
          users: [],
          students: [],
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
                      { text: 'Año de ingreso', value: 'std_year' },
                      { text: 'Regular', value: 'std_regular' }
          ]
        }
      },
    
        methods: {
            deleteStudent(student){                 
                this.axios.post(this.postURL + '/course/delete_course', {cur_id:student.cur_id}, this.config_request, )
                    .then(res => {      
                        this.courses.splice(this.courses.indexOf(course), 1);                    
                    })
                    .catch((error) => {      
                        console.log(error)
                    });  
            }
        },
        created() {
            var dni = [];
            this.axios.get(this.postURL + '/user/students')
                .then((res) => { 
                   this.users = res.data;
                   for (const i in res.data) {
                        console.log((res.data[i].usr_id))
                        dni.push((res.data[i].usr_dni))
                   }
                })
                .catch((error) => { console.log(error) });

            this.axios.get(this.postURL + '/student/students')
                .then((res) => { 
                    this.students = res.data; })
                .catch((error) => { console.log(error) });
        }
    }
    </script>