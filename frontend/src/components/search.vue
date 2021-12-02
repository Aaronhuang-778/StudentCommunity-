<template>

<div>
  <div class="search">
                <form>
                    <input :="post_title__icontains" type="text" class="b" placeholder="输入搜索内容...">
                  <a href="#" class="c">
                    <img src="src/assets/function/search.png" style="width:20px;" @click="search">
                  </a>
                </form>
            </div>

</div>
</template>

<script>
import api from '../../tools/user'

export default {
  name: "search",

  data() {
    return {
        post_title__icontains: ''
    }
  },

  methods: {
    // async search() {
    //   let res = await api.search({"post_title__icontains": this.post_title__icontains});
    //   if (res.data.code === 20000) {
    //
    //   } else {
    //     alert("search error!")
    //   }
    // }
  }
}
</script>

<style scoped>
.search{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background-color: #2f3640;
  height: 100px;
  border-radius: 60px;
  padding: 30px;
}
.search:hover .b{
  width: 400px;
  padding: 0 10px;
}
.search:hover .c{
  background-color: #E4E9F7;
}
.b{
  border: none;
  background: none;
  /* 取消选中搜索框时的外边框 */
  outline: none;
  width: 0;
  padding-top: 30px;
  transition: .4s;
  line-height: 40px;
  font-size: 25px;
  color:  #E4E9F7;
}
.c{
  color: #E4E9F7;
  float: right;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #2f3640;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: .4s;
}
</style>


