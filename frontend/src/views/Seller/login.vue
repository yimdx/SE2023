<template>
  <div class="all">
    <div class="stripe"></div>
    <div class="stripe2"></div>
    <div class="stripe3"></div>
    <div class="circle"></div>
    <div class="circle2"></div>
    <div class="circle3"></div>
    <div class="title">Welcome Back!</div>

    <div class="box">
      <div class="channels">Try to login via another channel,</div>
      <div class="icons">
        <span
          @click="gotoAdminLoginPage"
          style="cursor: pointer"
          class="channel"
          ><el-icon size="36px"><Avatar /></el-icon>
          <span class="des">admin</span>
        </span>
        <span
          @click="gotoBuyerLoginPage"
          style="cursor: pointer"
          class="channel"
          ><el-icon size="36px"><User /></el-icon>
          <span class="des">buyer</span></span
        >
      </div>
      <div
        class="channels"
        style="top: 15%; margin-bottom: 0; padding-bottom: 0"
      >
        or use Username and Password to login
      </div>
      <div class="form">
        <div class="input">
          <el-tooltip
            effect="customized"
            content="letters,digits and underline only, with length of 3~10"
            placement="right"
            ><el-input
              v-model="username"
              placeholder="Please input your Username."
              clearable
          /></el-tooltip>
        </div>

        <div class="input">
          <el-tooltip
            effect="customized"
            content="6~32 characters are needed;letters,digits and special characters(_ or -) must appear in group"
            placement="right"
          >
            <el-input
              v-model="password"
              type="password"
              placeholder="Please input your Password."
              show-password
          /></el-tooltip>
        </div>

        <div style="width: 352px">
          <span
            style="position: relative; left: 10px; cursor: pointer"
            @click="gotoUserRegister"
          >
            Don't have account?</span
          >
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span style="position: relative; right: 0; cursor: pointer"
            >Forgot Password?</span
          >
        </div>

        <div class="btn">
          <el-button
            :icon="Unlock"
            size="large"
            type="success"
            round
            @click="signInBuyer"
            >Sign In</el-button
          >
        </div>
      </div>
      <!--         
      <router-link to="/register">user register</router-link>
       -->
    </div>
  </div>
</template>

<script setup>
import { ElNotification } from "element-plus";
import { ref, getCurrentInstance } from "vue";
import { Unlock, User, Avatar } from "@element-plus/icons-vue";
import { useRouter } from "vue-router";
import { usernameCheck, passwordCheck } from "../../utils/regressionCheck.js";
import {useCounterStore} from "../../stores/counter"
// import {leaf} from "../../static/img-base64/leaf"
let { proxy } = getCurrentInstance();

// img.src=leaf;
// var child = document.getElementById("canvas_sakura");
// while(child){
//     var parent=child.parentNode;
//     parent.removeChild(child);
//     child = document.getElementById("canvas_sakura")
// }
// startSakura();
// child = document.getElementById("canvas_sakura")
// var parent=child.parentNode;
// parent.removeChild(child);

