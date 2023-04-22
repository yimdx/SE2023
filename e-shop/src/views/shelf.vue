<template>
<div class="all">
<div class="shop-header">
    <div class="left"></div>
    <div class="right">Shop Name : {{shopName}}</div>
</div>
<div class="body">
    <div v-show="crossVisible" class="card" @click="addGood">
        <img
        class="image" 
        style="height=100%"
        src="https://img1.baidu.com/it/u=2279237123,3956366328&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500"/>
    </div>
    <div
      v-for="(item, index) in goodsList"
      :key="index"
      class="card"
    >
      <el-card :body-style="{ padding: '2px' }" >
        <img
          :src="item.picture"
          class="image"
        />
        <div style="padding:20px">
          <span class="title">{{item.name}}</span>
          <span class="price"><span style="font-size:20px">￥</span>{{item.price}} </span>
          <div class="bottom">
            Stock:{{item.stock}} 
          </div>
          <div class="addCart"><el-icon size="20"><Goods /></el-icon><span style="font-size:10px">BUY</span></div>
          
          <el-tag :type="getType(item,index)" class="status">{{item.submitStatus}}</el-tag>
        </div>
      </el-card>
      
    </div>
    <div class="footer"></div>
</div>

<div class="cart"><el-icon><ShoppingCart /></el-icon></div>
</div>
  
</template>

<script setup>
import  {useCounterStore} from "../stores/counter"
import {useRouter} from "vue-router"
import { onMounted ,ref} from "vue";
import { Goods ,ShoppingCart} from "@element-plus/icons-vue";

const counter=useCounterStore();
const userType=counter.userType;
const crossVisible=userType==="seller";
const router=useRouter();
const {shopName} =router.currentRoute.value.query;
let goodsList=[];
function getGoodsList(){
    goodsList.push({
        name:"apple",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"up"
    });
    goodsList.push({
        name:"orange",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"down"
    });
     goodsList.push({
        name:"orange",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"down"
    });
 goodsList.push({
        name:"orange",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"down"
    });
    goodsList.push({
        name:"orange",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"down"
    });
    goodsList.push({
        name:"orange",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"down"
    });
     goodsList.push({
        name:"orange",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"down"
    });
     goodsList.push({
        name:"orange",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"down"
    });
    for(let i=0;i<10;i++){
           goodsList.push({
        name:"apple",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"up"
    });
    }
};
getGoodsList();
function getType(item,index){
    if(item.submitStatus==="up") return "success";
    else return "danger"

}
function addGood(){

}
</script>

<style scoped>

.all{
    margin:0px;
    padding:0px;
   height: calc(100%); 
overflow-y:scroll;
overflow-x:hidden;

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
  position: absolute;
  bottom: 17px;
  right: 16px;
  font-size: 15px;
  color:grey;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}
.title{
    font-size: 12px;
    text-align: center;
}

.price{
    font-size: 18px;
    position: absolute;
    right:10px;
    color: red;
}
.status{
    position: absolute;
    top:3%;
    left: 3%;
    
}
.shop-header{
    margin:120px 200px 0px 200px;
    padding: 12px;
    position: absolute;
    display: flex;
    width: 60%;
    height: 200px;
    background: white;
    border-radius: 10px;
}
.left{
position: relative;
 margin: 0;
 padding: 12px;
 background: red;
 height: 176px;
 width: 50%;
}
.right{
    position: relative;
 margin: 0;
 padding: 12px;
 background: blue;
 height: 176px;
 width: 50%;
}
.body{
    position: absolute;
    top:40%;
    margin:120px 200px 200px 200px;
    display: flex;
    width: 60%;
    background: white;
    border-radius: 10px;
    justify-content:left;
    flex-direction: row;
    flex-wrap: wrap;
    padding: 12px;
    padding-left: 40px;
    padding-top: 40px;

} 
.card{
    position: relative;
    display: block;
    height: 300px;
    width: 19%;
    border: solid 1px;
    margin: 1px;
    border-radius: 5px;

}
.card:hover{
    transform: scale(1.1);
    border: solid 1px red;
    z-index: 999;
}
.footer{
    height: 100px;
    width: 60%;
    margin: 0;
    padding: 0;
    display: block;
}
.addCart{
    position: absolute;
    left: 10%;
    bottom: 5%;
}
.addCart:hover{
    transform: scale(1.2);
    cursor: pointer;
}

.cart{
    position: fixed;
    right: 1%;
    bottom: 1%;
}

</style>