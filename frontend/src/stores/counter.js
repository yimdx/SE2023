import { ref, computed,reactive } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let userName =ref("");
  let userType =ref("");
  let cart=reactive([]);
  let cartNum=ref(0);
  let totalCost=ref(0.0);
  return {userName,userType,cart,cartNum,totalCost}
})
