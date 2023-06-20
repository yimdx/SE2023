<template>
<div>
    <el-card>
        <el-breadcrumb separator-class="el-icon-arrow-right" style="margin-top:30">
            <el-breadcrumb-item>Orders</el-breadcrumb-item>
            <el-breadcrumb-item>All</el-breadcrumb-item>
        </el-breadcrumb>

        <el-button
        @click="getAllOrder()">
        所有订单    
        </el-button>
        <el-button
        @click="getNotPaidOrder()">
        未支付    
        </el-button>
        <el-button     
        @click="getPaidOrder()">
            已支付
        </el-button>
        <el-button
        @click="getCanceledOrder()">
            已撤销
        </el-button>

        <el-table :data="orderList" :border="true" style="width: 100%;margin-top:30;margin-left:0">
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
                <p m="t-0 b-2">Order Number: {{ props.row.orderId }}</p>
                <p m="t-0 b-2">Total Price: {{ props.row.totalPrice }}</p>
                <p m="t-0 b-2">Create time: {{ props.row.createTime }}</p>
                <p m="t-0 b-2">Status: {{ props.row.status }}</p>
                </div>
                <div style="position:absolute;left:30%;top:80%"><span style="color:red;font:25px red">Total:</span> 
                &nbsp;<span style="color:grey;font-size:20px">￥</span>
                <!-- <span style="font-size:25px">{{props.row.unitPrice*props.row.quantity}}</span></div> -->
                </div>
                </div>
            </template>
            </el-table-column>
            <el-table-column label="Order Number" prop="orderId" />
            <el-table-column label="Total Price" prop="totalPrice" />
            <el-table-column label="Create time" prop="createTime" />
            <el-table-column label="Status" prop="status" >            
            </el-table-column>

            <el-table-column label="Operations">
            <template #default="scope">
                <el-button
                size="small"
                type="danger"
                @click="showMore(scope.$index, scope.row)"
                >showMore</el-button
                >
                <el-button
                size="small"
                type="danger"
                @click="handleCancel(scope.$index, scope.row)"
                >Cancel</el-button
                >
                <el-button
                size="small"
                type="danger"
                @click="handlePay(scope.$index, scope.row)"
                >Pay</el-button
                >
            </template>
            </el-table-column>
        
        </el-table>

    </el-card>
</div>
</template>

<script setup>
import  {useCounterStore} from "../../stores/counter"
import { ElNotification } from "element-plus";
import {useRouter} from "vue-router"
import { reactive ,ref, getCurrentInstance} from "vue";
const router=useRouter();
const counter =useCounterStore();
counter.cart.forEach(item=>{
  item.maxQuantity=item.quantity;
});
const orderList = ref([])
const orderId = ref("")
const userType=counter.userType;
const userName=ref(counter.userName);
const cart=reactive(counter.cart);
const cartNum=ref(counter.cartNum);
const totalCost=ref(counter.totalCost);
let {proxy}= getCurrentInstance();
function handleChange(current,old){
  if(current<old){
     counter.cartNum--;
  checkDelete();
  }else counter.cartNum++;

  getTotal();
}

function getAllOrder(){
    // orderList.value.push({
    // orderId:"000",
    // totalPrice:"100.22",
    // createTime:"10:22",
    // status:"paid"
    // });
    // orderList.value.push({
    // orderId:"000",
    // totalPrice:"100.22",
    // createTime:"10:22",
    // status:"paid"
    // });
    proxy.$http
      .post("/buyer/order/orderAll", {
        userName: userName.value,
      })
      .then(function (res) {
         orderList.value=res.data.result;
         console.log(res.data.result)
      })
      .catch(function (error) {
        console.log(error);
        ElNotification({
          title: "Error",
          message: "getAllOrder Failed(Something must go wrong!)",
          type: "error",});
      });
}

getAllOrder();

function getNotPaidOrder(){ 
    proxy.$http
      .post("/buyer/order/notPaid", {
        userName: userName.value,
      })
      .then(function (res) {
         orderList.value=res.data.result;
         console.log(res.data.result)
      })
      .catch(function (error) {
        console.log(error);
        
        ElNotification({
          title: "Error",
          message: "getNotPaidOrder Failed(Something must go wrong!)",
          type: "error",});
      });
}

function getPaidOrder(){
    proxy.$http
      .post("/buyer/order/paid", {
        userName: userName.value,
      })
      .then(function (res) {
         orderList.value=res.data.result;
         console.log(res.data.result)
      })
      .catch(function (error) {
        console.log(error);
        
        ElNotification({
          title: "Error",
          message: "getPaidOrder Failed(Something must go wrong!)",
          type: "error",});
      });
}

function getCanceledOrder(){
    proxy.$http
      .post("/buyer/order/canceled", {
        userName: userName.value,
      })
      .then(function (res) {
         orderList.value=res.data.result;
      })
      .catch(function (error) {
        console.log(error);
        
        ElNotification({
          title: "Error",
          message: "getCanceledOrder Failed(Something must go wrong!)",
          type: "error",});
      });
}

function handlePay(index,item){
    router.push("/buyer/index/pay?orderId="+item.orderId);
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
          message: "Cancel Failed(Something must go wrong!)",
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