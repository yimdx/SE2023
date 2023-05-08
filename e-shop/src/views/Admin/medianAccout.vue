<template>
  <div class="all">
    <div class="card">
    <el-card>
      <el-descriptions title = 'MyAcocount' style="width: 600px" :column="1" :border='true'>
          <template #extra>
          <el-button type='primary' size='middle' @click="showConfirmCodeDialog">Recharge</el-button>
          </template>
        <el-descriptions-item label = 'Account'>
          <i class="el-icon-user"></i>
          {{ username }}
        </el-descriptions-item>
        <el-descriptions-item label = 'Balance'>
          <i class="el-icon-message"></i>
          {{ emailPrefix }}@{{emailSuffix}}
        </el-descriptions-item>
        <el-descriptions-item label = 'Phone'>
          <i class="el-icon-mobile-phone"></i>
          {{ phoneNumber }}
        </el-descriptions-item>
        <el-descriptions-item label = 'IdCode'>
          <i class="el-icon-location-outline"></i>
          {{ idCode }}
        </el-descriptions-item>
      </el-descriptions>
    </el-card>
    </div>
    <div class="dialog">
    <!-- 修改对话框 -->
    <el-dialog v-model="dialogVisible" title="modify your personal information" draggable>
      <div style="display: flex;flex-direction: column;align-items: center;justify-content: center;">
        <el-form :inline="true">
          <el-form-item label="Recharge Money">
            <el-input v-model="rechargeMoney" placeholder="1000.00 at least"></el-input>
          </el-form-item>
        </el-form>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancelRecharge()">Cancel</el-button>
        <el-button type="primary" @click="confirmRecharge()">Confirm</el-button>
      </span>
    </el-dialog>
    </div>
  </div>
</template>

<script setup>
import { ElNotification } from "element-plus";
import { ref, getCurrentInstance } from "vue";
import { Unlock, User, Avatar } from "@element-plus/icons-vue";
import { useRouter } from "vue-router";
import {usernameCheck,passwordCheck,idCodeCheck,emailCheck,phoneCheck} from "../../utils/regressionCheck"

let { proxy } = getCurrentInstance();


const rechargeMoney = ref("");
const router = useRouter();
const dialogVisible = ref(false);

function getAccount(){
  username.value = "myname";
  phoneNumber.value = "65535";
  emailPrefix.value = "200";
  emailSuffix.value = "fdu.edu.cn";
  idCode.value = "65535";
  password.value = "";
  certifyPassword.value = "";
};
getAccount();

const showConfirmCodeDialog = () => {
  // 显示对话框
  dialogVisible.value = true;
};
const cancelRecharge = () =>{
  getAccount();
  dialogVisible.value = false;
}
const confirmRecharge = () => {
//   if(!usernameCheck(username.value)){
//      ElNotification({
//       title: "Error",
//       message: "Invalid Username!",
//       type: "error",
//     });
//     username.value ="";
//   }
//   else
//   {
    // proxy.$http
    //   .post("/register", {
    //     username: username.value,
    //     password: password.value,
    //     idNumber: idCode.value,
    //     phoneNumber:phoneNumber.value,
    //     email:emailPrefix.value+"@"+emailSuffix.value
    //   })
    //   .then(function (res) {
    //     router.push('/');
    //      ElNotification({
    //       title: "Success",
    //       message: "Confirm PersonalInfo Change",
    //       type: "success",});
    //   })
    //   .catch(function (error) {
    //     console.log(error)
    //     ElNotification({
    //       title: "Error",
    //       message: "Register Failed(maybe username not unique)",
    //       type: "error",});
    //   });
//   }
  getAccount();
  dialogVisible.value = false;
}
</script>

<style scoped>
.all {
  position: absolute;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: linear-gradient(270deg, rgb(223, 198, 213), white);
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
  background: #ecf0f3;
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
  background: linear-gradient(117deg, white, rgb(239, 208, 233));
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
  background: linear-gradient(90deg, white, rgb(250, 230, 252));
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
  background: linear-gradient(86deg, white, rgb(245, 220, 249));
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