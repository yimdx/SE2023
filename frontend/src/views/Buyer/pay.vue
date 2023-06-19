<template>
  <el-table
    :data="order"
    :border="true"
    style="width: 100%; margin-top: 0; margin-left: 0"
  >
    <el-table-column type="expand">
      <template #default="props">
        <div m="4" class="expand">
          <h class="title"><strong>Details:</strong></h>
          <img
            :src="props.row.picture"
            class="image"
            @click="showMore(index, item)"
          />
          <div class="des">
            <p m="t-0 b-2">Name: {{ props.row.goodsName }}</p>
            <p m="t-0 b-2">Merchant Name: {{ props.row.merchantName }}</p>
            <p m="t-0 b-2">UnitPrice: {{ props.row.unitPrice }}</p>
            <p m="t-0 b-2">Quantity: {{ props.row.quantity }}</p>
          </div>
          <div style="position: absolute; left: 30%; top: 80%">
            <span style="color: red; font: 25px red">Total:</span> &nbsp;<span
              style="color: grey; font-size: 20px"
              >￥</span
            >
            <span style="font-size: 25px">{{
              props.row.unitPrice * props.row.quantity
            }}</span>
          </div>
        </div>
      </template>
    </el-table-column>
    <el-table-column label="Name" prop="goodsName" />
    <el-table-column label="Merchant Name" prop="merchantName" />
    <el-table-column label="UnitPrice" prop="unitPrice" />
    <el-table-column label="Quantity" prop="quantity" />
  </el-table>
  <!-- <div v-for="(item,index) in cart" :key="index">
    {{item.merchantName}} {{item.picture}} {{item.price}} {{item.quantity}} {{item.goodsName}}
  </div> -->
  <div style="position: absolute; left: 80%; top: 80%" class="total">
    <span style="color: red; font: 25px red">Total:</span> &nbsp;<span
      style="color: grey; font-size: 20px"
      >￥</span
    >
    <span style="font-size: 25px">{{ totalCost }}</span>
    <div></div>
    <el-button
      size="large"
      type="info"
      @click="buy"
      style="border-radius: 15px; width: 100px"
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
        <el-button type="primary" @click="confirmPurchase"> Confirm </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { useCounterStore } from "../../stores/counter";
import { useRouter } from "vue-router";
import { reactive, ref } from "vue";
import { ElNotification } from "element-plus";
const router = useRouter();
const counter = useCounterStore();
const userType = counter.userType;
const userName = counter.userName;
const order = ref([]);
const centerDialogVisible = ref(false);
const totalCost = ref(0.0);
let { orderId } = router.currentRoute.value.query;
function fetchOrder() {
  console.log(orderId);
  //api fetch order info from order id
  proxy.$http
    .post("/buyer/order/orderInfo", {
      orderId: orderId
    })
    .then(function (res) {
      order.value=res.data.result;
    })
    .catch((err) => {
       ElNotification({
          title: "Error",
          message: "Couldn't get order info",
          type: "Error",});
    });
}
fetchOrder();
function getTotal() {
  totalCost.value = 0;
  for (let i = 0; i < order.value.length; i++) {
    totalCost.value += order.value[i].quantity * order.value[i].unitPrice;
  }
}

getTotal();
function buy() {
  centerDialogVisible.value = true;
}
function confirmPurchase() {
  //api buy

      proxy.$http
      .post("/buyer/order/pay", {
        orderId: orderId
      })
      .then(function (res) {
         ElNotification({
          title: "Success",
          message: "Purchase Successfully!",
          type: "success",
        });
        router.push("/buyer/index/order");
      })
      .catch((err) => {
        ElNotification({
            title: "Error",
            message: "Fail to purchase",
            type: "Error",});
      });
 
}
</script>

<style scoped>
.image {
  position: relative;
  height: 200px;
  width: 160px;
  left: 12%;
  margin-top: 15px;
}
.expand {
  height: 230px;
  width: 98%;
  position: relative;
  left: 1%;
  background: linear-gradient(to right, rgb(241, 223, 223), rgb(187, 187, 206));
  margin-right: 10px;
  margin-top: 0;
  margin-bottom: 0;
  padding-right: 10px;
  border-radius: 10px;
}
.title {
  font-size: 25px;
  margin: 10px;
  position: absolute;
  top: 0%;
}
.des {
  position: absolute;
  left: 30%;
  top: 0%;
  margin-top: 15px;
  font-size: 20px;
}
</style>