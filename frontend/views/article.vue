<template>
  <div id="app">
    <!-- 用 v-for 渲染文章列表 -->
    <Article v-for="article in articleList" :key="article.title" :article="article"></Article>
  </div>
</template>

<script>
// 引入组件
import Article from '@/components/Article.vue';

export default {
  name: 'article',
  // 注册组件
  components: {
    Article
  },
  data: function() {
    return {
      articleList: [
        {
          cover: require('@/assets/logo.png'),
          title: '首发！近百位漫画家创作了一本战“疫”漫画，全书免费读',
          time: '2020-02-02 14:40:00',
          content:
            '这个春节与往年大不相同：大人们停止了走亲访友，孩子们被禁止外出玩耍，“口罩”取代“红包”成为正月里的关键词。也许你已经知道了，这些改变与新型冠状病毒有关，也许你还想知道，这讨厌的病毒为什么会突然出现、该怎么打败它，一级小朋友们可以帮什么忙？为了解答你的疑问，《中国少年报》、未来网联手近百位漫画家制作了这本电子漫画书，你应当知道的五件事。'
        },
        {
          cover: require('@/assets/logo.png'),
          title: '战友，你的“补给”到了！抗击疫情，青年突击队在行动',
          time: '2020-02-01 18:51:00',
          content:
            '今天是2月1日，疫情仍在延续。在大部分人还在家里“避险”的时候，医生、警察们早已坚守在自己的工作岗位，用自己的血肉之躯铸就抗击疫情的钢铁长城。钢轨上，火车呼啸，铁路人们也早早地来到单位，他们为运输物资的重要“生命线”保驾护航。新型冠状肺炎疫情打响后，车站封闭、乡镇互关，交通不便，留守值班干部职工的日常生活、防控药品极缺。'
        }
      ]
    };
  }
};
</script>

<style lang="scss">
#app {
  width: 100%;
  height: 100%;
}
</style>

