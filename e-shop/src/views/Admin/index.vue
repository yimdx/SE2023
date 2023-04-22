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
          <!-- <span class="right-btn">   
                    <el-button :icon="SwitchButton" circle  @click="changeBg"/>
          
                  </span> -->
          <el-dropdown>
            <el-icon style="right: 2%;" color="#334155" size="170%"
              ><setting
            /></el-icon>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click.enter="goinfo">Your Information</el-dropdown-item>
                <el-dropdown-item @click.enter="changesettings">Settings</el-dropdown-item>
                <el-dropdown-item @click.enter="logout">Signed Out</el-dropdown-item>
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
                    <el-icon><message /></el-icon>All Users
                  </template>
                  <el-menu-item-group>
                    <template #title>Merchant</template>
                    <el-menu-item index="1-2">merchents</el-menu-item>
                  </el-menu-item-group>
                  <el-menu-item-group title="User">
                    <el-menu-item index="1-3">users</el-menu-item>
                  </el-menu-item-group>
                </el-sub-menu>
                <el-sub-menu index="2">
                  <template #title>
                    <el-icon><icon-menu /></el-icon>All Stores
                  </template>
                  <el-menu-item-group>
                    <template #title>Store</template>
                    <el-menu-item index="store" @click="goto('/seller/index/store')">stores</el-menu-item>
                  </el-menu-item-group>
                  <el-menu-item-group title="Request">
                    <el-menu-item index="request" @click="gotoRequestPage">requests</el-menu-item>
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
import { Edit } from '@element-plus/icons-vue'
import { useRouter } from "vue-router";
const changesettings=()=>{
  // if(bg_op.value==false){
  //   bg_op.value=true;
  // }else{
  //   bg_op.value=false;
  // }
};

const goinfo=()=>{
  // not implemented
};
const router = useRouter();
const gotoRequestPage = () => {
  router.push("/admin/index/request");
};
const gotoStore=()=>{
  router.push("/admin/index/store");
}
const logout=()=>{
  // if(bg_op.value==false){
  //   bg_op.value=true;
  // }else{
  //   bg_op.value=false;
  // }
  router.push("/");
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
</style>