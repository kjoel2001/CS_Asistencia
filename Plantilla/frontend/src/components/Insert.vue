<template>
        
</template>

<script>
  export default {
    data () {
      return {
        courses: [],
        newCourse: {},
        step: 0,
        postURL: 'http://127.0.0.1:5000',
        config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
        },  
        valid: true,
        name: '',
        des: '',
        checkbox: false,
        date: new Date().toISOString().substr(0, 10)
      }
    },
    methods: {
      addCourse(){ 
        if (this.$refs.form.validate()) {
          console.log(this.newCourse.cur_name);
          console.log(this.newCourse.cur_des);
          this.axios.post(this.postURL + '/course/create_course', this.newCourse, this.config_request)
          .then(res => {                                         
            this.courses.push(res.data);
            console.log(res.data);
          })
          .catch((error) => {
            console.log(error)
          });
          console.log("fin");
          this.newCourse = {}; 
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
