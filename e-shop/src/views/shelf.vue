<template>
<div class="all">
<div class="shop-header">
    <div class="left">Merchant Name: {{merchantName}}</div>
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
          @click="showMore(index,item)"
        />
        <div style="padding:20px" @click="showMore(index,item)">
          <span class="title">{{item.name}}</span>
          <span class="price"><span style="font-size:20px">￥</span>{{item.price}} </span>
          <div class="bottom" >
            Stock:{{item.stock}} 
          </div>
         
          <el-tag :type="getType(item,index)" class="status" >{{item.submitStatus}}</el-tag>
        </div>
         <div class="addCart" @click="addCart(item,index)"><el-icon size="20"><Goods /></el-icon><span style="font-size:10px">BUY</span></div>
          <div v-show="crossVisible" class="delete" @click="deleteGood(item,index)"><el-icon size="20"><Close /></el-icon></div>
      </el-card>
      
    </div>
    <div class="footer"></div>
</div>


<div class="cart" >
     <el-badge :value="cartNum">
        <el-icon size="100" @click="gotoCart"><ShoppingCart />
    </el-icon> 
    </el-badge>
</div> 
<el-dialog class="addForm" v-model="addGoodDialogVisible" title="Add a new item" draggable>
    
     <el-form
    label-position="left"
    label-width="100px"
    :model="newItem"
    style="max-width: 460px"
    class="form"
  >
    <el-form-item label="Name" class="item">
      <el-input v-model="newItem.name" />
      <el-alert type="info" show-icon :closable="false" class="hint">
        <p>characters</p>
      </el-alert>
    </el-form-item>
    <el-form-item label="Picture(url)" class="item">
      <el-input v-model="newItem.picture" />
      <el-alert type="info" show-icon :closable="false" class="hint">
        <p>url</p>
      </el-alert>
    </el-form-item>
    <el-form-item label="Description" class="item">
      <el-input  type="textarea" v-model="newItem.description" :rows="4" />
      <el-alert type="info" show-icon :closable="false" class="hint-long">
        <p>sentences</p>
      </el-alert>
    </el-form-item>
    <el-form-item label="Price" class="item">
      <el-input v-model="newItem.price" />
      <el-alert type="info" show-icon :closable="false" class="hint">
        <p>float</p>
      </el-alert>
    </el-form-item>
    <el-form-item label="Stock" class="item">
      <el-input v-model="newItem.stock" />
      <el-alert type="info" show-icon :closable="false" class="hint">
        <p>integer</p>
      </el-alert>
    </el-form-item>
  </el-form>

    <template #footer>
      <span class="dialog-footer">
        <el-button @click="cancelAdd">Cancel</el-button>
        <el-button type="primary" @click="confirmAdd">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>

 <el-dialog v-model="showMoreVisible" title="Good Info" draggable>
        <el-descriptions title="" :column="3" border>
    <el-descriptions-item
      label="Name"
      label-align="right"
      align="center"
      label-class-name="my-label"
      class-name="my-content"
      width="150px"
      >{{showInfo.name}}</el-descriptions-item
    >
    
    <el-descriptions-item label="Price" label-align="right" align="center" width="150px"
      >￥{{showInfo.price}}</el-descriptions-item
    >
   
    <el-descriptions-item label="Stock" label-align="right" align="center"
      >{{showInfo.stock}}</el-descriptions-item
    >
     <el-descriptions-item label="Status" label-align="right" align="center">
      <el-tag :type="getType(showInfo,0)" size="small">{{showInfo.submitStatus}}</el-tag>
    </el-descriptions-item>

     <el-descriptions-item label="" label-align="right" align="center"
      ></el-descriptions-item
    >
    <el-descriptions-item label="" label-align="right" align="center"
      ></el-descriptions-item
    >
    <el-descriptions-item label="Description" label-align="right" align="center"
      >{{showInfo.description}}</el-descriptions-item
    >
  </el-descriptions>
  <div v-show="crossVisible && canEdit" class="edit-btn" @click="editShow">Update Information</div>
  <div v-show="editVisible">
     <el-form
    label-position="left"
    label-width="100px"
    :model="newItem"
    style="max-width: 460px"
    class="form"
  >
    <el-form-item label="Name" class="item">
      <el-input v-model="newItem.name" />
      <el-alert type="info" show-icon :closable="false" class="hint">
        <p>characters</p>
      </el-alert>
    </el-form-item>
    <el-form-item label="Picture(url)" class="item">
      <el-input v-model="newItem.picture" />
      <el-alert type="info" show-icon :closable="false" class="hint">
        <p>url</p>
      </el-alert>
    </el-form-item>
    <el-form-item label="Description" class="item">
      <el-input  type="textarea" v-model="newItem.description" :rows="4" />
      <el-alert type="info" show-icon :closable="false" class="hint-long">
        <p>sentences</p>
      </el-alert>
    </el-form-item>
    <el-form-item label="Price" class="item">
      <el-input v-model="newItem.price" />
      <el-alert type="info" show-icon :closable="false" class="hint">
        <p>float</p>
      </el-alert>
    </el-form-item>
    <el-form-item label="Stock" class="item">
      <el-input v-model="newItem.stock" />
      <el-alert type="info" show-icon :closable="false" class="hint">
        <p>integer</p>
      </el-alert>
    </el-form-item>
     
  </el-form>
    <div  class="edit-btn" @click="confirmUpdate">Confirm</div>
  </div>
    </el-dialog>
