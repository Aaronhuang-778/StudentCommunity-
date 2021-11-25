<template>
   <div>
    <el-row :gutter="25">
      <el-col :span="20" :offset="2">
        <el-card v-for="(item,index) in articles" :key="index" style="background: transparent">
          <div slot="header">
            <div class="main-text" @click="goforDetail(item.post_id)">
              {{item.post_title}}
            </div>
<!--            <router-link class="main-text"-->
<!--                         :to="{ name: 'articleDetails', params: { article_id: item.post_id , user_id: this.user_id}}"-->
<!--                         >{{item.post_title}}</router-link>-->
            <div class="article-info">
              <el-tag effect="dark" size="mini">原创</el-tag>
              浏览量：0
              <span class="article_info_date">标签：
                <span v-if="item.labels.length === 0">未分类</span>
                <el-tag v-else class="tag_margin" v-for="(tag,index) in item.labels" :key="index">{{tag}}</el-tag>
              </span>
            </div>
          </div>
          <div class="tabloid">{{item.content}}</div>
          <i class="el-icon-user-solid article-icon">{{item.user_name}}</i>
          <i class="el-icon-date article-icon">
            {{formatted_time(item.post_date)}}
          </i>
<!--          <i class="el-icon-price-tag article-icon">-->
<!--            <router-link-->
<!--              class="tag"-->
<!--              v-for="(tag,index) in article.tags"-->
<!--              :key="index"-->
<!--              v-text="tag"-->
<!--              :to="'/tag/'+tag"-->
<!--            ></router-link>-->
<!--          </i>-->
        </el-card>
      </el-col>
    </el-row>
  </div>

</template>

<script>
    import api from '../tools/user';


    export default {
      name: 'articlelist',
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
            console.log("---");
            console.log(this.articles.labels);
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
            return date.toLocaleDateString() + '  ' + date.toLocaleTimeString()
          },
          goforDetail(article_id) {
              this.$router.push({
                name: 'articleDetails', params: { article_id: article_id , user_id: this.user_id, user_name: this.user_name}});
          }
        }
    }

</script>

<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>


    .item-box {
  position: relative;
  width: 100%;
  height: 100%;
}
.carimg {
  width: 100%;
  height: 100%;
  overflow: hidden;
  object-fit: cover;
}
.desc-box {
  position: absolute;
  bottom: 0;
  left: 50%;
  top: 50%;
  width: 500px;
  height: 40px;
  margin-left: -250px;
  margin-top: -20px;
  text-align: center;
}
.el-card {
  margin-top: 20px;
}
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
