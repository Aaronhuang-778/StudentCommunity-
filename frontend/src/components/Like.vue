<template>
      <div >
        <span class="img-box" @click="handleClickUp">
          <img v-if="isUp" src="../assets/like.png" alt=""/>
          <img v-else src="../assets/tolike.png" alt="" />
        </span>
        <span class="img-box" @click="handleClickDown">
          <img v-if="isDown" src="../assets/dislike.png" alt=""/>
          <img v-else src="../assets/todislike.png" alt="" />
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
      isDown: false
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
      this.isUp = !this.isUp;
      //call back
    },
    handleClickDown() {
      this.isDown = !this.isDown;
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
    width: 30px;
    height: 30px;
    }
}
</style>
