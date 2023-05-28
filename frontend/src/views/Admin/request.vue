<template>
   <el-card>
      <div class="tableName">Opening Requset :</div>
      <el-table :data="storelist" border stripe>
         <el-table-column type="index"></el-table-column>
         <el-table-column label="ShopName" prop="shopName"></el-table-column>
         <el-table-column label="Address" prop="address"></el-table-column>
         <el-table-column label="ShopInfo" prop="shopInfo"></el-table-column>
         <el-table-column label="StartTime" prop="startTime"></el-table-column>
         <el-table-column label="Goods" prop="goods"></el-table-column>
         <el-table-column label="status" prop="status"></el-table-column>
         <el-table-column label="action">
            <template v-slot="scope">
            <el-tooltip effect="dark" content="approve the request" placement="top" :enterable="false">
               <el-button type="warning" size="mini" @click="approveRequest(scope.row.index)">Approve</el-button>
            </el-tooltip>
            </template>
         </el-table-column>
    </el-table>
    <div class="tableName">Deleting Requset :</div>
    <el-table :data="storelist" border stripe>
         <el-table-column type="index"></el-table-column>
         <el-table-column label="ShopName" prop="shopName"></el-table-column>
         <el-table-column label="Address" prop="address"></el-table-column>
         <el-table-column label="ShopInfo" prop="shopInfo"></el-table-column>
         <el-table-column label="StartTime" prop="startTime"></el-table-column>
         <el-table-column label="Goods" prop="goods"></el-table-column>
         <el-table-column label="status" prop="status"></el-table-column>
         <el-table-column label="action">
            <template v-slot="scope">
            <el-tooltip effect="dark" content="approve the request" placement="top" :enterable="false">
               <el-button type="warning" size="mini" @click="approveRequest(scope.row.index)">Approve</el-button>
            </el-tooltip>
            </template>
         </el-table-column>
    </el-table>
   </el-card>

</template>



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
      total: 0,
      deltestorelist: [{shopName: "testshop", 
                   address: "address",
                   shopInfo: "shopinfo",
                   startTime: "starttime",
                   goods: "no goods",
                   status: "submitted" }],
    }
  },
  created () {
    this.getStoreList()
    this.getDeleteStoreList()
  },
  methods: {
       getStoreList () {
            this.$http
            .post('/admin/checkOpenningRequest')
            .then(function (res) {
               this.storelist = res.data.result;
            }).catch(err=>{
               console.log(err);
            });
      },

      getDeleteStoreList() {
          this.$http
            .post('/admin/checkOpenningRequest')
            .then(function (res) {
               this.deletestorelist = res.data.result;
            }).catch(err=>{
               console.log(err);
            })
      },

      approveRequest(index){
         this.$http
         .post('/admin/checkOpenningRequest/Passed',
          this.storelist[index]
         )
         .then(function (res) {
          console.log(res.data);
          this.storelist = this.getStoreList()
         })
      .catch(function (error) {
         console.log(error);
         
         });
      },

      approveDeleteRequest(index){
         this.$http
         .post('/admin/checkDeletingRequest/Passed',
          this.deletestorelist[index]
         )
         .then(function (res) {
          console.log(res.data);
          this.deletestorelist = this.getDeleteStoreList()
         })
      .catch(function (error) {
         console.log(error);
         });
      }
   
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