const errorMsg = ref("");
const username = ref("");
const password = ref("");
const router = useRouter();
const counter =useCounterStore();
const gotoAdminLoginPage = () => {
  router.push("/admin/login");
};
const gotoBuyerLoginPage = () => {
  router.push("/buyer/login");
};
const gotoUserRegister = () => {
  router.push("/register");
};
const signInBuyer = () => {
  if (usernameCheck(username.value) && passwordCheck(password.value)) {
    proxy.$http
      .post("/seller/login", {
        username: username.value,
        password: password.value,
      })
      .then(function (res) {
        window.localStorage.setItem('token','123');
        counter.$patch({
          userName:username.value,
          userType:"seller"
        });
        router.push('/seller/index');
          ElNotification({
          title: "Success",
          message: "Login Success",
          type: "success",});
      })
      .catch(function (error) {
         ElNotification({
          title: "Error",
          message: "User Not Found",
          type: "Error",});
      });
  } else {
    ElNotification({
      title: "Error",
      message: "Invalid Username or Password format!",
      type: "error",
    });
    username.value = "";
    password.value = "";
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
  background: linear-gradient(270deg, rgb(192, 255, 218), white);
  background-size: 200% 200%;
  background-position: 0 0;
  animation: bgposition 2s infinite linear alternate;
}
@keyframes bgposition {
  0% {
    background-position: 0 0;
  }
  100% {
    background-position: 100% 100%;
  }
}
.box {
  margin: 0%;
  padding: 20px;
  align-items: center;
  position: relative;
  left: 38%;
  right: auto;
  background: #e9ffd5;
  top: 24%;
  width: 392px;
  height: 370px;
  box-sizing: border-box;
  box-shadow: 10px 10px 10px 0px rgb(209, 217, 230),
    -10px -10px 10px 0px rgb(249, 249, 249);
  border-radius: 16px;
}
.form {
  position: relative;
  width: 352px;
  height: 100px;
  margin: auto;
  top: 16%;
}
.input {
  margin: 20px;
}
.btn {
  position: relative;
  margin: auto;
  margin-top: 10px;
  left: 37%;
}
.title {
  position: relative;
  top: 16%;
  text-align: center;
  font-weight: 600;
  font-size: 36px;
  text-decoration: rgb(55, 65, 81);
  text-shadow: rgb(168, 168, 168) 3px 2px 2px;
}
.channels {
  font-size: 20px;
  font-weight: 400;
  text-align: center;
  position: relative;
  top: 0;
}
.icons {
  position: relative;
  top: 8%;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.channel :hover {
  transform: scale(1.02);
}

.circle {
  position: fixed;
  left: 100px;
  bottom: 125px;
  width: 130px;
  height: 130px;
  border-radius: 50%;
  background: linear-gradient(117deg, white, rgb(180, 255, 210));
  opacity: 50%;
  box-shadow: 10px 10px 10px 0px rgb(209, 217, 230) inset;
  /* animation: x-run 5s 10s cubic-bezier(.09,.66,.26,1.29), y-run 5s 1s linear; */
  animation: x-run 60s 0s linear infinite, y-run 60s 0s linear infinite;
}

.circle2 {
  position: fixed;
  opacity: 50%;
  left: 1000px;
  bottom: 725px;
  width: 260px;
  height: 260px;
  border-radius: 50%;
  background: linear-gradient(90deg, white, rgb(224, 255, 197));
  box-shadow: 10px 10px 10px 0px rgb(209, 217, 230) inset;
  /* animation: x-run 5s 10s cubic-bezier(.09,.66,.26,1.29), y-run 5s 1s linear; */
  animation: x-run2 75s 0s linear infinite, y-run2 75s 0s linear infinite;
}

.circle3 {
  position: fixed;
  left: 1100px;
  bottom: 100px;
  opacity: 50%;
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: linear-gradient(86deg, white, rgb(190, 255, 191));
  box-shadow: 10px 10px 10px 0px rgb(209, 217, 230) inset;
  /* animation: x-run 5s 10s cubic-bezier(.09,.66,.26,1.29), y-run 5s 1s linear; */
  animation: x-run3 45s 0s linear infinite, y-run3 45s 0s linear infinite;
}

@keyframes x-run {
  0% {
    left: 100px;
    transform: rotate(0deg);
  }

  25% {
    ransform: rotate(90deg);
    left: 700px;
  }
  50% {
    ransform: rotate(180deg);
    left: 1200px;
  }
  75% {
    ransform: rotate(270deg);
    left: 680px;
  }
  100% {
    ransform: rotate(360deg);
    left: 100px;
  }
}

@keyframes x-run2 {
  0% {
    left: 1000px;
    transform: rotate(0deg);
  }

  25% {
    ransform: rotate(90deg);
    left: 1700px;
  }
  50% {
    ransform: rotate(180deg);
    left: 1200px;
  }
  75% {
    ransform: rotate(270deg);
    left: 680px;
  }
  100% {
    ransform: rotate(360deg);
    left: 1000px;
  }
}

@keyframes x-run3 {
  0% {
    left: 1100px;
    transform: rotate(0deg);
  }

  25% {
    ransform: rotate(90deg);
    left: 700px;
  }
  50% {
    ransform: rotate(180deg);
    left: 200px;
  }
  75% {
    ransform: rotate(270deg);
    left: 680px;
  }
  100% {
    ransform: rotate(360deg);
    left: 1100px;
  }
}

@keyframes y-run {
  0% {
    bottom: -73px;
  }
  50% {
    bottom: 960px;
  }
  100% {
    bottom: -73px;
  }
}

@keyframes y-run2 {
  0% {
    bottom: 725px;
  }
  50% {
    bottom: 660px;
  }
  100% {
    bottom: 725px;
  }
}

@keyframes y-run3 {
  0% {
    bottom: 100px;
  }
  50% {
    bottom: 560px;
  }
  100% {
    bottom: 100px;
  }
}

.stripe {
  background: linear-gradient(to right, white, rgb(223, 198, 213));
  opacity: 10%;
  position: fixed;
  left: 50%;
  top: -120%;
  width: 10%;
  height: 350%;
  transform: rotate(0deg);
  animation: 60s rot infinite;
}
@keyframes rot {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.stripe2 {
  background: linear-gradient(to right, white, rgb(223, 198, 213));
  opacity: 10%;
  position: fixed;
  left: 50%;
  top: -120%;
  width: 5%;
  height: 350%;
  transform: rotate(30deg);
  animation: 40s rot2 infinite;
}
@keyframes rot2 {
  0% {
    transform: rotate(30deg);
  }
  100% {
    transform: rotate(390deg);
  }
}

.stripe3 {
  background: linear-gradient(to right, white, rgb(223, 198, 213));
  opacity: 10%;
  position: fixed;
  left: 50%;
  top: -120%;
  width: 7%;
  height: 350%;
  transform: rotate(0deg);
  animation: 50s rot3 infinite;
}
@keyframes rot3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(-360deg);
  }
}
</style>