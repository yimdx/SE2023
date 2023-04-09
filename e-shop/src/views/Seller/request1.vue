<template>
  <div class="all">
    <div class="box">
      <div class="title">Create Account!</div>
      <div class="subtitle">
        Fill in the form and you can explore the app freely.
      </div>

      <div class="form">
        <div class="input">
          <el-icon class="myIcon"><UserFilled /></el-icon>
          <el-tooltip
            effect="customized"
            content="letters,digits and underline only, with length of 3~10"
            placement="right"
            ><el-input  class="input-box" v-model="username" placeholder="Username" clearable
          /></el-tooltip>
        </div>

        <div class="input">
          <el-icon class="myIcon"><Iphone /></el-icon>
          <el-tooltip
            effect="customized"
            content="personal phone number in MainLand of China"
            placement="right"
            ><el-input
            class="input-box"
              v-model="phoneNumber"
              placeholder="Phone Number"
              clearable
          /></el-tooltip>
        </div>

        <div class="input">
          <el-icon class="myIcon"><CreditCard /></el-icon>
          <el-tooltip
            effect="customized"
            content="personal ID number in MainLand of China"
            placement="right"
            ><el-input class="input-box" v-model="idCode" placeholder="ID number" clearable
          /></el-tooltip>
        </div>

        <div class="input">
          <el-icon class="myIcon"><Message /></el-icon>
          <el-tooltip
            effect="customized"
            content="Common Email,Must be valid."
            placement="right"
          >
          <div style="display:flex">
             <div class="prefix">
              <el-input
              class="input-box"
                v-model="emailPrefix"
                placeholder="Email Username"
                clearable
              />
            </div>
            <span>&nbsp; @ &nbsp;</span>
            <div class="suffix">
              <el-input
              class="input-box"
                v-model="emailSuffix"
                placeholder="Email Address"
                clearable
              />
            </div>
          </div>
           
          
          </el-tooltip>
        </div>

        <div class="input">
          <el-icon class="myIcon"><Key /></el-icon>
          <el-tooltip
            effect="customized"
            content="6~32 characters are needed;letters,digits and special characters(_ or -) must appear in group"
            placement="right"
          >
            <el-input
            class="input-box"
              v-model="password"
              type="password"
              placeholder="Password"
              show-password
          /></el-tooltip>
        </div>

        <div class="input">
          <el-icon class="myIcon"><Key /></el-icon>
          <el-tooltip
            effect="customized"
            content="same as password above"
            placement="right"
          >
            <el-input
            class="input-box"
              v-model="certifyPassword"
              type="password"
              placeholder="Password confirmation"
              show-password
          /></el-tooltip>
        </div>
      </div>

      <div class="btn">
        <el-button class="btn-c" size="large" round @click="request"><span style="font-size:22px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store Open Request&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
// import { ElNotification } from "element-plus";
// import { ref ,getCurrentInstance} from "vue";
// import {usernameCheck,passwordCheck,idCodeCheck,emailCheck,phoneCheck} from "../../utils/regressionCheck"
import {
  Key,
  UserFilled,
  Message,
  CreditCard,
  Iphone,
  User,
} from "@element-plus/icons-vue";
import {sakura} from "../../static/img-base64/sakura"
img.src="";
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
let {proxy}= getCurrentInstance();
const radio = ref("seller");
const username = ref("");
const password = ref("");
const phoneNumber = ref("");
const idCode = ref("");
const emailPrefix = ref("");
const emailSuffix = ref("");
const certifyPassword = ref("");
const register=()=>{
  if(!usernameCheck(username.value)){
     ElNotification({
      title: "Error",
      message: "Invalid Username!",
      type: "error",
    });
    username.value ="";
  }else if(!passwordCheck(password.value)){
      ElNotification({
      title: "Error",
      message: "Invalid Password!",
      type: "error",
    });
    password.value = "";
  }else if(!(password.value=== certifyPassword.value )){
      ElNotification({
      title: "Error",
      message: "Password Confirmation failed.",
      type: "error",
    });
    certifyPassword.value="";
  }else if(!idCodeCheck(idCode.value)){
     ElNotification({
      title: "Error",
      message: "Invalid ID number",
      type: "error",});
    idCode.value="";
  }
  else if(!emailCheck(emailPrefix.value+"@"+emailSuffix.value)){
     ElNotification({
      title: "Error",
      message: "Invalid email",
      type: "error",});
    emailPrefix.value="";
    emailSuffix.value="";
  }else if(!phoneCheck(phoneNumber.value)){
     ElNotification({
      title: "Error",
      message: "Invalid phone number",
      type: "error",});
    phoneNumber.value="";
  }
  else
  {
    proxy.$http
      .post("/request", {
        username: username.value,
        password: password.value,
        userType: radio.value,
        idNumber: idCode.value,
        phoneNumber:phoneNumber.value,
        email:emailPrefix.value+"@"+emailSuffix.value
      })
      .then(function (res) {
        console.log(res.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  
};
</script>

<style scoped>
.all {
  position: absolute;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: linear-gradient(270deg, rgb(213, 251, 255), white);
}

.box {
  margin: 0%;
  padding: 20px;
  align-items: center;
  position: relative;
  left: 32%;
  right: auto;
  background: linear-gradient(315deg,rgb(196, 234, 245),#ecf0f3);
  top: 10%;
  width: 600px;
  height: 633px;
  box-sizing: border-box;
  box-shadow: 10px 10px 10px 0px rgb(209, 217, 230),
    -10px -10px 10px 0px rgb(249, 249, 249);
  border-radius: 16px;
}

.title {
  font-size: 30px;
  text-align: center;
  font-weight: 700;
  text-decoration: rgb(55, 65, 81);
}
.subtitle {
  font-size: 19px;
  font-weight: 500;
  text-align: center;
  color: #94a3af;
}

.form {
  position: relative;
  background: red;
  left: 14%;
  width: 400px;
  height: 400px;
  margin: 0;
  top: 5%;
  border-radius: 10px;
  background:linear-gradient(45deg,rgb(170, 234, 254),white);
}
.input {
  margin: 20px;
  margin-bottom: 10px;
  display: flex;
}
.input-box {
 border-radius: 10px;
}
.prefix {
  margin: 0px;
}
.suffix {
  margin: 0;
}
.myIcon {
  font-size: 26px;
  margin-right: 20px;
}
.myIcon :hover{
  animation: icon-rot 1s;
}
@keyframes icon-rot{
  0%{
    transform: rotate(0deg);
  }
  25%{
    transform: rotate(10deg);
  }
  50%{
    transform: rotate(0deg);
  }
  75%{
    transform: rotate(-8deg);
  }
  100%{
    transform: rotate(0deg);
  }
}
.btn{
  margin: 20px;
  position: relative;
  left:25%;
  bottom: -5%;
}
.btn-c{
  background: linear-gradient(to right,rgb(185, 251, 251),rgb(239, 253, 252));
}
a{
  text-decoration: none;
  color: blue;
  font-size: 20px;
}
</style>