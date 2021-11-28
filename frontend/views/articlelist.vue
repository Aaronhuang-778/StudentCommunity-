<template>
   <div>
      <div class="search">
        <div class="a">
          <form>
            <input type="text" class="b" placeholder="输入搜索内容..." v-model="searchstr">
            <a href="#" class="c">
              <img src="../src/assets/function/search.png" style="width:20px;" @click="search">
            </a>
          </form>
        </div>
      </div>
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
            </div>
          </div>
          <div class="tabloid">{{brief(item.content)}}</div>
          <i class="el-icon-user-solid article-icon" @click="goforMan(item.user_id)">
              {{item.user_name}}
          </i>
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
    import Search from "../src/components/search";

    export default {
      name: 'articlelist',
      components: {Search},
      props:["user_id", "user_name"],
      data() {
            return {
              articles:[],
              searchstr:""
            }
      },
    mounted() {
      this.fetchlist();

    },
        methods: {
          async fetchlist() {
            let res = await api.getPostList();
            let posts = res.data.data.post;
            console.log(posts);
            this.articles = posts;
          },

          formatted_time(iso_date_string) {
            // console.log(iso_date_string);
            const date = new Date(iso_date_string);
            return date.toLocaleDateString() + '  ' + date.toLocaleTimeString()
          },
          goforDetail(article_id) {
              this.$router.push({
                name: 'articleDetails', params: { article_id: article_id , user_id: this.user_id, user_name: this.user_name}});
          },
          brief(content) {
            return content.substr(0, 35) + '...';
          },
          goforMan(other_id) {
            this.$router.push({name: 'userProfile', params: {user_id: this.user_id, other_id: other_id}});
          },
          async search() {
            //fetch list
            let res = await api.search({"search": this.searchstr})
            console.log(res.data.data.post);
            this.articles = res.data.data.post;
            // this.fetchlist();
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
.search {
  margin-top: 10px;
}

    .a{
      position: absolute;
      top: 8%;
      left: 75%;
      margin-left: 100px;
      transform: translate(-50%,-50%);
      background-color: #2f3640;
      height: 40px;
      border-radius: 60px;
      padding: 10px;
    }
    .a:hover .b{
      width: 100px;
      padding: 0 10px;
    }
    .a:hover .c{
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
      font-size: 15px;
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
