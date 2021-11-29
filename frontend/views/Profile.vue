<template>
  <el-container  class="total">
    <lside :user_id="user_id" :user_name="user_name" :picture="picture"> </lside>
  <el-container style="border-right: 0">
    <el-header style="border-right: 0">
      <blogheader></blogheader>
    </el-header>
    <el-main style="margin-top: 25px">
      <router-view></router-view>
    </el-main>
  </el-container>
</el-container>
</template>

<script>
import lside from '../src/components/LSidebar'
import rside from '../src/components/RSidebar'
import blogheader from '../src/components/BlogHeader'
export default {
  name: "Profile",
  props:["user_id", "user_name", "picture"],
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
  height: 700px;
}



</style>
