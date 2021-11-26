<template>
  <el-aside width="150px">
  <el-dropdown>
    <div class="picture">
      <img src="../assets/user_head.jpg"/>
    </div>
    <br/>
    <div style="text-align: center; font-size: medium">
          {{user_name}}
    </div>

  <el-dropdown-menu slot="dropdown">

    <el-dropdown-item>
      <router-link
        :to="{name: 'userProfile', params: {user_id: this.user_id, other_id: this.user_id}}"
      style="color: #333333">
        <li class="el-icon-house">
            个人主页
        </li>
      </router-link>
    </el-dropdown-item>
    <el-dropdown-item >
      <router-link :to="{name: 'newLog'}" style="color: #333333">
        <li class="el-icon-back">
            退出登录
        </li>
      </router-link>
    </el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>
    <el-menu
      default-active="2"
      @open="handleOpen"
      @close="handleClose"
    style="background-color: transparent; border-right: 0;">
<!--      <el-menu-item index="1">-->
<!--        <i class="el-icon-menu"></i>-->
<!--        <span slot="title">-->
<!--          <router-link style="text-decoration: none"-->
<!--                       :to="{name: 'userProfile', params: {user_id: this.user_id, user_name: this.user_name}} ">主页</router-link>-->
<!--        </span>-->
<!--      </el-menu-item>-->
      <el-menu-item index="1">
        <i class="el-icon-news" style="color: aqua"></i>
        <span slot="title">
          <router-link style="text-decoration: none; color: black"
                       :to="{name: 'articlelist', params: {user_id: this.user_id, user_name: this.user_name}} ">广场</router-link>
        </span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-edit" style="color: aqua"></i>
        <span slot="title">
          <router-link style="text-decoration: none; color: black"
                       :to="{name: 'createArticle', params: {user_id: this.user_id, user_name: this.user_name}} ">发布</router-link>
        </span>
      </el-menu-item>
      <el-menu-item index="3">
        <i class="el-icon-document" style="color: aqua"></i>
        <span slot="title">
          <router-link style="text-decoration: none; color: black"
                       :to="{name: 'myarticles', params: {user_id: this.user_id, user_name: this.user_name}} ">我的</router-link>
        </span>
      </el-menu-item>
<!--      <el-menu-item index="4">-->
<!--        <i class="el-icon-search" style="color: aqua"></i>-->
<!--        <span slot="title">-->
<!--          <router-link style="text-decoration: none; color: black"-->
<!--                       :to="{name: 'search', params: {user_id: this.user_id, user_name: this.user_name}} ">查找</router-link>-->
<!--        </span>-->
<!--      </el-menu-item>-->
      <el-menu-item index="4">
        <i class="el-icon-view" style="color: aqua"></i>
        <span slot="title">
          <router-link style="text-decoration: none; color: black"
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
    // logout() {
    //   this.$router.push({name:"newLog"});
    // },
    // editInformation() {
    //   this.$router.push({name:"userProfile", params: {user_id: this.user_id, user_name: this.user_name}});
    // }
  }
}
</script>

<style scoped>
.picture {
  width: 100px;
  transform: rotate(45deg);
  overflow: hidden;
}
.picture > img {
  max-width: 100%;
  transform: rotate(-45deg) scale(1.42);
}

</style>
