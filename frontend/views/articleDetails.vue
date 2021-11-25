<template>
    <div>
    <div v-if="article !== null" class="grid-container">
        <div>
            <h1 id="title">{{ article.post_title }}</h1>
            <p id="subtitle">
                本文由 {{ article.user_name }} 发布于 {{ formatted_time(article.post_date) }}
            </p>
            <div class="article-body">{{ article.content }}</div>
        </div>
    </div>
  <Comment :article="article"></Comment>
      </div>

</template>

<script>
    import axios from 'axios';
    import Comment from '../src/components/Comment'
    import api from "../tools/user";

    export default {
        name: 'articleDetails',
        props:["article_id", "user_id","user_name"],
        components: {
          Comment
        },
        data() {
            return {
                article: null
            }
        },
        async mounted() {
            let res = await api.getPost(this.http());
            this.article = res.data.data;
        },
        methods: {
            formatted_time: function (iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
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
        display: grid;
        grid-template-columns: 3fr 1fr;
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
    .article-body p img {
        max-width: 100%;
        border-radius: 50px;
        box-shadow: gray 0 0 20px;
    }

    .toc ul {
        list-style-type: none;
    }

    .toc a {
        color: gray;
    }
</style>