</div>
  
  
</template>

<script setup>
import  {useCounterStore} from "../stores/counter"
import {useRouter} from "vue-router"
import { onMounted ,ref,reactive} from "vue";
import { Goods ,ShoppingCart,Close} from "@element-plus/icons-vue";
import {goodsNameCheck,goodsDescriptionCheck,priceCheck,pictureCheck,stockCheck} from "../utils/regressionCheck"
const counter=useCounterStore();
const userType=counter.userType;
let canEdit=ref(false);
const crossVisible=userType==="seller";
const addGoodDialogVisible=ref(false);
const showMoreVisible=ref(false);
const router=useRouter();
const {shopName} =router.currentRoute.value.query;
let goodsList=[];
let merchantName="";
const cartNum=ref(0);
const newItem = reactive({
     name:"",
    description:"",
    picture:"",
    price:"",
    stock:"",
});
const showInfo=reactive({
    name:"",
    description:"",
    picture:"",
    price:"",
    stock:"",
    submitStatus:""
});


function getGoodsList(){
    goodsList.push({
        name:"apple",
        description:"sweet",
        picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:0,
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
    };
    //api get merchantName
    merchantName="Li Hua";

    cartNum.value=counter.cartNum;
};
getGoodsList();
function getType(item,index){
    if(item.submitStatus==="up") return "success";
    else return "danger"

}
function addGood(){
    addGoodDialogVisible.value=true;
}
function cancelAdd(){
    addGoodDialogVisible.value=false;
    newItem.name="";
    newItem.description="";
    newItem.picture="";
    newItem.price="";
    newItem.stock="";
}
function confirmAdd(){
    //api confirm add
    //check
    if(!goodsNameCheck(newItem.name)){
        newItem.name="";
        console.log("name check failed")
        return;
    }
     console.log("name check passed")
     console.log(newItem.description)
    if(!goodsDescriptionCheck(newItem.description)){
        newItem.description="";
         console.log("description check failed")
        return;
    }
     console.log("description check passed")
    if(!pictureCheck(newItem.picture)){
        newItem.picture="";
         console.log("picture check failed")
        return;
    }
     console.log("picture check passed")
    if(!priceCheck(newItem.price)){
        newItem.price="";
         console.log("price check failed")
        return;
    }
     console.log("price check passed")
    if(!stockCheck(newItem.stock)){
        newItem.stock="";
         console.log("stock check failed")
        return;
    }
     console.log("stock check passed")
    console.log("success add");
    newItem.name="";
    newItem.description="";
    newItem.picture="";
    newItem.price="";
    newItem.stock="";

    addGoodDialogVisible.value=false;
}

function confirmUpdate(){
    //api confirm add
    //check
    if(!goodsNameCheck(newItem.name)){
        newItem.name="";
        console.log("name check failed")
        return;
    }
     console.log("name check passed")
     console.log(newItem.description)
    if(!goodsDescriptionCheck(newItem.description)){
        newItem.description="";
         console.log("description check failed")
        return;
    }
     console.log("description check passed")
    if(!pictureCheck(newItem.picture)){
        newItem.picture="";
         console.log("picture check failed")
        return;
    }
     console.log("picture check passed")
    if(!priceCheck(newItem.price)){
        newItem.price="";
         console.log("price check failed")
        return;
    }
     console.log("price check passed")
    if(!stockCheck(newItem.stock)){
        newItem.stock="";
         console.log("stock check failed")
        return;
    }
     console.log("stock check passed");
     if(newItem.name===showInfo.name && newItem.description===showInfo.description 
     && newItem.price===showInfo.price && newItem.stock === showInfo.stock
     && newItem.picture === showInfo.picture){
        return;
     }
    console.log("success update");

}
function showMore(index,item){
    showMoreVisible.value=true;
    showInfo.name=item.name;
    showInfo.description=item.description;
    showInfo.picture=item.picture;
    showInfo.price=item.price;
    showInfo.stock=item.stock;
    showInfo.submitStatus=item.submitStatus;
    canEdit.value=(showInfo.submitStatus==="up");
     newItem.name=showInfo.name;
    newItem.description=showInfo.description;
    newItem.picture=showInfo.picture;
    newItem.price=showInfo.price;
    newItem.stock=showInfo.stock;
}
const editVisible=ref(false);
function editShow(){
    editVisible.value=!editVisible.value;
}
function deleteGood(item,index){
    //api delete good
    alert(item.name);
}
function addCart(item,index){
    if(item.stock===0){
        return;
    }
    let flag=false;
    let idx=-1;
    counter.cart.forEach((o,index)=>{
        if(o.merchantName===merchantName && o.goodsName===item.name){
            o.quantity++;
            flag=true;
            idx=index;
        }
    });
    if(idx!==-1 && counter.cart[idx].quantity> item.stock){
        counter.cart[idx].quantity=item.stock;
        return;
    }
    if(flag===false){
        counter.cart.push({
            merchantName:merchantName,
            goodsName:item.name,
            picture:item.picture,
            unitPrice:item.price,
            quantity:1
        })
    };
    counter.cartNum++;
    console.log(counter.cart)
     cartNum.value=counter.cartNum;
}
function gotoCart(){
    router.push("/buyer/index/cart");
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
.delete{
    position: absolute;
    right: 10px;
    top:10px;
}
.delete:hover{
    transform: scale(1.2);
}

.cart{
    position: fixed;
    right: 1%;
    bottom: 1%;
    cursor: pointer;
    height: 100px;
    width: 100px;
}
.addForm{
    position: fixed;
    
}
.form{
    margin: 0%;
    padding-top: 10px;
    padding-bottom: 3px;
    background: #f4f4f5;
    border-radius: 10px;
    padding-left: 10px;
}
.item{
    display: flex;
}
.hint{
    position: absolute;
    right: -93%;
    width: 90%;
    height: 60px;
    border-radius: 5px;
    margin:10px;
    top:-60%;
    overflow: hidden;
}
.hint-long{
    position: absolute;
    right: -93%;
    width: 90%;
    height: 60px;
    border-radius: 5px;
    margin:10px;
    top:-10px;
    overflow: hidden;
}
.edit-btn{
    margin-top: 15px;
     margin-bottom: 15px;
    position: relative;
    color: rgb(0, 144, 144);
    font-size: 16px;
}
.edit-btn:hover{
    cursor: pointer;
    color: plum;

}

</style>