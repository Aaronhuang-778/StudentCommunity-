<template>
      <div >
        <span class="img-box" @click="handleClickUp">
          <img v-if="isUp" src="../assets/like.png" alt=""/>
          <img v-else src="../assets/tolike.png" alt="" />
          {{like_num}}
        </span>
        <span class="img-box" @click="handleClickDown">
          <img v-if="isDown" src="../assets/dislike.png" alt=""/>
          <img v-else src="../assets/todislike.png" alt="" />
          {{unlike_num}}
        </span>
      </div>
</template>

<script>
export default {
  name: "Like",
  props: ["article_id"],
  components: {
  },
  data () {
    return {
      isUp: false,
      isDown: false,
      like_num:0,
      unlike_num: 0
    };
  },
  created () {

  },
  mounted () {

  },
  computed: {},
  watch: {},
  methods: {
    handleClickUp () {
      if (this.isUp) {
        this.like_num--;
      } else {
        this.like_num++;
      }
      this.isUp = !this.isUp;
      //call back
    },
    handleClickDown() {
      if (this.isDown) {
        this.unlike_num--;
      } else {
        this.unlike_num++;
      }
      this.isDown = !this.isDown;
      //call back
    }
  },
}

</script>

<style lang='less' scoped>

  .img-box {
    width: 30px;
    height: 30px;
    margin: 5px;
    & img {
    width: 20px;
    height: 20px;
    }
}
</style>
