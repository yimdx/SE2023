<template>
  <div class="all">
    <div class="circle"></div>
    <div class="circle2"></div>
    <div class="circle3"></div>
    <div class="title">Welcome Back!</div>
    
    <div class="box">
       <div class="channels">Try to login via another channel,</div>
       <div class="icons">
        <span @click="gotoAdminLoginPage" style="cursor:pointer" class="channel"><el-icon size="36px"><Avatar /></el-icon> <span class="des">admin</span> </span>
        <span @click="gotoSellerLoginPage" style="cursor:pointer" class="channel"><el-icon size="36px" ><User /></el-icon> <span class="des">seller</span></span>
        </div>
         <div class="channels" style="top:15%;margin-bottom:0;padding-bottom:0">or use Username and Password to login</div>
        <div class="form">
         
          <div  class="input">
               <el-input
              v-model="username"
              placeholder="Please input your Username."
              clearable
            />
          </div>
           
           <div class="input">
            <el-input
              v-model="password"
              type="password"
              placeholder="Please input your Password."
              show-password
            />
           </div>
              
            <div style="width:352px;"> 
              <span  style="position:relative;left:10px;cursor:pointer" @click="gotoUserRegister" > Don't have account?</span>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span style="position:relative;right:0;cursor:pointer" >Forgot Password?</span>
            </div>

            <div class="btn">
               <el-button :icon="Unlock" size="large" type="danger" round @click="signInBuyer">Sign In</el-button>
            </div>
        </div>
<!--         
      <router-link to="/register">user register</router-link>
       -->
    
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import {Unlock ,User,Avatar} from "@element-plus/icons-vue";
import {useRouter} from "vue-router"
const username = ref("");
const password = ref("");
const router=useRouter();
const gotoAdminLoginPage=()=>{
  router.push("/admin/login");
};
const gotoSellerLoginPage=()=>{
  router.push("/seller/login");
};
const gotoUserRegister=()=>{
  router.push("/register");
}
const signInBuyer=()=>{
  alert(username.value);
  alert(password.value);
  //regression check
  //status or api
};
</script>

<style scoped>
.all {
  position : absolute;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: linear-gradient(to top,rgb(243,218,233),white);
}
.box {
  margin: 0%;
  padding: 20px;
  align-items: center;
  position: relative;
  left: 38%;
  right: auto;
  background: #ECF0F3;
  top:24%;
  width:392px;
  height: 370px;
  box-sizing: border-box;
  box-shadow: 10px 10px 10px 0px rgb(209,217,230) ,-10px -10px 10px 0px  rgb(249,249,249);
  border-radius: 16px;
}
.form{
  position: relative;
  width: 352px;
  height:100px;
  margin: auto;
  top:16%;
}
.input{
  margin: 20px;;
}
.btn{
  position: relative;
  margin: auto;
  margin-top: 10px;
  left:37%;
  
}
.title{
  position: relative;
  top:16%;
  text-align: center;
  font-weight:600;
  font-size: 36px;
  text-decoration :rgb(55,65,81);
  text-shadow: rgb(168,168,168) 3px 2px 2px;
}
.channels{
  font-size:20px;
  font-weight: 400;
  text-align: center;
  position: relative;
  top:0;
}
.icons{
  position: relative;
  top:8%;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.channel :hover{
  transform: scale(1.02);
}

.circle{
  position: fixed;
  left: 100px;
  bottom: 125px;
  width:130px;
  height: 130px;
  border-radius: 50%;
  background: white;
   box-shadow: 10px 10px 10px 0px rgb(209,217,230) inset;
  /* animation: x-run 5s 10s cubic-bezier(.09,.66,.26,1.29), y-run 5s 1s linear; */
  animation: x-run 60s 0s linear  infinite,y-run 60s 0s linear infinite;
}
    
.circle2{
  position: fixed;
  left: 1000px;
  bottom: 725px;
  width:260px;
  height: 260px;
  border-radius: 50%;
  background: white;
   box-shadow: 10px 10px 10px 0px rgb(209,217,230) inset;
  /* animation: x-run 5s 10s cubic-bezier(.09,.66,.26,1.29), y-run 5s 1s linear; */
  animation: x-run2 75s 0s linear  infinite,y-run2 75s 0s linear infinite;
}

.circle3{
  position: fixed;
  left: 1100px;
  bottom: 100px;
  width:70px;
  height: 70px;
  border-radius: 50%;
  background: white;
   box-shadow: 10px 10px 10px 0px rgb(209,217,230) inset;
  /* animation: x-run 5s 10s cubic-bezier(.09,.66,.26,1.29), y-run 5s 1s linear; */
  animation: x-run3 45s 0s linear  infinite,y-run3 45s 0s linear infinite;
}

@keyframes x-run {
    0% {
        left: 100px;
        transform: rotate(0deg);
    }
 
    25% {
        ransform:rotate(90deg);
        left: 700px;
    }
    50% {
        ransform:rotate(180deg);
        left: 1200px;
    }
    75% {
        ransform:rotate(270deg);
        left: 680px;
    }
    100% {
        ransform:rotate(360deg);
        left: 100px;
    }

}

@keyframes x-run2 {
    0% {
        left: 1000px;
        transform: rotate(0deg);
    }
 
    25% {
        ransform:rotate(90deg);
        left: 1700px;
    }
    50% {
        ransform:rotate(180deg);
        left: 1200px;
    }
    75% {
        ransform:rotate(270deg);
        left: 680px;
    }
    100% {
        ransform:rotate(360deg);
        left: 1000px;
    }

}

@keyframes x-run3 {
    0% {
        left: 1100px;
        transform: rotate(0deg);
    }
 
    25% {
        ransform:rotate(90deg);
        left: 700px;
    }
    50% {
        ransform:rotate(180deg);
        left: 200px;
    }
    75% {
        ransform:rotate(270deg);
        left: 680px;
    }
    100% {
        ransform:rotate(360deg);
        left: 1100px;
    }

}
 
@keyframes y-run {
    0% {
        bottom: -73px;
    }
    50%{
      bottom:960px;
    }
    100% {
        bottom: -73px;
    }
}

@keyframes y-run2 {
    0% {
        bottom: 725px;
    }
    50%{
      bottom:660px;
    }
    100% {
        bottom: 725px;
    }
}


@keyframes y-run3 {
    0% {
        bottom: 100px;
    }
    50%{
      bottom:560px;
    }
    100% {
        bottom: 100px;
    }
}
</style>