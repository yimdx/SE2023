<template>
  <el-table :data="cart" :border="true" style="width: 100%;margin-top:0;margin-left:0">
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
          <p m="t-0 b-2">Name: {{ props.row.goodsName }}</p>
          <p m="t-0 b-2">Merchant Name: {{ props.row.merchantName }}</p>
          <p m="t-0 b-2">UnitPrice: {{ props.row.unitPrice }}</p>
          <p m="t-0 b-2">Quantity: {{ props.row.quantity }}</p>
          </div>
          <div style="position:absolute;left:30%;top:80%"><span style="color:red;font:25px red">Total:</span> 
           &nbsp;<span style="color:grey;font-size:20px">￥</span>
           <span style="font-size:25px">{{props.row.unitPrice*props.row.quantity}}</span></div>
        </div>
      </template>
    </el-table-column>
    <el-table-column label="Name" prop="goodsName" />
    <el-table-column label="Merchant Name" prop="merchantName" />
    <el-table-column label="UnitPrice" prop="unitPrice" />
    <el-table-column label="Quantity"  >
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
          @click="handleDelete(scope.$index, scope.row)"
          >Delete</el-button
        >
      </template>
    </el-table-column>
   
  </el-table>
  <!-- <div v-for="(item,index) in cart" :key="index">
    {{item.merchantName}} {{item.picture}} {{item.price}} {{item.quantity}} {{item.goodsName}}
  </div> -->
   <div style="position:absolute;left:80%;top:80%" class="total"><span style="color:red;font:25px red">Total:</span> 
           &nbsp;<span style="color:grey;font-size:20px">￥</span>
      <span style="font-size:25px">{{totalCost}}</span>
      <div></div>
         <el-button
          size="large"
          type="info"
          @click="buy"
          style="border-radius:15px;width:100px"
          >BUY</el-button
        >
      </div>

        <el-dialog
    v-model="centerDialogVisible"
    title="Confirm Purchase"
    width="30%"
    align-center
  >
    <span>Check carefully that these items are what you wat to buy.</span>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="centerDialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="confirmPurchase">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, getCurrentInstance , reactive} from "vue";
import  {useCounterStore} from "../../stores/counter"
import {useRouter} from "vue-router"
import {ElNotification} from "element-plus"

let { proxy } = getCurrentInstance();
const router=useRouter();
const counter =useCounterStore();
counter.cart.forEach(item=>{
  item.maxQuantity=item.quantity;
});
const userType=counter.userType;
const userName=counter.userName;
const cart=reactive(counter.cart);
cart.push({
    merchantName:"Li Hua",
    goodsName:"apple",
    unitPrice:1.015,
    quantity:3,
    picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
});
const cartNum=ref(counter.cartNum);
const totalCost=ref(counter.totalCost);
const centerDialogVisible=ref(false);
function handleChange(current,old){
  if(current<old){
     counter.cartNum--;
  checkDelete();
  }else counter.cartNum++;

  getTotal();
}
function checkDelete(){
  for(let i=0;i<cart.length;i++){
    if(cart[i].quantity===0) handleDelete(i,cart[i]);
  }
}
function handleDelete(index,item){
  for(let i=index;i<cart.length-1;i++)
  {
    cart[i]=cart[i+1];
  }
  cart.pop();
  getTotal();
  counter.cartNum-=item.quantity;
}
function getTotal(){
  counter.totalCost=0;
  for(let i=0;i<cart.length;i++){
    counter.totalCost+=cart[i].quantity*cart[i].unitPrice;
  }
  totalCost.value=counter.totalCost;
}
function buy(){
  centerDialogVisible.value=true;
}
function confirmPurchase(){
  //api create order
  let k=cart.length;
  //create order number
    proxy.$http
      .post("/buyer/order/create", {
        username: username.value,
      })
      .then(function (res) {
        let orderId=res.data.result;
         for(let i=0;i<k;++i){
            //send one item
              proxy.$http
              .post("/buyer/order/orderItem", {
                orderId:orderId,
                goodsName:cart[i].goodsName,
                merchantName:cart[i].merchantName,
                quantity:cart[i].quantity,
                unitPrice:cart[i].unitPrice,
              })
              .then(function (res) {
                console.log("order item "+i+" has been created");
                if(i===k-1){
                  router.push("/buyer/index/pay?orderId="+orderId);
                  ElNotification({
                    title: 'Success',
                    message: 'Order Successfully!',
                    type: 'success',
                  })
                }
              }).catch(err=>{
                console.log("order item" +i+' failed to be added');
              })

          }
      })
      .catch(function (error) {
        ElNotification({
          title: "Error",
          message: "Couldn't get order number",
          type: "Error",});
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