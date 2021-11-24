<template>
<div>
  {{user_name}}信息
      <el-row :gutter="20" style="margin-top:10px;">
        <el-col :span="8">
            <div class="grid-content bg-purple">
                 <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>个人中心</span>
        </div>
          <div class="name-role">
          <span class="sender">Admin - {{user_name}}</span>
        </div>
        <div class="registe-info">
          <span class="registe-info">
            注册时间：
            <li class="fa fa-clock-o"></li>
             2020/4/10 9:40:33
          </span>
        </div>
        <el-divider></el-divider>
        <div class="personal-relation">
        <div class="relation-item">手机号:  <div style="float: right; padding-right:20px;">{{user_phone}}</div></div>
    </div>
    <div class="personal-relation">
      <div class="relation-item">发布文章数:  <div style="float: right; padding-right:20px;">{{post_num}}</div></div>
    </div>
       <div class="personal-relation">
      <div class="relation-item">关注人数:  <div style="float: right; padding-right:20px;">{{star_num}}</div></div>
    </div>
     <div class="personal-relation">
      <div class="relation-item">粉丝人数:  <div style="float: right; padding-right:20px;">{{follow_num}}</div></div>
    </div>
      </el-card>
        </div>
        </el-col>
    <el-col :span="16">
        <div class="grid-content bg-purple">
       <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>基本资料</span>
        </div>
        <div>
          <el-form label-width="80px" v-model="dataForm" size="small" label-position="right">
          <el-form-item label="用户名" prop="nickName">
          <el-input  auto-complete="off" v-model="dataForm.user_name"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="phone">
          <el-input auto-complete="off" v-model="dataForm.user_phone"></el-input>
        </el-form-item>
          <el-form-item label="头像" prop="picture">
          <el-upload
            class="avatar-uploader"
            action="https://jsonplaceholder.typicode.com/posts/"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload">
            <img v-if="dataForm.picture" :src="dataForm.picture" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
          <el-button size="mini" type="primary">提交</el-button>
          <el-button size="mini" type="warning" >关闭</el-button>
        </div>
        </div>
      </el-card>
        </div>
        </el-col>

      </el-row>

</div>
</template>

<script>
export default {
  name: "UserProfile",
  props:["user_id", "user_name"],
  data() {
    return {
      dataForm:{
        user_name: 'ty',
        user_phone: '173567777777',
        picture: ''
      },
      user_name: 'ty',
      user_phone: '173567777777',
      picture: '',
      follow_num: '0',
      star_num: '0',
      post_num: '0',
    }
  },
  methods: {
      handleAvatarSuccess(res, file) {
        this.picture = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isJPG && isLt2M;
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
</style>
