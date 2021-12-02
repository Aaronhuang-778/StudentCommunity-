<template>
  <div>
    <el-divider></el-divider>
  <!-- 评论多行文本输入控件 -->
    <li> 发布评论：</li>
  <textarea
            v-model="message"
            :placeholder="placeholder"
            name="comment"
            id="comment-area"
            cols="130"
            rows="3"
            style="box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
                  background-color: transparent;
                    margin-left: 65px; margin-top: 20px"
            ></textarea>
    <img class="commentBtn" src="../assets/function/comment.png" @click="submit" height="30px" width="30px"
         style="margin-left: 10px; margin-bottom: 10px">
  <div>
  </div>

  <el-divider></el-divider>
    已有 {{ article.comment_number }} 条评论
    <div class="infinite-list-wrapper" style="overflow:auto">
    <ul
      style="list-style: none"
      v-infinite-scroll="load"
      infinite-scroll-disabled="disabled">
      <!-- 渲染所有评论内容 -->
      <li v-for="comment in comments"
       :key="comment.comment_id">
          <div class="comments">
            <div>
              <span class="username">
                {{ comment.user_name }}
              </span>
              于
              <span class="created">
                {{formatted_time(comment.comment_date)}}
              </span>
      <!--        <span v-if="comment.parent">-->
      <!--          对-->
      <!--          <span class="parent">-->
      <!--            {{ comment.parent.author.username }}-->
      <!--          </span>-->
      <!--        </span>-->
              说道：
            </div>
            <div class="content">
              {{ comment.content }}
            </div>
      <!--      <div>-->
      <!--        <button class="commentBtn" @click="replyTo(comment)">回复</button>-->
      <!--      </div>-->
          </div>
      </li>
    </ul>
    <p v-if="loading" style="font-size: small; font-family: 黑体">加载中...</p>
    <p v-if="noMore" style="font-size: small; font-family: 黑体">没有更多了</p>
  </div>

  </div>
</template>

<script>
  import api from '../../tools/user';
  import axios from 'axios';
  import user from "../../tools/user";

  export default {
    name: 'Comment',
    // 通过 props 获取当前文章
    props: {article: Object, user_id: Number},
    data: function () {
      return {
        // 所有评论
        comments: [],
        // 评论控件绑定的文本和占位符
        message: '',
        placeholder: '发表您的评论',
        // 评论的评论
        // parentID: null
        count: 10,
        loading: false
      }
    },
    computed: {
      noMore () {
        return this.count >= 20
      },
      disabled () {
        return this.loading || this.noMore
      }
    },
    // 监听 article 对象
    // 以便实时更新评论
    watch: {
      article() {
        this.comments = this.article !== null ? this.article.comment : [];
      }
    },
    methods: {
      // 提交评论
      http() {
        return {
          post_id:this.article.post_id,
          user_id:this.user_id,
          content:this.message
        }
      },
      async submit() {
        let res = await api.comment(this.http());
        if (res.data.code===20000) {
          this.comments = res.data.data.comment;
          this.article.comment_number = this.comments.length;
          // alert("评论成功");
        } else {
          alert("评论失败");
        }
      },
      load () {
        this.loading = true
        setTimeout(() => {
          this.count += 2
          this.loading = false
        }, 2000)
      },
      formatted_time(iso_date_string) {
            // console.log(iso_date_string);
            const date = new Date(iso_date_string);
            return date.toLocaleDateString() + '  ' + date.toLocaleTimeString()
      },
    }
  }
</script>

<style scoped>
  button {
    cursor: pointer;
    border: none;
    outline: none;
    color: black;
    border-radius: 5px;
  }
  .submitBtn {
    height: 35px;
    background:#e5e9f2;
    width: 60px;
    size: inherit;
  }
  .commentBtn:hover{
    transform: scale(1.5,1.5);

    -ms-transform:scale(1.5,1.5);

    -moz-transform:scale(1.5,1.5);

    -webkit-transform:scale(1.5,1.5);

    -o-transform:scale(1.5,1.5);

  }
  .comments {
    padding-top: 10px;
  }
  .username {
    font-weight: bold;
    color: darkorange;
  }
  .created {
    font-weight: bold;
    color: darkblue;
  }
  .parent {
    font-weight: bold;
    color: orangered;
  }
  .content {
    font-size: large;
    padding: 15px;
  }
</style>
