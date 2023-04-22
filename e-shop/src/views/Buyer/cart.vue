<template>
  cart+{{carNum}}
  <div v-for="(item,index) in cart" :key="index">
    {{item.merchantName}} {{item.picture}} {{item.price}} {{item.quantity}} {{item.goodsName}}
  </div>
</template>

<script setup>
import  {useCounterStore} from "../../stores/counter"
import {useRouter} from "vue-router"
import { reactive ,ref} from "vue";
const router=useRouter();
const counter =useCounterStore();
const userType=counter.userType;
const userName=counter.userName;
const cart=reactive(counter.cart);
const cartNum=ref(counter.cartNum);
</script>

<style scoped>

</style>