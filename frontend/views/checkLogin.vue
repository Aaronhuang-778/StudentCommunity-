<template>

</template>

<script>
import api from '../tools/user';
export default {
  name: "checkLogin",
  mounted() {
    this.checkLogin();
  },
  methods: {
    async checkLogin() {
      let res = await api.checkLogin(null);
      if (res.data.code === 20000) {
        let user_id = res.data.data.user_id;
        let user_name = res.data.data.user_name;
        let picture = res.data.data.picture;
        this.$router.push({
          name: 'articlelist',
          params: {user_id: user_id, user_name: user_name, picture: picture}
        });
      } else {
        this.$router.push({name: 'newLog'});
      }
    }
  }
}
</script>

<style scoped>

</style>
