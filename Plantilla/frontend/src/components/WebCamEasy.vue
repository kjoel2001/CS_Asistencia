<template>
  <div>
    <div id="container">
      <video autoplay="true" id="videoElement">	
    </video>  
    </div>
    
    <button v-on:click='open'> Open </button>
    <button v-on:click='stop'> Stop </button>
    <button id="snap" v-on:click='snap'>Snap Photo</button>
    <br>

    <canvas id="canvas" width="500px" height="375px"></canvas>
  
</div>

</template>

<script>
// este componente no utiliza ningun modulo adicional
import axios from 'axios'

export default {
    data() {
        return {
          my_video: {}
        }
    },

    methods: {
        stop(e) {
            //var stream = this.my_video.srcObject;
            
            var stream = document.querySelector("#videoElement").srcObject;
            var tracks = stream.getTracks();

            for (var i = 0; i < tracks.length; i++) {
              var track = tracks[i];
              track.stop();
            }

            //this.video.srcObject = null;
            document.querySelector("#videoElement").srcObject = null
          },
        open() {
          this.my_video = document.querySelector("#videoElement");          

          //console.log(this.my_video);

          if (navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true })
              .then(function (stream) {
                //console.log(stream);
                //this.my_video.srcObject = stream;
                document.querySelector("#videoElement").srcObject = stream;
              })
              .catch(function (err) {
                console.log("Something went wrong!");
                console.log(err);
              });
          }
        },

        snap(){
          var video=document.querySelector('video');
          var canvas = document.querySelector('canvas');
          var context = canvas.getContext('2d');
          

          var ratio = video.videoWidth/video.videoHeight;
          var w = video.videoWidth-100;
          var h = parseInt(w/ratio,10);
          canvas.width = w;
          canvas.height = h;

          //console.log(canvas);

          context.fillRect(0,0,w,h);
          context.drawImage(document.querySelector('video'),0,0,w,h);   

          /****************************************************/
          // send canvas to file to be uploaded
          // Convert canvas image to Base64
          var img = canvas.toDataURL();
          // Convert Base64 image to binary
          var file = this.dataURItoBlob(img);

          // send to endpoint
          var data = new FormData();          
          data.append('file', file, 'foto.png');

         

          axios.post('http://127.0.0.1:5000/task/upload_photo', data, {headers: {'Content-Type': 'multipart/form-data'}})
            .then(function(data){
              console.log(data.data);
            })
            .catch((error) => {
              console.log(error)
          });

          

          /****************************************************/
                
        },

        dataURItoBlob(dataURI) {
            // convert base64/URLEncoded data component to raw binary data held in a string
            var byteString;
            if (dataURI.split(',')[0].indexOf('base64') >= 0)
                byteString = atob(dataURI.split(',')[1]);
            else
                byteString = unescape(dataURI.split(',')[1]);
            // separate out the mime component
            var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
            // write the bytes of the string to a typed array
            var ia = new Uint8Array(byteString.length);
            for (var i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            return new Blob([ia], {type:mimeString});
        }
    },
    
    created(){ 
        
    }
}
</script>

<style>
#container {
	margin: 0px auto;
	width: 500px;
	height: 375px;
	border: 10px #333 solid;
}
#videoElement {
	width: 500px;
	height: 375px;
	background-color: #666;
  /*Mirror code starts*/
    transform: rotateY(180deg);
    -webkit-transform:rotateY(180deg); /* Safari and Chrome */
    -moz-transform:rotateY(180deg); /* Firefox */
    /*Mirror code ends*/
}  
#canvas {	
  background-color: #666;
  /*Mirror code starts*/
    transform: rotateY(180deg);
    -webkit-transform:rotateY(180deg); /* Safari and Chrome */
    -moz-transform:rotateY(180deg); /* Firefox */
    /*Mirror code ends*/
}  
</style>