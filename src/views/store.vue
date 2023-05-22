<template>
  <el-card>
    <el-table :data="storelist" border stripe>
      <el-table-column type="index"></el-table-column>
      <el-table-column label="ShopName" prop="shopName"></el-table-column>
      <el-table-column label="Address" prop="address"></el-table-column>
      <el-table-column label="ShopInfo" prop="shopIntro"></el-table-column>
      <el-table-column label="StartTime" prop="startTime"></el-table-column>
      <el-table-column label="Goods" prop="goodsType"></el-table-column>
      <el-table-column label="Operations">
        <template #default="scope">
          <el-button size="small" @click="handleShowMore(scope.$index, scope.row)"
            >ShowMore</el-button
          >
          <el-button
            size="small"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            >Delete</el-button
          >
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="showMoreVisible" title="Store Info">
        <div @click="gotoShelf" class="gotoShelf">Go to Shelf</div>
        <el-descriptions title="" :column="3" border>
    <el-descriptions-item
      label="ShopName"
      label-align="right"
      align="center"
      label-class-name="my-label"
      class-name="my-content"
      width="150px"
      >{{showInfo.shopName}}</el-descriptions-item
    >
    <el-descriptions-item label="StartTime" label-align="right" align="center"
      >{{showInfo.startTime}}</el-descriptions-item
    >
    <el-descriptions-item label="Address" label-align="right" align="center" width="150px"
      >{{showInfo.address}}</el-descriptions-item
    >
    <el-descriptions-item label="ShopInfo" label-align="right" align="center"
      >{{showInfo.shopInfo}}</el-descriptions-item
    >
     <el-descriptions-item label="Goods" label-align="right" align="center"
      >{{showInfo.goods}}</el-descriptions-item
    >
  </el-descriptions>
    </el-dialog>
  </el-card>
</template>




<script>
import  {useCounterStore} from "../stores/counter"
export default {
  data() {
    return {
      //预留字段
      queryInfo: {
        query: "",
        pagenum: 1,
        pagesize: 5,
      },
      storelist: [
        {
          shopName: "testshop",
          address: "address",
          shopInfo: "shopinfo",
          startTime: "starttime",
          goods: "no goods",
          merchantName:"Li Hua",
        },
      ],
      total: 0,
      showMoreVisible:false,
      showInfo:{
        shopName: "",
        address: "",
        shopInfo: "",
        startTime: "",
        goods: "",
        merchantName:"",
      },
    };
  },
  created() {
    this.getStoreList();

  },
  methods: {
    async getStoreList() {
      //todo getMyStore

      this.storelist = [
        {
          shopName: "testshop",
          address: "address",
          shopInfo: "shopinfo",
          startTime: "starttime",
          goods: "no goods",
          status: "submitted",
          merchantName:'Li Hua',
        },
        {
          shopName: "testshop",
          address: "address",
          shopInfo: "shopinfo",
          startTime: "starttime",
          goods: "no goods",
          status: "passed",
          merchantName:'Li Hua',
        },
        {
          shopName: "testshop",
          address: "address",
          shopInfo: "shopinfo",
          startTime: "starttime",
          goods: "no goods44444444444444444444444444444444444444444444",
          status: "sendBack",
          merchantName:'Li Hua',
        },
      ];
      this.$http.post("/admin/index/stores")
      .then(res=>{
        this.storelist = res.data.result;
        console.log(this.storelist);
        console.log(res);
      }).catch(err=>{
        console.log(err);
      });
    },
    handleShowMore(index, row) {

      if(this.showMoreVisible===false) {
        this.showMoreVisible=true;
        this.showInfo.shopName=row.shopName;
        this.showInfo.shopInfo=row.shopIntro;
        this.showInfo.address=row.address;
        this.showInfo.startTime=row.startTime;
        this.showInfo.goods=row.goodsType;
        this.showInfo.merchantName=row.userName;
        console.log(this.showInfo)
    }
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
    gotoShelf(){
      const counter=useCounterStore();
     if(counter.userType==="admin") this.$router.push("/admin/index/shelf?shopName="+this.showInfo.shopName+"&merchantname="+this.showInfo.merchantName);
      else if (counter.userType==="seller") this.$router.push("/seller/index/shelf?shopName="+this.showInfo.shopName+"&merchantname="+this.showInfo.merchantName);
      else if(counter.userType==='buyer')  this.$router.push("/buyer/index/shelf?shopName="+this.showInfo.shopName+"&merchantname="+this.showInfo.merchantName);
      console.log(counter.userType);
    }
  },
};
</script>

<style scoped>
.el-card {
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15) !important;
}
.el-table {
  margin-top: 15px;
  font-size: 12px;
}
.gotoShelf{
  position: absolute;
  color: rgb(21, 238, 254);
  cursor: pointer;
  font-size: 20px;
  margin-bottom: 5px;
  right: 7%;
  top:30%;
}
.gotoShelf:hover{
  color: rgb(21, 103, 107);
  text-decoration: underline;
}
</style>