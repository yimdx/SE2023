<template>
  <div class="all">
    <el-container>
      <el-header >
      <div class="header">
          <el-page-header :icon="null" title="  "  style="overflow-x:hidden">
            <template #content>
              <div class="logo">
                <el-avatar
                  class="mr-3"
                  :size="48"
                  src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                />
              </div>
            </template>
            <div class="title">Welcome To e-shop!</div>
          </el-page-header>
        <div class="toolbar">
          <el-dropdown>
            <el-icon style="right: 2%;" color="#334155" size="170%"
             class="icon" ><setting
            /></el-icon>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="goInfo">Your Information</el-dropdown-item>
                <el-dropdown-item @click="changesettings">Settings</el-dropdown-item>
                <el-dropdown-item @click="logout">Signed Out</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
          <span>{{userName}}</span>
        </div>
      </div>
      </el-header>
      <el-container>
        <el-aside width="200px" height="100%" color="#334155" class="aside">
            <el-scrollbar>
            <!-- <div class="navigation"> -->
              <el-menu :default-openeds="['1', '3']"
              :router='true'>
                <el-sub-menu index="1">
                  <template #title>
                    <el-icon><Menu /></el-icon><span style="font-size:25px">All Stores</span>
                  </template>
                  <el-menu-item-group>
                    <template #title><span style="font-size:23px">Store</span></template>
                    <el-menu-item index="store" @click="gotoStore"><span style="font-size:20px">Stores</span></el-menu-item>
                  </el-menu-item-group>
                </el-sub-menu>
                <el-sub-menu index="2">
                  <template #title>
                    <el-icon><icon-menu /></el-icon><span style="font-size:25px">All Accounts</span>
                  </template>
                  <el-menu-item-group>
                    <template #title><span style="font-size:23px">Account</span></template>
                    <el-menu-item index="account" @click="gotoPersonalAccountPage"><span style="font-size:20px">Personal Account</span></el-menu-item>
                  </el-menu-item-group>
                </el-sub-menu>
                <el-sub-menu index="3">
                  <template #title>
                    <el-icon><icon-menu /></el-icon><span style="font-size:25px">Cart and Order</span>
                  </template>
                  <el-menu-item-group>
                    <template #title><span style="font-size:23px">Cart</span></template>
                    <el-menu-item index="cart" @click="gotoCartPage"><span style="font-size:20px">Cart</span></el-menu-item>
                  </el-menu-item-group>
                  <el-menu-item-group>
                    <template #title><span style="font-size:23px">Order</span></template>
                    <el-menu-item index="order" @click="gotoOrderPage"><span style="font-size:20px">Order</span></el-menu-item>
                  </el-menu-item-group>
                </el-sub-menu>
              </el-menu>
              <!-- </div> -->
            </el-scrollbar>
        </el-aside>
        <el-main style="width:100%;margin:0;padding:0;margin-top:12px;z-index=998">
           <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>


<script setup>
import { Setting } from "@element-plus/icons-vue";
import { Edit ,Menu} from '@element-plus/icons-vue'
import { useRouter } from "vue-router";
import  {useCounterStore} from "../../stores/counter"
const counter=useCounterStore();
const userName=counter.userName;
const userType=counter.userType;
const changesettings=()=>{
  // if(bg_op.value==false){
  //   bg_op.value=true;
  // }else{
  //   bg_op.value=false;
  // }
};
const logout=()=>{
  // if(bg_op.value==false){
  //   bg_op.value=true;
  // }else{
  //   bg_op.value=false;
  // }
  router.push("/");
  window.localStorage.removeItem("token");
};
const router = useRouter();
const goInfo=()=>{
  router.push("/buyer/index/personalinfo");
  // not implemented
};
// const router = useRouter();
const gotoStore = () => {
  router.push("/buyer/index/store");
};
const gotoPersonalAccountPage=()=>{
  router.push("/buyer/index/personalaccount");
}

const gotoCartPage = () =>{
  router.push("/buyer/index/cart");
}

const gotoOrderPage = () =>{
  router.push("/buyer/index/order");
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
  background:  rgb(230, 224, 224);
  display: flex;

}

.header {
  position: fixed;
  left: 0%;
  right: 0%;
  top: 0%;
  display: block;
  height: 80px;
  z-index:999;
  background-color: #ffffff;
  color: var(--el-text-color-primary);
}

.title {
  position: fixed;
  top: 3%;
  left: 15%;
  text-align: center;
  font-weight: 600;
  font-size: 24px;
  text-decoration: rgb(55, 65, 81);
  text-shadow: rgb(168, 168, 168) 3px 2px 2px;
}

.logo {
    position: fixed;
    top: 2%;
    left: 5%;
}

.toolbar {
  position: fixed;
  color: #171717;
  display: inline-flex;
  justify-content: center;
  height: 100%;
  right: 2.5%;
  top: 3%;
}

.navigation{
  position: relative;
  color: antiquewhite;
  top: 2%;
  overflow-x: hidden;
}
.aside{
  position: relative;
  left: 0;
  width: 18%;
  font-size: 16px;
  height: 100%;
}
.menu{
  font-size: 25px;
}

@keyframes rot{
  0%{
    transform: rotate(0deg);
  }
  100%{
    transform: rotate(360deg);
  }
}
.icon:hover{
  animation: rot 1s;
}

</style>