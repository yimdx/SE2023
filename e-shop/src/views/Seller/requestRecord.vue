<template>
<div class="all">
    <div class="left">
  <div class="tableName">Modify Commodity Information :</div>
   <el-table :data="MCIrecords" :border="true" style="width: 100%;margin-top:0;margin-left:0">
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
          <p m="t-0 b-2">Name: {{ props.row.name }}</p>
          <p m="t-0 b-2">Shop Name: {{ props.row.shopName }}</p>
          <p m="t-0 b-2">UnitPrice: {{ props.row.price }}</p>
          <p m="t-0 b-2">Quantity: {{ props.row.stock }}</p>
          <p m="t-0 b-2">Description: {{ props.row.discription }}</p>
          </div>
        </div>
      </template>
    </el-table-column>
    <el-table-column label="Name" prop="name" />
    <el-table-column label="Shop Name" prop="shopName" />
    <el-table-column label="UnitPrice" prop="price" />
    <el-table-column label="Quantity" prop="stock" />
      <el-table-column
        prop="submitStatus"
        label="Status"
        width="100"
        :filters="[
          { text: 'Submitted', value: 'Submitted' },
          { text: 'Passed', value: 'Passed' },
          { text: 'sendBack', value: 'sendBack' },
        ]"
        :filter-method="filterTag"
        filter-placement="bottom-end"
      >
        <template #default="scope">
          <el-tag :type="getTag(scope.$index,scope.row)" disable-transitions>{{
            scope.row.submitStatus
          }}</el-tag>
        </template>
      </el-table-column>
    <el-table-column label="Operations">
      <template #default="scope">
        <el-button
          size="small"
          type="danger"
          @click="handleUpdateDelete(scope.$index, scope.row)"
          >Delete</el-button
        >
      </template>
    </el-table-column>
   
  </el-table>
<div class="footer"></div>
</div>
<div class="right">
  <div class="tableName">Add Commodity Information :</div>
   <el-table :data="addRecords" :border="true" style="width: 100%;margin-top:0;margin-left:0">
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
          <p m="t-0 b-2">Name: {{ props.row.name }}</p>
          <p m="t-0 b-2">Shop Name: {{ props.row.shopName }}</p>
          <p m="t-0 b-2">UnitPrice: {{ props.row.price }}</p>
          <p m="t-0 b-2">Quantity: {{ props.row.stock }}</p>
          <p m="t-0 b-2">Description: {{ props.row.discription }}</p>
          </div>
        </div>
      </template>
    </el-table-column>
    <el-table-column label="Name" prop="name" />
    <el-table-column label="Shop Name" prop="shopName" />
    <el-table-column label="UnitPrice" prop="price" />
    <el-table-column label="Quantity" prop="stock" />
      <el-table-column
        prop="submitStatus"
        label="Status"
        width="100"
        :filters="[
          { text: 'Submitted', value: 'Submitted' },
          { text: 'Passed', value: 'Passed' },
          { text: 'sendBack', value: 'sendBack' },
        ]"
        :filter-method="filterTag"
        filter-placement="bottom-end"
      >
        <template #default="scope">
          <el-tag :type="getTag(scope.$index,scope.row)" disable-transitions>{{
            scope.row.submitStatus
          }}</el-tag>
        </template>
      </el-table-column>
    <el-table-column label="Operations">
      <template #default="scope">
        <el-button
          size="small"
          type="danger"
          @click="handleAddDelete(scope.$index, scope.row)"
          >Delete</el-button
        >
      </template>
    </el-table-column>
   
  </el-table>
  <div class="footer"></div>
</div>

</div>

</template>

