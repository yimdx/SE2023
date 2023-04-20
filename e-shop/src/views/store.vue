<template>
   <el-card>
      <el-table :data="userlist" border stripe>
      <el-table-column type="index"></el-table-column>
      <el-table-column label="ShopName" prop="shopName"></el-table-column>
      <el-table-column label="Address" prop="email"></el-table-column>
      <el-table-column label="ShopInfo" prop="mobile"></el-table-column>
      <el-table-column label="StartTime" prop="role_name"></el-table-column>
      <el-table-column label="Goods" prop="role_name"></el-table-column>
      <el-table-column label="Status" prop="mg_state">
        <template v-slot="scope">
          <el-switch v-model="scope.row.mg_state" />
        </template>
      </el-table-column>
    </el-table>
   </el-card>
</template>



<script setup>
import { ElNotification } from "element-plus";
import { ref, getCurrentInstance } from "vue";
import { Unlock, User, Avatar } from "@element-plus/icons-vue";
import { useRouter } from "vue-router";
import { usernameCheck, passwordCheck } from "../utils/regressionCheck.js";
import {snow} from "../static/img-base64/snow"
img.src=snow;
var child = document.getElementById("canvas_sakura");
while(child){
    var parent=child.parentNode;
    parent.removeChild(child);
    child = document.getElementById("canvas_sakura")
}
startSakura();
child = document.getElementById("canvas_sakura")
var parent=child.parentNode;
parent.removeChild(child);
</script>

<script>

export default {
  data () {
    return {
       //预留字段
      queryInfo: {
        query: '', 
        pagenum: 1, 
        pagesize: 5 
      },
      storelist: [{shopName: "testshop", 
                   address: "address",
                   shopInfo: "shopinfo",
                   startTime: "starttime",
                   goods: "no goods",
                   status: "submitted" }],
      total: 0
    }
  },
  created () {
    this.getStoreList()
  },
  methods: {
      async getStoreList () {
      const { data: res } = await proxy.$http.post('/admin/index/stores', {
         params: this.queryInfo
      })
      if (res.meta.status !== 200) return this.$message.error('getting store list failed')
      this.storelist = res.data
      console.log(res)
      },
  }
}
</script>

<style>

.el-card{
    box-shadow: 0 1px 1px rgba(0,0,0,0.15) !important;
}
.el-table{
    margin-top: 15px;
    font-size: 12px;
}

</style>