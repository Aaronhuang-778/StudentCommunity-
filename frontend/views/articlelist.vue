<template>
  <div id="content">
    <div class="article_wrap" v-for="(item,index) in articles" :key="index">
      <div class="article_title" @click="goforDetail(item.post_id)"> {{item.post_title}}</div>
      <div class="article_info">
        <span class="article_info_username">{{item.user_name}}</span>
        <span class="article_info_date">发表时间：{{item.post_date}}</span>
        <span class="article_info_date">标签：
          <span v-if="item.labels.length === 0">未分类</span>
          <el-tag v-else class="tag_margin" v-for="(tag,index) in item.labels" :key="index">{{tag}}</el-tag>
        </span>
      </div>
      <div class="article_gist">文章摘要：{{item.content}}</div>
    </div>
  </div>

<!--  <div>-->
<!--    <div v-for="article in info.results" v-bind:key="article.url" id="articles">-->
<!--        <div>-->
<!--            <span-->
<!--                  v-for="tag in article.tags"-->
<!--                  v-bind:key="tag"-->
<!--                  class="tag"-->
<!--            >-->
<!--                {{ tag }}-->
<!--            </span>-->
<!--        </div>-->
<!--         <router-link-->
<!--                :to="{ name: 'articleDetails', params: { article_id: article.id , user_id: this.user_id}}"-->
<!--                class="article-title"-->
<!--        >-->
<!--            {{ article.title }}-->
<!--        </router-link>-->

<!--        <div>{{ formatted_time(article.created) }}</div>-->
<!--    </div>-->
<!--    </div>-->

</template>

<script>
    import api from '../tools/user';
    import axios from 'axios';
    import Article from "./article";

    export default {
      name: 'articlelist',
      components: {Article},
      props:["user_id", "user_name"],
      data() {
            return {
                articles:[]
            }
      },
      async  mounted() {
            let res = await api.getPostList();
            let posts = res.data.data.post;
            // console.log(posts);
            this.articles = posts;
            // console.log("---");
            // console.log(this.articles[0].post_id);
            // axios
            //     .get('/api/article')
            //     .then(response => (this.info = response.data))

          // this.$https({
          //   method: "post",
          //   url: '-----',
          //   data:{}
          // }).then(function (res){
          //   this.articles = res.body.payload.article;
          //   for(let i = 0;i < this.articles.length; i++) {
          //     if (this.articles[i].labels.length > 0) {
          //       this.articles[i].labels = this.articles[i].labels.split(',');
          //       console.log(this.articles[i].labels.length);
          //     }
          //   }
          // }).catch(function (e){
          //   this.$message.error("error!");
          // })
        },
        methods: {
            formatted_time: function (iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
            },
          goforDetail(article_id) {
              this.$router.push({ name: 'articleDetails', params: { article_id: article_id , user_id: this.user_id}});
          }
        }
    }

</script>

<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>
    #articles {
        padding: 10px;
    }

    .article-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }

    .tag {
        padding: 2px 5px 2px 5px;
        margin: 5px 5px 5px 0;
        font-family: Georgia, Arial, sans-serif;
        font-size: small;
        background-color: #4e4e4e;
        color: whitesmoke;
        border-radius: 5px;
    }

    .article_wrap {
      padding: 20px;
    }
    .article_title {
      display: inline-block;
      color: white;
      font-size: 22px;
      font-weight: 600;
      cursor: pointer;
    }

    .article_title:hover {
      border-bottom: 1px solid #222;
      color: black;
      background: white;
    }

    .article_info {
      color: white;
      font-size: 14px;
      padding-top: 8px;
      margin-top: 10px;
    }

    .article_info_username {
      margin-right: 10px;
    }

    .article_info_date {
      margin-right: 10px;
    }

    .tag_margin {
      margin: 3px;
    }

    .article_gist {
      text-align: center;
      margin-top: 10px;
      padding-top: 40px;
      padding-bottom: 40px;
      font-size: 16px;
      color: white;
    }

    .article_button {
      display: inline-block;
      padding: 3px 12px;
      border: 2px solid black;
      color: white;
      font-size: 14px;
      cursor: pointer;
      margin-top: 20px;
    }

    .article_all:hover {
      color: white;
      background: #000;
      font-weight: 600;
    }

</style>
