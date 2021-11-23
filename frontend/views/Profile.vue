<template>
  <el-container  style="height: 700px; border: 1px solid #eee">>

    <lside :user_id="user_id" :user_name="user_name"> </lside>


  <el-container>
    <el-header>
      <blogheader></blogheader>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>

  </el-container>

    <rside :user_id="user_id" :user_name="user_name"></rside>
</el-container>
</template>

<script>
import lside from '../src/components/LSidebar'
import rside from '../src/components/RSidebar'
import blogheader from '../src/components/BlogHeader'
export default {
  name: "Profile",
  props:["user_id", "user_name"],
  components: {
      lside,
    rside,
    blogheader
  },
  data() {
    return {

    }
  },
  methods: {

  }
}
</script>

<style scoped>
.el-header, .el-footer {
    background-color: #0e69e0;
    color: #333;
    text-align: center;
  }

  .el-main {
    background-color: #c6e8ec;
    color: #333;
    text-align: center;
  }

   .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }



</style>
