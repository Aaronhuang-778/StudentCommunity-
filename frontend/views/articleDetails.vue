<template>
    <div>
    <div v-if="article !== null" class="grid-container">
        <div>
            <h1 id="title" style="position: center; font-size: xx-large">{{ article.post_title }}</h1>
            <p id="subtitle" style="color: #333333; font-size: medium">
                本文由 <i class="el-icon-user-solid article-icon" @click="goforMan(article.user_id)">
              {{article.user_name}}
          </i>发布于 {{ formatted_time(article.post_date) }}
            </p>
            <div class="article-body" style="word-wrap: break-word; word-break: normal">{{ article.content }}</div>
          <div>
            <Like :article="article" :user_id="user_id" ref="like" style="float: right; margin-top: 100px"></Like>
          </div>
        </div>
    </div>

  <Comment :article="article" :user_id="user_id" style="margin-top: 150px"></Comment>
      </div>

</template>

<script>
    import Comment from '../src/components/Comment'
    import api from "../tools/user";
    import Like from "../src/components/Like"

    export default {
        name: 'articleDetails',
        props:["article_id", "user_id","user_name"],
        components: {
          Comment,
          Like
        },
        data() {
            return {
                article: null,
                count: 0
            }
        },
        async mounted() {
            let res = await api.getPost(this.http());
            this.article = res.data.data;
            console.log(this.article);
            // this.$refs.comment.comments = this.article.comment;
            // console.log("++++++++++++++++");
        },
        methods: {
            formatted_time: function (iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
            },
          goforMan(other_id) {
            this.$router.push({name: 'userProfile', params: {user_id: this.user_id, other_id: other_id}});
          },
            http() {
                return {
                  user_id: this.user_id,
                  post_id: this.article_id
                }
            }
        }
    }
</script>

<style scoped>
    .grid-container {
      position: center;
    }


    #title {
        text-align: center;
        font-size: x-large;
    }

    #subtitle {
        text-align: center;
        color: gray;
        font-size: small;
    }
    .article-body {
        font-family: 华文新魏;
      font-size: x-large;
      width: 700px;
      margin-left: 150px;
      margin-top: 50px;
    }

    .toc ul {
        list-style-type: none;
    }

    .toc a {
        color: gray;
    }
</style>
