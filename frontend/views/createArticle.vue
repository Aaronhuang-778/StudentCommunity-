<template>
  <div id="article-create">
    <h3>发表文章</h3>
    <form>
      <div class="form-elem">
        <span>标题：</span>
        <input v-model="post_title" type="text" placeholder="输入标题"
               style="background-color: transparent; border-width: 0; outline:none">
      </div>

      <div class="form-elem">
        <span>分类：</span>
        <span
              v-for="category in categories"
              :key="category.id"
              >
          <!--样式也可以通过 :style 绑定-->
          <button
                  class="category-btn"
                  :style="categoryStyle(category)"
                  @click.prevent="chooseCategory(category)"
                  >
            {{category.keyword_name}}
          </button>
        </span>
      </div>


      <div class="form-elem">
        <span>内容：</span>
        <textarea v-model="content"  style="background: transparent; font-size: 23px; height: 300px; width: 600px"></textarea>
      </div>

      <div class="form-elem">
        <img height="35" width="35" src="../src/assets/function/publish.png" v-on:click.prevent="submit" style="float: right; margin-right: 200px">
      </div>
    </form>
  </div>
</template>

<script>
  import api from '../tools/user';
  import axios from 'axios';
  // import authorization from '@/utils/authorization';

  export default {
    name: 'createArticle',
    props:["user_id", "user_name"],
    data: function () {
      return {
        // 文章标题
        post_title: '',
        // 文章正文
        content: '',
        // 数据库中所有的分类
        categories: [],
        // 选定的分类
        selectedCategory: null
      }
    },
    async mounted() {
      // 页面初始化时获取所有分类
      // axios
      //   .get('/api/category/')
      //   .then(response => this.categories = response.data)
      let res = await api.getKeywordList();
      // console.log(res.data.data);
      this.categories = res.data.data;
    },
    methods: {
      // 根据分类是否被选中，按钮的颜色发生变化
      // 这里可以看出 css 也是可以被 vue 绑定的，很方便
      categoryStyle(category) {
        if (this.selectedCategory !== null && category.id === this.selectedCategory.id) {
          return {
            backgroundColor: '#46c8ff',
            border: 'black',
          }
        }
        return {
          backgroundColor: 'white',
          color: 'black',
        }
      },
      // 选取分类的方法
      chooseCategory(category) {
        // 如果点击已选取的分类，则将 selectedCategory 置空
        if (this.selectedCategory !== null && this.selectedCategory.id === category.id) {
          this.selectedCategory = null
        }
        // 如果没选中当前分类，则选中它
        else {
          this.selectedCategory = category;
        }
      },
      http() {
        return {
          post_title: this.post_title,
          content: this.content,
          keyword: this.selectedCategory,
          user_id: this.user_id
        }
      },
      // 点击提交按钮
      async submit() {
        let res = await api.publishPost(this.http());
        if (res.data.code === 20000) {
          // alert("发布成功");
          this.$router.push({name: 'articlelist', params: {user_id: this.user_id, user_name: this.user_name}});
        }
        else {
          alert("发布失败");
        }
      },
    }
  }
</script>

<style scoped>
  .category-btn {
    margin-right: 10px;
  }
  #article-create {
    text-align: center;
    font-size: large;
  }
  form {
    text-align: left;
    padding-left: 100px;
    padding-right: 10px;
  }
  .form-elem {
    padding: 10px;
  }
  .form-elem img:hover{
    transform: scale(2.0,2.0);

    -ms-transform:scale(2.0,2.0);

    -moz-transform:scale(2.0,2.0);

    -webkit-transform:scale(2.0,2.0);

    -o-transform:scale(2.0,2.0);

  }
  input {
    height: 25px;
    padding-left: 10px;
    width: 50%;
  }
  button {
    height: 35px;
    cursor: pointer;
    outline: none;
    background: steelblue;
    color: whitesmoke;
    border-radius: 5px;
    width: 60px;
  }
</style>
