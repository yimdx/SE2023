<template>
<div>
    <el-card>
        <el-breadcrumb separator-class="el-icon-arrow-right" style="margin-top:30">
            <el-breadcrumb-item>Orders</el-breadcrumb-item>
            <el-breadcrumb-item>All</el-breadcrumb-item>
        </el-breadcrumb>

        <el-button
        @click="showNotPaid(scope.$index, scope.row)">
        未支付    
        </el-button>
        <el-button     
        @click="showPaid(scope.$index, scope.row)">
            已支付
        </el-button>
        <el-button
        @click="showCanceled(scope.$index, scope.row)">
            已撤销
        </el-button>

        <el-table :data="cart" :border="true" style="width: 100%;margin-top:30;margin-left:0">
            <el-table-column type="expand">
            <template #default="props">
                <div m="4" class="expand">
                <h class="title"><strong>Details:</strong></h>
                <img
                :src="props.row.picture"
                class="image"
                @click="showMore(index,item)"
                />
                <div class="des">
                <p m="t-0 b-2">Order Number: {{ props.row.goodsName }}</p>
                <p m="t-0 b-2">Total Price: {{ props.row.merchantName }}</p>
                <p m="t-0 b-2">Create time: {{ props.row.unitPrice }}</p>
                <p m="t-0 b-2">Status: {{ props.row.quantity }}</p>
                </div>
                <div style="position:absolute;left:30%;top:80%"><span style="color:red;font:25px red">Total:</span> 
                &nbsp;<span style="color:grey;font-size:20px">￥</span>
                <span style="font-size:25px">{{props.row.unitPrice*props.row.quantity}}</span></div>
                </div>
            </template>
            </el-table-column>
            <el-table-column label="Order Number" prop="goodsName" />
            <el-table-column label="Total Price" prop="merchantName" />
            <el-table-column label="Create time" prop="unitPrice" />
            <el-table-column label="Status"  >
            <template #default="scope">
                <el-input-number
                v-model="scope.row.quantity"
                class="mx-4"
                :min="0"
                :max="scope.row.maxQuantity"
                controls-position="right"
                @change="handleChange"
            />
            </template>
            
            </el-table-column>

            <el-table-column label="Operations">
            <template #default="scope">
                <el-button
                size="small"
                type="danger"
                @click="showMore(scope.$index, scope.row)"
                >Delete</el-button
                >
                <el-button
                size="small"
                type="danger"
                @click="handleCancel(scope.$index, scope.row)"
                >Delete</el-button
                >
                <el-button
                size="small"
                type="danger"
                @click="handlePay(scope.$index, scope.row)"
                >Delete</el-button
                >
            </template>
            </el-table-column>
        
        </el-table>

    </el-card>
  <!-- <div v-for="(item,index) in cart" :key="index">
    {{item.merchantName}} {{item.picture}} {{item.price}} {{item.quantity}} {{item.goodsName}}
  </div> -->
</div>
</template>

<script setup>
import  {useCounterStore} from "../../stores/counter"
import {useRouter} from "vue-router"
import { reactive ,ref} from "vue";
const router=useRouter();
const counter =useCounterStore();
counter.cart.forEach(item=>{
  item.maxQuantity=item.quantity;
});

const userType=counter.userType;
const userName=counter.userName;
const cart=reactive(counter.cart);
const cartNum=ref(counter.cartNum);
const totalCost=ref(counter.totalCost);
function handleChange(current,old){
  if(current<old){
     counter.cartNum--;
  checkDelete();
  }else counter.cartNum++;

  getTotal();
}

function getAllOrder(){
    proxy.$http
      .post("/buyer/order/all", {
        userName: userName,
      })
      .then(function (res) {
         orderList=res.data.result;
      })
      .catch(function (error) {
        console.log(error);
        
        ElNotification({
          title: "Error",
          message: "Recharge Failed(Something must go wrong!)",
          type: "error",});
      });
}

function getNotPaidOrder(){
    proxy.$http
      .post("/buyer/order/notPaid", {
        userName: userName,
      })
      .then(function (res) {
         orderList=res.data.result;
      })
      .catch(function (error) {
        console.log(error);
        
        ElNotification({
          title: "Error",
          message: "Recharge Failed(Something must go wrong!)",
          type: "error",});
      });
}

function getPaidOrder(){
    proxy.$http
      .post("/buyer/order/paid", {
        userName: userName,
      })
      .then(function (res) {
         orderList=res.data.result;
      })
      .catch(function (error) {
        console.log(error);
        
        ElNotification({
          title: "Error",
          message: "Recharge Failed(Something must go wrong!)",
          type: "error",});
      });
}

function getCanceledOrder(){
    proxy.$http
      .post("/buyer/order/canceled", {
        userName: userName,
      })
      .then(function (res) {
         orderList=res.data.result;
      })
      .catch(function (error) {
        console.log(error);
        
        ElNotification({
          title: "Error",
          message: "Recharge Failed(Something must go wrong!)",
          type: "error",});
      });
}

function handlePay(index,item){
    router.push("/buyer/index/pay");
}

function handleCanceled(index,item){
   proxy.$http
      .post("/buyer/order/cancelOrder", {
        userName:userName, 
        orderNumber:item.orderNumber
      })
      .then(function (res) {
         console.log("success add");
        newItem.name="";
        newItem.description="";
        newItem.picture="";
        newItem.price="";
        newItem.stock="";

        addGoodDialogVisible.value=false;
      })
      .catch(function (error) {
        console.log(error)
        ElNotification({
          title: "Error",
          message: "Add Commodity Failed(Something must go wrong!)",
          type: "error",});

      });
}

</script>

<style scoped>

.image{
 position: relative;
 height: 200px;
 width: 160px;
 left:12%;
 margin-top:15px;

}
.expand{
  height: 230px;
  width: 98%;
  position: relative;
  left: 1%;
  background: linear-gradient(to right,rgb(241, 223, 223),rgb(187, 187, 206));
  margin-right: 10px;
  margin-top:0;
  margin-bottom:0;
  padding-right: 10px;
  border-radius: 10px;
}
.title{
  font-size: 25px;
  margin: 10px;
  position: absolute;
  top:0%;
  
}
.des{
  position: absolute;
  left: 30%;
  top:0%;
  margin-top: 15px;
  font-size: 20px;
}
</style>