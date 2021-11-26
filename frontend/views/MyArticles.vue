<template>
<div>
    <el-row :gutter="25" style="background-image: image('../src/assets/seesky.jpg')">
      <el-col :span="20" :offset="2"  >
        <el-card v-for="(item,index) in articles" :key="index" style="background: transparent">
          <div slot="header">
            <div class="main-text" @click="goforDetail(item.post_id)">
              {{item.post_title}}
            </div>

            <div class="article-info">
              <el-tag effect="dark" size="mini">原创</el-tag>
              浏览量：0
              <span class="article_info_date">标签：
                <el-tag  class="tag_margin"  >{{item.keyword_name}}</el-tag>
<!--                <span v-if="item.labels.length === 0">未分类</span>-->
<!--                <el-tag v-else class="tag_margin" v-for="(tag,index) in item.labels" :key="index">{{tag}}</el-tag>-->
              </span>
              <el-button @click="deleteArticles(item.post_id)" style="float: right; size: 10px" type="danger">删除</el-button>
            </div>
          </div>
          <div class="tabloid">{{brief(item.content)}}</div>
          <i class="el-icon-date article-icon">
            {{formatted_time(item.post_date)}}
          </i>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
 import api from '../tools/user';

export default {
  name: "MyArticles",
  props:["user_id", "user_name"],
  data() {
        return {
            articles:[]
        }
  },
  mounted() {
    //my articles!!!
    this.fetchlist();
  },
  methods: {
          async deleteArticles(article_id) {
            let res = await api.delPost({"post_id":article_id});
            this.fetchlist();
          },
         async fetchlist() {
            let res = await api.getMyPostList({"user_id": this.user_id});
            let posts = res.data.data.post;
            console.log(posts);
            this.articles = posts;
            console.log("---");
            console.log(this.articles.data);
         } ,
          formatted_time(iso_date_string) {
            console.log(iso_date_string);
            const date = new Date(iso_date_string);
            return date.toLocaleDateString() + '  ' + date.toLocaleTimeString()
          },
          goforDetail(article_id) {
              this.$router.push({
                name: 'articleDetails', params: { article_id: article_id , user_id: this.user_id, user_name: this.user_name}});
          },
          brief(content) {
            return content.substr(0, 35) + '...';
          }

      }
}
</script>

<style scoped>
.article-info {
  margin-top: 10px;
  color: black;
  font-size: 13px;
}
.article-icon,
.article-icon .tag {
  color: black;
  font-size: 13px;
  margin-right: 10px;
  text-decoration: none;
}
.article-icon .tag:hover {
  color: black;
  cursor: pointer;
}
.tabloid {
  color: black;
  font-size: 14px;
  margin-bottom: 10px;
}
</style>
