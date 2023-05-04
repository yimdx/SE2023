<template>
   <div class="box">
      <div class="title">
         Open a store
      </div>
      <div class="subtitle">
        Fill in the box and submit it to create a store openning request.
      </div>
   
      <div class="form">
        <div class="input">
          <el-icon class="myIcon"><CreditCard /></el-icon>
          <el-tooltip
            effect="customized"
            content="letters,digits and underline only, with length of 3~10"
            placement="right"
            ><el-input  class="input-box" v-model="shopName" placeholder="Shopname" clearable
          /></el-tooltip>
        </div>

        <div class="input">
          <el-icon class="myIcon"><CreditCard /></el-icon>
          <el-tooltip
            effect="customized"
            content="digits"
            placement="right"
            ><el-input
            class="input-box"
              v-model="identificationID"
              placeholder="Identification ID"
              clearable
          /></el-tooltip>
        </div>

        <div class="input">
          <el-icon class="myIcon"><CreditCard /></el-icon>
          <el-tooltip
            effect="customized"
            content="address in MainLand of China"
            placement="right"
            ><el-input class="input-box" v-model="address" placeholder="Address" clearable
          /></el-tooltip>
        </div>

        <div class="input">
          <el-icon class="myIcon"><CreditCard /></el-icon>
          <el-tooltip
            effect="customized"
            content="digits"
            placement="right"
            ><el-input class="input-box" v-model="initialFund" placeholder="Initial Fund" clearable
          /></el-tooltip>
        </div>

         <div class="input">
          <el-icon class="myIcon"><CreditCard /></el-icon>
          <el-tooltip
            effect="customized"
            content="sentences"
            placement="right"
            ><el-input class="input-box" v-model="shopIntro" placeholder="A brief shop introduction" clearable
          /></el-tooltip>
        </div>
         
         <div class="btn">
          <el-button class="btn-c" size="large" round @click="request"><span style="font-size:22px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Submit&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></el-button>
         </div>
      </div>
   </div>
</template>

<script setup>
import { ElNotification } from "element-plus";
import { ref ,getCurrentInstance} from "vue";
import {shopNameCheck,addressCheck,identificationIDCheck,initialFundCheck} from "../../utils/regressionCheck";
// import {sakura} from "../../static/img-base64/sakura"
// img.src="";
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
let {proxy}= getCurrentInstance();
const radio = ref("seller");
const shopName = ref("");
const address = ref("");
const identificationID = ref("");
const shopIntro = ref("");
const initialFund = ref("");
const request=()=>{
  if(!shopNameCheck(shopName.value)){
     ElNotification({
      title: "Error",
      message: "Invalid ShopName!",
      type: "error",
    });
    shopName.value ="";
  }else if(!addressCheck(address.value)){
      ElNotification({
      title: "Error",
      message: "Invalid Address!",
      type: "error",
    });
    address.value = "";
  }else if(!identificationIDCheck(identificationID.value)){
     ElNotification({
      title: "Error",
      message: "Invalid IdentificationID number",
      type: "error",});
      identificationID.value="";
  }else if(!initialFundCheck(initialFund.value)){
     ElNotification({
      title: "Error",
      message: "Invalid InitialFund",
      type: "error",});
      initialFund.value="";
  }
  else
  {
    proxy.$http
      .post("/seller/request", {
        shopName: shopName.value,
        identificationID: identificationID.value,
        address: address.value,
        initialFund: initialFund.value,
        shopIntro:shopIntro.value,
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
  left: 16%;
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
  left: 10%;
  width: 400px;
  height: 400px;
  margin: 0;
  top: 5%;
  border-radius: 10px;
}

.input {
  margin: 20px;
  margin-bottom: 10px;
  display: flex;
}
.input-box {
 border-radius: 10px;
}

.btn{
  margin: 20px;
  position: relative;
  left:0%;
  bottom: -5%;
}

.btn-c{
  background: linear-gradient(to right,rgb(185, 251, 251),rgb(239, 253, 252));
}
</style>