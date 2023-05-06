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
      <span style="font-size:25px">{{totalCost}}</span></div>
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