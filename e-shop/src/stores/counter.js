import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let userName =ref("");
  let userType =ref("");
  return {userName,userType}
})
