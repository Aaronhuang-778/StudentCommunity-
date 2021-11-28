<template>
<div>
      <el-row :gutter="20" style="margin-top:10px;">
        <el-col :span="8">
            <div class="grid-content bg-purple">
                 <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>基本信息</span>
        </div>
             <div class="mid">
                 <img :src="require('../src/assets/photo/' + this.picture + '.png')" style="position: center"/>
               </div>
          <div style="text-align: center; font-size: medium">
          {{this.user_name}}
          </div>
         <div class="personal-relation">
    </div>
       <div style="width: 85%;margin: auto; padding-top: 10px">
        <div style="float:left;width: 20%; text-align: center; font-size: 10px">
            关注:{{star_num}}
        </div>
        <div style="float:left;width: 20%; text-align: center; font-size: 10px">
            粉丝:{{follow_num}}
        </div>
         <div style="float:left;width: 33%; text-align: center"  v-show="this.user_id != this.other_id">
            <span style="width: 100px; float: right" v-if="isFollow === false">
            <i class="el-icon-star-off" @click="followClick" > 关注</i>
            </span>
          <span style="width: 100px; float: right" v-else>
            <i class="el-icon-star-on" @click="followReset"> 已关注</i>
            </span>
        </div>
    </div>
        <el-divider></el-divider>
        <div class="personal-relation">
        <div class="relation-item">手机号:  <div style="float: right; padding-right:20px;">{{user_phone}}</div></div>
    </div>
    <div class="personal-relation">
      <div class="relation-item">发布文章数:  <div style="float: right; padding-right:20px;">{{post_num}}</div></div>
    </div>
      </el-card>
        </div>
        </el-col>
    <el-col :span="16">
        <div class="grid-content bg-purple">


       <el-card class="box-card" v-show="this.user_id == this.other_id">
        <div slot="header" class="clearfix">
          <span>留言栏</span>
        </div>
        <el-card v-for="(item,index) in messages" :key="index" style="background: transparent">
          <div class="tabloid">
            {{item.content}}
            <el-button @click="deleteMessage(item.message_id)" style="float: right; size: 10px" type="danger">删除</el-button>
          </div>
          <i class="el-icon-user-solid article-icon">{{item.send_user_name}}</i>
          <i class="el-icon-date article-icon">
            {{formatted_time(item.message_date)}}
          </i>
        </el-card>
      </el-card>

      <el-card class="box-card" v-show="this.user_id != this.other_id">
        <div slot="header" class="clearfix">
          <span style="width: 100px; float: left">说点什么</span>
        </div>
        <el-form :model="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="留言内容" prop="content">
            <el-input type="textarea" v-model="ruleForm.content" style="background: transparent"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')" style="background: #aabeee; size: 6px">留言</el-button>
            <el-button @click="resetForm('ruleForm')" style="background: #e5e9f2" size="6px">重置</el-button>
          </el-form-item>
        </el-form>
      </el-card>

        </div>
        </el-col>
      </el-row>

</div>
</template>

<script>
import api from "../tools/user";

export default {
  name: "UserProfile",
  props:["user_id","other_id"],
  async mounted() {
    //this.user_id,this.other_id
    //return content
    let topass = this.other_id;
      let res = await api.getUser({"user_id": topass, "follow_id": this.user_id});
      console.log(res.data.data);
    this.user_name = res.data.data.user_name;
    this.picture = res.data.data.picture;
    this.user_phone = res.data.data.user_phone;
    this.follow_num = res.data.data.follow_num;
    this.star_num = res.data.data.star_num;
     this.post_num = res.data.data.post_num;
     this.messages = res.data.data.message;
     this.isFollow = res.data.data.isFollow !== -1;
  },
  data() {
    return {
      // dataForm:{
      //   user_name: 'ty',
      //   user_phone: '173567777777',
      //   picture: ''
      // },
      isFollow: false,
      messages:[],
      user_name: '',
      user_phone: '',
      picture: '',
      follow_num: '',
      star_num: '',
      post_num: '',
      ruleForm: {
          content: ''
      }
    }
  },
  methods: {
          async fetchlist() {
            let topass = this.other_id;
            let res = await api.getUser({"user_id": topass, "follow_id": this.user_id});
            console.log(res.data.data);
           this.messages = res.data.data.message;
          },

          async deleteMessage(message_id) {
            let res = await api.cancelmessage({"message_id": message_id});
            this.fetchlist();
          },
          formatted_time: function (iso_date_string) {
            const date = new Date(iso_date_string);
            return date.toLocaleDateString() + '  ' + date.toLocaleTimeString()
          },
          isSelf() {
            return this.user_id === this.other_id;
          },
          async followClick() {
            this.isFollow = true;
            let res = await api.follow({"follow_id":this.user_id, "star_id":this.other_id});
            this.follow_num++;
            //call
          },
          async followReset() {
            this.isFollow = false;
            // call
            let res = await api.cancelfollow({"follow_id": this.user_id, "star_id": this.other_id});
            this.follow_num--;
          },

    http() {
        return {
          send_user_id: this.user_id,
          receive_user_id: this.other_id,
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

<style lang="scss" scoped>
//卡片样式
 .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 100%;
  }
//文本样式区
  .name-role {
    font-size: 16px;
    padding: 5px;
   text-align:center;
  }
   .sender{
      text-align:center;
    }
.registe-info{
  text-align: center;
  padding-top:10px;
}
.personal-relation {
  font-size: 16px;
  padding: 0px 5px 15px;
  margin-right: 1px;
    width: 100%
}

.relation-item {
  padding: 12px;

}
.dialog-footer{
  padding-top:10px ;
  padding-left: 10%;
}
//布局样式区
   .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }

  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }

  .tabloid {
  color: black;
  font-size: 14px;
  margin-bottom: 10px;
}

  .article-icon,
.article-icon .tag {
  color: black;
  font-size: 13px;
  margin-right: 10px;
  text-decoration: none;
}
.article-icon .tag:hover {
  color: black;
  cursor: pointer;
}

.mid {
  display: flex;
  justify-content: center;
  align-items: center;
}
.mid img {
  width: 35%;
}
</style>
