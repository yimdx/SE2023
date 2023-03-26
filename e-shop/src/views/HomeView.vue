<template>
  <div class="common-layout" :style="{background:bg_op?'#000000':'#FFFFFF'}">
    <el-container style="width:100%;margin:0;padding:0;">
      <el-header>
        <div class="header" :style="{background:bg_op?'#334155':'#ececec'}">
          <div class="navigation">
            <el-page-header :icon="null" title="  "  style="overflow-x:hidden">
              <template #content>
                <div>
                  <el-avatar
                    class="mr-3"
                    :size="32"
                    src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                  />
                </div>
              </template>
              <template #extra>
                <div>
                  <el-button style="overflow-x:hidden" size="large" type="info" round color="#EBECFF"
                    ><router-link to="/admin/login"
                      >Admin Channel</router-link
                    ></el-button
                  >
                  <el-button style="overflow-x:hidden"  size="large" type="info" round color="#EBECFF"
                    ><router-link to="/seller/login"
                      >Seller Channel</router-link
                    ></el-button
                  >
                  <el-button style="overflow-x:hidden"  size="large" type="info" round color="#EBECFF"
                    ><router-link to="/buyer/login"
                      >Buyer Channel</router-link
                    ></el-button
                  >
                  <span class="right-btn">
                    <el-button :icon="SwitchButton" circle @click="changeBg" />
                  </span>
                </div>
              </template>
            </el-page-header>
          </div>
        </div>
      </el-header>
      <el-main style="width:100%;margin:0;padding:0;margin-top:12px;z-index=998">
          <!-- <el-card
            class="box-card"
            style="width: 250px"
          >
            <template #header>
              <div class="card-header">
                <span>Card name</span>
                <el-button class="button" text>Operation button</el-button>
              </div>
            </template>
          <el-image style="width: 100px; height: 100px" src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" fit="full" /> 
          </el-card> -->
        <div class="full">
          <div style="font-size:60px;padding-left:40px;padding-top:100px;">Welcome to e-shop!</div>
          <div style="font-size:30px;padding-left:40px;padding-top:20px;">Here is the home page!</div>
        </div>
        <div>
          <div style="font-size:70px;text-align:center"><span :style="{color:bg_op?'#FFFFFF':'#000000' }"> Shopping anytime,anywhere!</span></div>
          <div style="font-size:30px;text-align:center"><span :style="{color:bg_op?'#FFFFFF':'#000000' }">Enjoy attractive promotions,super savings from the most prestigious store!</span> </div>
        </div>

        <el-row style="margin-left:20px;margin-right-150px;">
          <el-col
            v-for="(o,index) in titles1"
            :key="index"
            :span="5"
            :offset="2"
          >
            <el-card :body-style="{ padding: '0px' }">
              <img
                :src="img1[index]"
                class="image"
              />
              <div style="padding: 14px">
                <span style="font:20px bold;">{{o}}</span>
                <div class="bottom">
                  <div>{{des1[index]}}</div>
                </div>
              </div>
            </el-card>
          </el-col>


           <el-col
            v-for="(o,index) in titles2"
            :key="index"
            :span="5"
            :offset="2"
          >
            <el-card :body-style="{ padding: '0px' }">
              <img
                :src="img2[index]"
                class="image"
              />
              <div style="padding: 14px">
                <span style="font:20px bold;">{{o}}</span>
                <div class="bottom">
                  <div>{{des2[index]}}</div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-divider />
        <div style="text-align:center;font-size:20px;color:#ee55aa">To see more about this app,please login in via three different channels.</div>
      </el-main>
    </el-container>
  </div>
</template>



<script setup>
import { SwitchButton } from "@element-plus/icons-vue";

import { ref } from 'vue'
const currentDate = ref(new Date())
const titles1=["Availability","Save Time","Comparison of Prices "];
const des1=[
"Online shopping stores are open round the clock of 24/7, 7 days a week and 365 days",
"With just a couple of clicks of the mouse, you can purchase your shopping orders."
,"The advanced innovation of search engine allows you to easily check prices."];

const img1=["https://img2.baidu.com/it/u=1005102363,3554051776&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500",
"https://img1.baidu.com/it/u=993869626,2637250794&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500",
"https://img0.baidu.com/it/u=117594428,1715799536&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500"];
const img2=["https://img0.baidu.com/it/u=2716259446,2240992840&fm=253&fmt=auto&app=138&f=PNG?w=500&h=500",
"https://img2.baidu.com/it/u=3927189674,4006346655&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500"
,"https://img2.baidu.com/it/u=345918708,548433025&fm=253&fmt=auto&app=138&f=PNG?w=500&h=500"];
const titles2=["Today's Suggestion","Transfer Support","Quality Guaranteed"];
const des2=[
"Choose the right product for you in Today's Suggestion.",
"You can the status of the order you've been purchased."
,"We can promise you the quality of the good.:)"];
let bg_op=ref(false);
const changeBg=()=>{
  if(bg_op.value==false){
    bg_op.value=true;
  }else{
    bg_op.value=false;
  }
};
</script>

<style scoped>
.common-layout{
  margin: 0;
  padding: 0;
  width:100%;
  overflow: hidden;
}
.header {
  position: fixed;
  left: 0%;
  right: 0%;
  top: 0%;
  display: block;
  height: 80px;
  z-index:999;
}
.navigation {
  position: fixed;
  margin: 20px;
}
.right-btn {
  position: fixed;
  right: 2%;
}
.banner{
  width:100%;
  margin:0;
  padding: 0;;
}
.full{
  width:100%;
  height:620px;
  background-image: url(../static/img/banner_main.png);
  background-repeat: no-repeat;
  background-size: cover;
}



.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}
.fixed{
  position: fixed;
};

</style>
