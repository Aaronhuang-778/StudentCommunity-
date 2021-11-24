<template>
  <el-container  class="total">

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

.total {
  background: url("../src/assets/sky.jpg");
  filter: alpha(opacity=50);
  height: 700px;
  border: 1px solid #eee
}



</style>
