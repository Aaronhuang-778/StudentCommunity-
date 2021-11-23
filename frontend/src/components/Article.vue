<template>
  <div class="article">
    <div>token</div>
    <div class="article-cover">
      <img :src="article.cover" alt="">
    </div>
    <div class="info">
      <div class="article-title">{{ article && article.title }}</div>
      <div class="article-time">{{ formatTime }}</div>
      <div class="article-content">{{ brief }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Article',
  // 接收父组件传来的 article 对象
  props: {
    article: Object
  },
  // 计算属性
  computed: {
    // 对时间进行格式化
    formatTime: function() {
      if (this.article) {
        const dt = new Date(this.article.time)
        const month = dt.getMonth()
        const date = dt.getDate()
        return `${month}月${date}日`
      }
      return '';
    },
    // 截取文章内容的前 35 个字，并加上省略号
    brief: function() {
      return this.article.content.substr(0, 35) + '...';
    }
  }
}
</script>

<style lang="scss" scoped>
.article {
  width: 400px;
  display: flex;
  padding: 10px 0;
  border-bottom: 1px solid #dbdbdb;
  &:last-child {
    border: none;
  }
  .article-title {
    font-size: 16px;
    font-weight: 500;
    color: #42b983;
    text-align: justify;
  }
  .article-cover {
    flex: none;
    width: 120px;
    margin-right: 10px;
    > img {
      width: 100%;
    }
  }
  .article-content, .article-time {
    font-size: 14px;
  }
  .article-time {
    margin: 10px 0;
    color: #c5c5c5;
  }
}
</style>
