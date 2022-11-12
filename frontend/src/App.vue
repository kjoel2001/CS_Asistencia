<template>
  <div id="login">
    <main>
      <!-- Different styles for different devices: -->
      <mq-layout mq="lg">
        <Login/>
      </mq-layout>

      <mq-layout mq="md">
        <Login mainStyle="left:20%;width:60%;" inputStyle="width:40%;" />
      </mq-layout>

      <mq-layout mq="sm">
        <Login mainStyle="left:10%;width:80%;" inputStyle="width:50%;" />
      </mq-layout>
    </main>
  </div>
</template>

<script>
import Login from './components/Login.vue'

export default {
  name: 'App',
  components: {
    Login
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;

}

#login {
  background: url("./assets/background.jpg");
  background-size: cover;
  image-rendering: crisp-edges;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
</style>