<script setup>
import {ElNotification} from "element-plus";
import {getCurrentInstance} from "vue";
import  {useCounterStore} from "../../stores/counter"
const counter=useCounterStore();
const userType=counter.userType;
const userName=counter.userName;
let {proxy}=getCurrentInstance();
//get MCIrequest
let MCIrecords=[
    {
        userName:'LiHua',
        shopName:'testShop',
        name:'apple',
        discription:'tasty',
         picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"Submitted"

    },
    {
        userName:'LiHua',
        shopName:'testShop',
        name:'orange',
        discription:'tasty',
         picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"sendBack"

    },
    {
        userName:'LiHua',
        shopName:'testShop',
        name:'melon',
        discription:'tasty',
         picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:2,
        submitStatus:"Passed"

    },
    {
        userName:'LiHua',
        shopName:'testShop',
        name:'melon',
        discription:'tasty',
         picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:2,
        submitStatus:"Passed"

    },
    {
        userName:'LiHua',
        shopName:'testShop',
        name:'melon',
        discription:'tasty',
         picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:2,
        submitStatus:"Passed"

    },
    {
        userName:'LiHua',
        shopName:'testShop',
        name:'melon',
        discription:'tasty',
         picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:2,
        submitStatus:"Passed"

    }
];
//get add records
let addRecords=[  
    {
        userName:'LiHua',
        shopName:'testShop',
        name:'apple',
        discription:'tasty',
         picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"Submitted"

    },
    {
        userName:'LiHua',
        shopName:'testShop',
        name:'orange',
        discription:'tasty',
         picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:3,
        submitStatus:"sendBack"

    },
    {
        userName:'LiHua',
        shopName:'testShop',
        name:'melon',
        discription:'tasty',
         picture:"https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        price:1.05,
        stock:2,
        submitStatus:"Passed"

    }
    ];
    function getRecords(){
          proxy.$http
      .post("/merchant/goodsList/upShelfRequestList",{
        userName:userName
      })
      .then(function (res) {
        addRecords=res.data.result;
      })
      .catch(function (error) {
        console.log(error)
        ElNotification({
          title: "Error",
          message: "Get Add Records Failed(Something must go wrong!)",
          type: "error",});
      });
       proxy.$http
      .post("/merchant/goodsList/MCIRequestList",{
        userName:userName
      })
      .then(function (res) {
        MCIrecords=res.data.result;
      })
      .catch(function (error) {
        console.log(error)
        ElNotification({
          title: "Error",
          message: "Get MCI Records Failed(Something must go wrong!)",
          type: "error",});
      });
    }
    getRecords();
    function  getTag(index,row) {
      let status = row.submitStatus;
      if (status === "Passed") return "success";
      else if (status === "Submitted") return "warning";
      else return "danger";
    };
    function   filterTag(value, row) {
      return row.submitStatus === value;
    };
    function handleUpdateDelete(index,row){
        //delete row
             proxy.$http
      .post("/merchant/goodsList/MCIRequestList/delete", {
        userName:row.userName, 
        shopName:row.shopName,
        name:row.name
      })
      .then(function (res) {
         console.log("success delete");
          ElNotification({
          title: "Success",
          message: "Delete MCI request Passed",
          type: "success",});
      })
      .catch(function (error) {
        console.log(error)
        ElNotification({
          title: "Error",
          message: "Delete MCI Request  Failed(Something must go wrong!)",
          type: "error",});
      });
    }
    function handleAddDelete(index,row){
        //delete add
          proxy.$http
      .post("/merchant/goodsList/upShelfRequestList/delete", {
        userName:row.userName, 
        shopName:row.shopName,
        name:row.name
      })
      .then(function (res) {
          console.log("success delete");
          ElNotification({
          title: "Success",
          message: "Delete Add request Passed",
          type: "success",});
      })
      .catch(function (error) {
         console.log(error)
        ElNotification({
          title: "Error",
          message: "Delete Add Request  Failed(Something must go wrong!)",
          type: "error",});
      });
        
    }
</script>

<style scoped>

.all{
    margin:0px;
    padding:0px;
   height: calc(100%); 
overflow-y:scroll;
overflow-x:hidden;

}
.left{
    margin-left: 40px;
    margin-right: 20px;
    position: relative;
}
.right{
    position: relative;
    margin-left: 20px;
    margin-right: 40px;
}
.image{
 position: relative;
 height: 200px;
 width: 160px;
 left:12%;
 margin-top:15px;

}
.expand{
  height: 230px;
  width: 1000px;
  position: relative;
  left: 3%;
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
.footer{
    height: 300px;
    width: 60%;
    margin: 0;
    padding: 0;
    display: block;
}
.tableName{
    margin:10px;
    font-size: 30px;
}
</style>