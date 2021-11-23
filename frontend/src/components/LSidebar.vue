<template>
  <el-aside width="200px">
  <el-dropdown>
  <span class="el-dropdown-link">
    <el-avatar :size="100" style="position: center"></el-avatar>
  </span>
  <el-dropdown-menu slot="dropdown">
    <el-dropdown-item >
      <button @click="logout" style="border: none">logout</button>
    </el-dropdown-item>
    <el-dropdown-item>
      <button @click="editInformation" style="border: none">edit u information</button>
    </el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>
    <el-menu
      default-active="2"
      @open="handleOpen"
      @close="handleClose">
<!--      <el-menu-item index="1">-->
<!--        <i class="el-icon-menu"></i>-->
<!--        <span slot="title">-->
<!--          <router-link style="text-decoration: none"-->
<!--                       :to="{name: 'userProfile', params: {user_id: this.user_id, user_name: this.user_name}} ">主页</router-link>-->
<!--        </span>-->
<!--      </el-menu-item>-->
      <el-menu-item index="1">
        <i class="el-icon-menu"></i>
        <span slot="title">
          <router-link style="text-decoration: none"
                       :to="{name: 'articlelist', params: {user_id: this.user_id, user_name: this.user_name}} ">帖子</router-link>
        </span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-document"></i>
        <span slot="title">
          <router-link style="text-decoration: none"
                       :to="{name: 'createArticle', params: {user_id: this.user_id, user_name: this.user_name}} ">发布</router-link>
        </span>
      </el-menu-item>
      <el-menu-item index="3">
        <i class="el-icon-setting"></i>
        <span slot="title">
          <router-link style="text-decoration: none"
                       :to="{name: 'message', params: {user_id: this.user_id, user_name: this.user_name}} ">留言</router-link>
        </span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title">
          <router-link style="text-decoration: none"
                       :to="{name: 'about', params: {user_id: this.user_id, user_name: this.user_name}} ">关于</router-link>
        </span>
      </el-menu-item>
    </el-menu>
  </el-aside>

</template>

<script>
export default {
  name: "LSidebar",
  props:["user_id", "user_name"],
  methods: {
    logout() {
      this.$router.push({name:"newLog"});
    },
    editInformation() {
      this.$router.push({name:"userProfile", params: {user_id: this.user_id, user_name: this.user_name}});
    }
  }
}
</script>

<style scoped>



</style>
