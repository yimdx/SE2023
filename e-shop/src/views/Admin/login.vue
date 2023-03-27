<template>
    admin login
</template>

<script setup>
import {sakura} from "../../static/img-base64/sakura"
img.src=sakura;
var child = document.getElementById("canvas_sakura");
while(child){
    var parent=child.parentNode;
    parent.removeChild(child);
    child = document.getElementById("canvas_sakura")
}
startSakura();
child = document.getElementById("canvas_sakura")
  var parent=child.parentNode;
    parent.removeChild(child);

</script>

<style>

</style>