<template>
<el-form :model="ruleForm" label-width="100px" class="demo-ruleForm">
  <el-form-item label="目标手机号" prop="name">
    <el-input v-model="ruleForm.phone"></el-input>
  </el-form-item>
  <el-form-item label="留言内容" prop="content">
    <el-input type="textarea" v-model="ruleForm.content"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">发送</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
  </el-form-item>
</el-form>
</template>

<script>
import api from '../tools/user';
export default {
  name: "message",
  props:["user_id", "user_name"],
   data() {
      return {
        ruleForm: {
          phone: '',
          content: ''
        }
      };
    },
    methods: {
      http() {
        return {
          send_user_id: this.user_id,
          receive_user_phone: this.ruleForm.phone,
          content: this.ruleForm.content
        }
      },
      async submitForm(formName) {
        let res = await api.message(this.http());
        if(res.data.code === 20000){
          alert("留言成功");
        } else{
          alert("留言失败");
        }
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
}
</script>

<style scoped>

</style>
