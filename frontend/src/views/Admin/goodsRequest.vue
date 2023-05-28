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
        <span @click="handleMCIApprove(scope.$index, scope.row)" class="approve">Approve</span>
        &nbsp;
        &nbsp;
         <span @click="handleMCIDisapprove(scope.$index, scope.row)" class="disapprove">Disapprove</span>
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
        <span @click="handleAddApprove(scope.$index, scope.row)" class="approve">Approve</span>
        &nbsp;
        &nbsp;
         <span @click="handleAddDisapprove(scope.$index, scope.row)" class="disapprove">Disapprove</span>
      </template>
    </el-table-column>
   
  </el-table>
  <div class="footer"></div>
</div>

</div>

</template>

<script setup>

import {ElNotification} from "element-plus";
import {getCurrentInstance,reactive,ref} from "vue";

let {proxy}=getCurrentInstance();
//get MCIrequest
let MCIrecords=ref([
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
]);
//get add records
let addRecords=ref([  
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
    ]);

    function getRecords(){
     proxy.$http
      .post("/admin/checkUpShelfRequest")
      .then(function (res) {
        addRecords.value=res.data.result;
        //console.log(addRecords.value);
      })
      .catch(function (error) {
        console.log(error)
        ElNotification({
          title: "Error",
          message: "Get Add Records Failed(Something must go wrong!)",
          type: "error",});
      });
       proxy.$http
      .post("/admin/checkMCIRequest")
      .then(function (res) {
        MCIrecords.value=res.data.result;
       // console.log(MCIrecords.value)
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
    function handleAddApprove(index,row){
        proxy.$http
      .post("/admin/checkUpShelfRequest/Passed",{
        userName:row.userName,
        shopName:row.shopName,
        name:row.name
      })
      .then(function (res) {
        getRecords();
        //row.submitStatus='Passed';

      })
      .catch(function (error) {
        console.log(error)
        ElNotification({
          title: "Error",
          message: "Approve Add Record Failed(Something must go wrong!)",
          type: "error",});
      });
    }
    function handleAddDisapprove(index,row){
            proxy.$http
      .post("/admin/checkUpShelfRequest/sendBack",{
        userName:row.userName,
        shopName:row.shopName,
        name:row.name
      })
      .then(function (res) {
        //row.submitStatus='sendBack';
        getRecords();
      })
      .catch(function (error) {
        console.log(error)
        ElNotification({
          title: "Error",
          message: "Disapprove Add Record Failed(Something must go wrong!)",
          type: "error",});
      });
    }
      function handleMCIApprove(index,row){
        proxy.$http
      .post("/admin/checkMCIRequest/Passed",{
        userName:row.userName,
        shopName:row.shopName,
        name:row.name
      })
      .then(function (res) {
        //row.submitStatus='Passed';
        getRecords();
      })
      .catch(function (error) {
        console.log(error)
        ElNotification({
          title: "Error",
          message: "Approve MCI Record Failed(Something must go wrong!)",
          type: "error",});
      });
    }
    function handleMCIDisapprove(index,row){
            proxy.$http
      .post("/admin/checkMCIRequest/sendBack",{
        userName:row.userName,
        shopName:row.shopName,
        name:row.name
      })
      .then(function (res) {
        //row.submitStatus='sendBack';
        getRecords();
      })
      .catch(function (error) {
        console.log(error)
        ElNotification({
          title: "Error",
          message: "Disapprove Add MCI Failed(Something must go wrong!)",
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
  background: linear-gradient(to right,rgb(241, 223, 223),rgb(187, 187, 206));
  margin-right: 10px;
  padding-right: 10px;
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
.approve{
    color:rgb(29, 84, 29);
    font-size: 10px;
}
.approve:hover{
    cursor: pointer;
    font-size: 11px;
    color: green;
}
.disapprove{
    color:rgb(255, 68, 68);
    font-size: 10px;
}
.disapprove:hover{
    color:rgb(114, 77, 77);
    font-size: 11px;
    cursor: pointer;
}
</style>