<template>
  <el-card>
    <el-table :data="storelist" border stripe>
      <el-table-column type="index"></el-table-column>
      <el-table-column label="ShopName" prop="shopName"></el-table-column>
      <el-table-column label="Address" prop="address"></el-table-column>
      <el-table-column label="ShopInfo" prop="shopInfo"></el-table-column>
      <el-table-column label="StartTime" prop="startTime"></el-table-column>
      <el-table-column label="Goods" prop="goods"></el-table-column>
      <el-table-column
        prop="status"
        label="Status"
        width="100"
        :filters="[
          { text: 'submitted', value: 'submitted' },
          { text: 'passed', value: 'passed' },
          { text: 'sendBack', value: 'sendBack' },
        ]"
        :filter-method="filterTag"
        filter-placement="bottom-end"
      >
        <template #default="scope">
          <el-tag :type="getTag(scope.$index,scope.row)" disable-transitions>{{
            scope.row.status
          }}</el-tag>
        </template>
      </el-table-column>
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
    <el-descriptions-item label="Status" label-align="right" align="center">
      <el-tag :type="getTag(0,showInfo)" size="small">{{showInfo.status}}</el-tag>
    </el-descriptions-item>
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
          status: "submitted",
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
        status: "",
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
        },
        {
          shopName: "testshop",
          address: "address",
          shopInfo: "shopinfo",
          startTime: "starttime",
          goods: "no goods",
          status: "passed",
        },
        {
          shopName: "testshop",
          address: "address",
          shopInfo: "shopinfo",
          startTime: "starttime",
          goods: "no goods44444444444444444444444444444444444444444444",
          status: "sendBack",
        },
      ];
      const { data: res } = await this.$http.post("/admin/index/stores", {
        params: this.queryInfo,
      });

      if (res.meta.status !== 200)
        return this.$message.error("getting store list failed");
      this.storelist = res.data;
      console.log(res);
    },
    handleShowMore(index, row) {
      if(this.showMoreVisible===false) {
        this.showMoreVisible=true;
        this.showInfo.shopName=row.shopName;
        this.showInfo.shopInfo=row.shopInfo;
        this.showInfo.address=row.address;
        this.showInfo.startTime=row.startTime;
        this.showInfo.goods=row.goods;
        this.showInfo.status=row.status;
        console.log(this.showInfo)
    }
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
    getTag(index,row) {
      let status = row.status;
      if (status === "passed") return "success";
      else if (status === "submitted") return "warning";
      else return "danger";
    },
    filterTag(value, row) {
      return row.status === value;
    },
    gotoShelf(){
         if(this.showInfo.status!=="passed"){
            return ;
        }
      const counter=useCounterStore();
     if(counter.userType==="admin") this.$router.push("/admin/index/shelf?shopName="+this.showInfo.shopName);
      else if (counter.userType==="seller") this.$router.push("/seller/index/shelf?shopName="+this.showInfo.shopName);
      else if(counter.userType==='buyer')  this.$router.push("/buyer/index/shelf?shopName="+this.showInfo.shopName);
      else  this.$router.push("/");
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