<template>
   <el-card>
      <div class="tableName">Opening Requset :</div>
      <el-table :data="storelist" border stripe>
         <el-table-column type="index"></el-table-column>
         <el-table-column label="ShopName" prop="shopName"></el-table-column>
         <el-table-column label="Address" prop="address"></el-table-column>
         <el-table-column label="ShopInfo" prop="shopIntro"></el-table-column>
         <el-table-column label="StartTime" prop="startTime"></el-table-column>
         <el-table-column label="Goods" prop="goodsType"></el-table-column>
         <el-table-column label="status" prop="submitStatus"></el-table-column>
         <el-table-column label="action">
            <template v-slot="scope">
            <el-tooltip effect="dark" content="approve the request" placement="top" :enterable="false">
               <el-button type="warning" size="mini" @click="approveRequest(scope.$index, scope.row)">Approve</el-button>
            </el-tooltip>
            </template>
         </el-table-column>
    </el-table>
    <div class="tableName">Deleting Requset :</div>
    <el-table :data="deltestorelist" border stripe>
         <el-table-column type="index"></el-table-column>
         <el-table-column label="ShopName" prop="shopName"></el-table-column>
         <el-table-column label="Address" prop="address"></el-table-column>
         <el-table-column label="ShopInfo" prop="shopIntro"></el-table-column>
         <el-table-column label="StartTime" prop="startTime"></el-table-column>
         <el-table-column label="Goods" prop="goodsType"></el-table-column>
         <el-table-column label="status" prop="submitStatus"></el-table-column>
         <el-table-column label="action">
            <template v-slot="scope">
            <el-tooltip effect="dark" content="approve the request" placement="top" :enterable="false">
               <el-button type="warning" size="mini" @click="approveDeleteRequest(scope.$index, scope.row)">Approve</el-button>
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
                   shopIntro: "shopinfo",
                   startTime: "starttime",
                   goodsType: "no goods",
                   submitStatus: "submitted" }],
      total: 0,
      deltestorelist: [{shopName: "testshop", 
                   address: "address",
                   shopIntro: "shopinfo",
                   startTime: "starttime",
                   goodsType: "no goods",
                   submitStatus: "submitted" }],
    }
  },
  created () {
    this.getStoreList()
    this.getDeleteStoreList()
  },
  methods: {
       getStoreList () {
         let that=this;
            this.$http
            .post('/admin/checkOpenningRequest')
            .then(function (res) {
               that.storelist = res.data.result;
            }).catch(err=>{
               console.log(err);
            });
      },

      getDeleteStoreList() {
         let that=this;
          this.$http
            .post('/admin/checkOpenningRequest')
            .then(function (res) {
               that.deletestorelist = res.data.result;
            }).catch(err=>{
               console.log(err);
            })
      },

      approveRequest(index,item){
         let that=this;
         console.log(that.storelist[index]);
         this.$http
         .post('/admin/checkOpenningRequest/Passed',
          that.storelist[index]
         )
         .then(function (res) {
          console.log(res.data);
          that.storelist = that.getStoreList()
         })
      .catch(function (error) {
         console.log(error);
         
         });
      },

      approveDeleteRequest(index,item){
         let that=this;
         console.log(that.deletestorelist[index]);
         this.$http
         .post('/admin/checkDeletingRequest/Passed',
          that.deletestorelist[index]
         )
         .then(function (res) {
          console.log(res.data);
          that.deletestorelist = that.getDeleteStoreList()
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