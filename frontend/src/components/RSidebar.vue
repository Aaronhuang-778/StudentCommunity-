<template>

  <el-aside width="200px">
    <div class="search">
                <form>
                    <input type="text" placeholder="输入搜索内容...">
                    <button @click="search"></button>
                </form>
            </div>
      <div> {{ user_name }},你好</div>
      <div>
            <span
                  v-for="tag in tags"
                  v-bind:key="tag"
                  class="tag"
            >
                {{ tag }}
            </span>
        </div>
  </el-aside>

</template>

<script>
export default {
  name: "RSidebar",
  props:["user_id", "user_name"],
  data() {
    return {
        tags: ["compile", "database"]
    }
  },
  methods: {
    search() {
      this.$router.push({name: 'articlelist', params: {user_id: this.user_id, user_name: this.user_name}});
    }
  }
}
</script>

<style scoped>
 .search {
        padding-top: 22px;
    }

    * {
        box-sizing: border-box;
    }

    form {
        position: relative;
        width: 200px;
        margin: 0 auto;
    }

    input, button {
        border: none;
        outline: none;
    }

    input {
        width: 100%;
        height: 35px;
        padding-left: 13px;
        padding-right: 46px;
    }

    button {
        height: 35px;
        width: 35px;
        cursor: pointer;
        position: absolute;
    }

    .search input {
        border: 2px solid gray;
        border-radius: 5px;
        background: transparent;
        top: 0;
        right: 0;
    }

    .search button {
        background: gray;
        border-radius: 0 5px 5px 0;
        width: 45px;
        top: 0;
        right: 0;
    }

    .search button:before {
        content: "搜索";
        font-size: 13px;
        color: white;
    }
</style>
