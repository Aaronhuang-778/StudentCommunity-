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
import api from "../../tools/user";
export default {
  name: "Like",
  props: {article: Object, user_id: Number},
  data () {
    return {
      isUp: this.article.like_id !== -1,
      isDown: this.article.unlike_id !== -1,
      like_num:this.article.like_number,
      unlike_num: this.article.unlike_number
    };
  },
  created () {

  },
  mounted () {
    console.log(this.article.post_id);
  },
  computed: {},
  watch: {},
  methods: {
    async handleClickUp() {
      if (this.isUp) {
        let res = await api.cancellike({"post_id": this.article.post_id, "user_id": this.user_id});
        console.log("----------------------");
        // this.cancellike();
        this.like_num--;
      } else {
        let res = await api.like({"post_id": this.article.post_id, "user_id": this.user_id});
        // this.likee();
        this.like_num++;
      }
      this.isUp = !this.isUp;
      //call back
    },
    // async cancellike() {
    //   console.log("+++++++++++++++");
    //   let res = await api.cancellike({"post_id": this.article.post_id, "user_id": this.user_id});
    //   console.log(res.data.code);
    // },
    // async likee() {
    //   let res = await api.like({"post_id": this.article.post_id, "user_id": this.user_id});
    // },
    async handleClickDown() {
      if (this.isDown) {
        let res = await api.cancelunlike({"post_id": this.article.post_id, "user_id": this.user_id});
        this.unlike_num--;
      } else {
        let res = await api.unlike({"post_id": this.article.post_id, "user_id": this.user_id});
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
