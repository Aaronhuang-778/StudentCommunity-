<template>
   <div>
      <div>
        <div class="search">
          <form>
              <input type="text" placeholder="输入搜索内容...">
              <button ></button>
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
            console.log(posts);
            this.articles = posts;
            console.log("---");
            console.log(this.articles.data);

        },
        methods: {
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
          },
          goforMan(other_id) {
            this.$router.push({name: 'userProfile', params: {user_id: this.user_id, other_id: other_id}});
          },
          search() {
            //fetch list
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
