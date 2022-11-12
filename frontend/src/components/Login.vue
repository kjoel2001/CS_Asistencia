<template>
    <div class="main" :style="mainStyle">
        <h1>La Salle <br/> Universidad</h1>
        <form v-on:submit.prevent="login" action="" method="post">
            <input type="text" v-model="user.usr_dni" name="username" id="username" placeholder="Usuario" :style="input"/><br/>
            <input type="password" v-model="user.usr_pass" name="password" id="password" placeholder="Contraseña" :style="input"/><br/>
            <input type="button" value="Ingresar" class="button" id="done" :style="inputStyle"/><br/><br/>
            <a>¿Olvido su contraseña?</a><br/>
            <img src="../assets/google.svg" alt="Login using Google" />
            <img src="../assets/facebook.svg" alt="Login using Facebook" />
        </form>
    </div>
</template>
  
<script>
    import axios from 'axios'
    export default {
    name: "Login",
    data(){ 
        return { 
            user: {},
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }           
        }
    },
    methods: {
        login(){
            axios.post(this.postURL + '/login', this.user, this.config_request)
            .then(res => {
                console.log(res.data)
            })
            .catch((error) => {
                console.log(error)
            });
            console.log("OK")
        }
    },
    //Custom style for main and input for make the page responsive:
    props: {
        mainStyle: String,
        inputStyle: String,
        },
    };
</script>
  
<style>
    /* Import Poppins font: */
    @import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
  
    .main {
        background: rgba(255, 255, 255, 0.4);
        position: absolute;
        top: 14%;
        left: 30%;
        width: 40%;
        text-align: center;
        padding: 5px;
        border-radius: 3rem;
        box-shadow: 0px 0px 8px -5px #000000;
        padding-top: 2%;
        padding-bottom: 1%;
        font-family: "Poppins", sans-serif;
    }
  
    h1 {
        cursor: default;
        user-select: none;
    }
  
    input {
        border-radius: 3rem;
        border: none;
        padding: 10px;
        text-align: center;
        outline: none;
        margin: 10px;
        width: 30%;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
        font-weight: 400;
    }
  
    input:hover {
        box-shadow: 0px 0px 8px -5px #000000;
    }
  
    input:active {
        box-shadow: 0px 0px 8px -5px #000000;
    }
  
    #done {
        background: lightgreen;
    }
  
    .button {
        cursor: pointer;
        user-select: none;
    }
  
    img {
        height: 2.2rem;
        margin: 10px;
        user-select: none;
    }
  
    img:hover {
        box-shadow: 0px 0px 8px -5px #000000;
        cursor: pointer;
        border-radius: 200rem;
    }

    a {
        text-decoration: none;
        color: #000000;
    }
</style>
  