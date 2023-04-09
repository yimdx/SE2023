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
      <el-table-column label="Agree"></el-table-column>
    </el-table>
   </el-card>
</template>

<script>
export default {

}
</script>

<style>

</style>