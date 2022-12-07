<template>
        <v-form ref="form" v-model="valid" lazy-validation>
          <h2> Agregar Nuevo Horario </h2>
          <v-text-field
            v-model="newSchedulle.sch_begin"
            label="Hora empieza"
          ></v-text-field>
          <v-text-field
            v-model="newSchedulle.sch_end"
            label="Hora termina"
          ></v-text-field>
          <v-text-field
            v-model="newSchedulle.sch_day"
            label="Dia"
          ></v-text-field>
          <v-btn :disabled="!valid"
            @click="addSchedulle">
            Enviar
          </v-btn>
          <v-btn @click.native="clear">Limpiar</v-btn>
        </v-form>
</template>

<script>
  export default {
    data () {
      return {
        schedulles: [],
        newSchedulle: {},
        step: 0,
        postURL: 'http://127.0.0.1:5000',
        config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
        },  
        valid: true,
        checkbox: false,
        date: new Date().toISOString().substr(0, 10)
      }
    },
    methods: {
      addSchedulle(){ 
        if (this.$refs.form.validate()) {
          this.axios.post(this.postURL + '/schedulle/create_schedulle', this.newSchedulle, this.config_request)
          .then(res => {                                         
            this.schedulles.push(res.data);
            console.log(res.data);
          })
          .catch((error) => {
            console.log(error)
          });
          console.log("fin");
          this.newSchedulle = {}; 
        }
        this.step = 1
      },
      clear () {
        this.$refs.form.reset()
      },
    }
  }
</script>

<style>
</style>
