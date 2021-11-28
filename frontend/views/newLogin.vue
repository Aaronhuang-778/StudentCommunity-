<template>
  <div class="_body">
    <div class="container right-panel-active">
      <!-- Sign Up -->
      <div class="container__form container--signup">
        <form action="#" class="form" id="form1">
          <h2 class="form__title">注册</h2>
          <input type="text" placeholder="用户名" class="input" v-model="UpData.user_name"/>
          <select id="group" class="sex" @change="getSex($event)">
            <option value="1" >男</option>
            <option value="0" >女</option>
            <option value="" disabled selected hidden>性别</option>
          </select>
          <input type="text" placeholder="手机号码" class="input" v-model="UpData.user_phone" @blur="CheckPhone2"/>
          <span :class="tipsStyle2">{{ tips2 }}</span>
          <input type="password" placeholder="密码" class="input" v-model= "UpData.password" @blur="CheckPassWords"/>
          <span :class="tipsStyle_p">{{ tips_p }}</span>
          <button class="btn" @click="signup">注册</button>
        </form>
      </div>

      <!-- Sign In -->
      <div class="container__form container--signin">
        <form action="#" class="form" id="form2">
          <h2 class="form__title">登录</h2>
          <input type="text" placeholder="手机号码" class="input" v-model="InData.user_phone" @blur="CheckPhone1"/>
          <span :class="tipsStyle1">{{ tips1 }}</span>
          <input type="password" placeholder="密码" class="input" v-model= "InData.password" />
          <a class="link">忘记密码请联系管理员找回密码</a>
          <button class="btn" @click="signin">登录</button>
        </form>
      </div>

      <!-- Overlay -->
      <div class="container__overlay">
        <div class="overlay">
          <div class="overlay__panel overlay--left">
            <button class="btn" id="signIn" @click="InClick()">登录</button>
          </div>
          <div class="overlay__panel overlay--right">
            <button class="btn" id="signUp" @click="UpClick()">注册</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../tools/user';

export default {
  name: "newLogin",
  data() {
    return {
      InData: {
        user_phone: '',
        password: ''
      },
      UpData: {
        user_name:'',
        user_phone: '',
        password: '',
        sex: '',
      },
      tips1:'',//In
      tipsStyle1:'',
      tips2:'',
      tipsStyle2:'',
      tips_p:'',
      tipsStyle_p:'',
    }
  },
  methods: {
    InClick() {
      addEventListener("click", () => {
        const container = document.querySelector(".container");
        container.classList.remove("right-panel-active");
        this.data.UpData.user_phone = '';
        this.data.UpData.password = '';
      });
    },

    UpClick() {
      addEventListener("click", () => {
        const container = document.querySelector(".container");
        container.classList.add("right-panel-active");
        this.data.InData.user_phone = '';
        this.data.UpData.password = '';
      });
    },

    getSex(event) {
        if (event.target.value === '0') this.UpData.sex = 0;
        else this.UpData.sex = 1;
    },

    async signup() {
      if (this.tips2 === '' && this.tips_p === ''){
        let res = await api.register(this.$data);
        if (res.data.code === 20000) {//20000，返回code
          alert("注册成功");
        } else {//40000
          alert("用户名或手机号已存在");
        }
      }
	    else {
        alert("手机号或密码格式不符合要求");
      }
    },

    async signin() {
      if (this.tips1 === '') {
        let res = await api.signin(this.$data);
        if (res.data.code === 20000) {//20000，返回code
          // alert("登录成功");
          console.log(res);
          let user_id = res.data.data.user_id;
          let user_name = res.data.data.user_name;
          let picture = res.data.data.picture;
          this.$router.push({name: 'articlelist', params: {user_id: user_id, user_name: user_name, picture: picture}});
        } else {//40000
          alert("手机号不存在或密码错误");
        }
      } else {
        alert("手机号格式不符合要求");
      }
//      this.$router.push("/nop");
    },

    async CheckPassWords() {
        if (this.UpData.password.length < 8 || this.UpData.password.length > 32){
          this.tips_p = '密码长度在8-32字符'
          this.tipsStyle_p = 'tips-err'
          return false
        }
        else {
          this.tips_p= ''
          return true
        }
    },
    async CheckPhone1() {
        if (this.InData.user_phone.length !== 11){
          this.tips1 = '请输入正确的电话号码！'
          this.tipsStyle1 = 'tips-err'
          return false
        }
        else {
          this.tips1 = ''
          return true
        }
    },
    async CheckPhone2() {
        if (this.UpData.user_phone.length !== 11){
          this.tips2 = '请输入正确的电话号码！'
          this.tipsStyle2 = 'tips-err'
          return false
        }
        else {
          this.tips2 = ''
          return true
        }
    }
  }
}
</script>

<style scoped>

    ._body {
      align-items: center;
      background-color:  #e9e9e9;
      /*background: url("../src/assets/back3.jpg");*/
      /* 决定背景图像的位置是在视口内固定，或者随着包含它的区块滚动。 */
      /* https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-attachment */
      background-attachment: fixed;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
      display: grid;
      height: 100vh;
      place-items: center;
    }


    .form__title {
      font-weight: 300;
      margin: 0;
      margin-bottom: 1.25rem;
    }

    .link {
      color: var(--gray);
      font-size: 0.9rem;
      margin: 1.5rem 0;
      text-decoration: none;
    }

    .container {
      background-color:  #e9e9e9;
      border-radius: var(--button-radius);
      box-shadow: 0 0.9rem 1.7rem rgba(0, 0, 0, 0.25),
        0 0.7rem 0.7rem rgba(0, 0, 0, 0.22);
      height: 420px;
      max-width: 758px;
      overflow: hidden;
      position: relative;
      width: 100%;
    }

    .container__form {
      height: 100%;
      position: absolute;
      top: 0;
      transition: all 0.6s ease-in-out;
    }

    .container--signin {
      left: 0;
      width: 50%;
      z-index: 2;
    }

    .container.right-panel-active .container--signin {
      transform: translateX(100%);
    }

    .container--signup {
      left: 0;
      opacity: 0;
      width: 50%;
      z-index: 1;
    }

    .container.right-panel-active .container--signup {
      animation: show 0.6s;
      opacity: 1;
      transform: translateX(100%);
      z-index: 5;
    }

     .container__overlay {
      height: 100%;
      left: 50%;
      overflow: hidden;
      position: absolute;
      top: 0;
      transition: transform 0.6s ease-in-out;
      width: 50%;
      z-index: 100;
    }

    .container.right-panel-active .container__overlay {
      transform: translateX(-100%);
    }

    .overlay {
      background-color: var(--lightblue);
      /*background: url("../src/assets/back3.jpg");*/
      background-attachment: fixed;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
      height: 100%;
      left: -100%;
      position: relative;
      transform: translateX(0);
      transition: transform 0.6s ease-in-out;
      width: 200%;
    }

    .container.right-panel-active .overlay {
      transform: translateX(50%);
    }

     .overlay__panel {
      align-items: center;
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: center;
      position: absolute;
      text-align: center;
      top: 0;
      transform: translateX(0);
      transition: transform 0.6s ease-in-out;
      width: 50%;
    }

     .overlay--left {
      transform: translateX(-20%);
    }

     .container.right-panel-active .overlay--left {
      transform: translateX(0);
    }

     .overlay--right {
      right: 0;
      transform: translateX(0);
    }

     .container.right-panel-active .overlay--right {
      transform: translateX(20%);
    }

     .btn {
      background-color: var(--blue);
      background-image: linear-gradient(90deg, var(--blue) 0%, var(--lightblue) 74%);
      border-radius: 20px;
      border: 1px solid var(--blue);
      color: var(--white);
      cursor: pointer;
      font-size: 0.8rem;
      font-weight: bold;
      letter-spacing: 0.1rem;
      padding: 0.9rem 4rem;
      text-transform: uppercase;
      transition: transform 80ms ease-in;
    }

    .form>.btn {
      margin-top: 1.5rem;
    }

    .btn:active {
      transform: scale(0.95);
    }

    .btn:focus {
      outline: none;
    }

    .form {
      background-color: var(--white);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      padding: 0 3rem;
      height: 100%;
      text-align: center;
    }

    .input {
      background-color: #fff;
      border: none;
      padding: 0.9rem 0.9rem;
      margin: 0.5rem 0;
      width: 100%;
    }
    .sex {
      background-color: #fff;
      border: none;
      padding: 0.5rem 0.5rem;
      margin: 0.5rem 0.5rem;
      height: 10%;
      width: 312px;
    }

    @keyframes show {

      0%,
      49.99% {
        opacity: 0;
        z-index: 1;
      }

      50%,
      100% {
        opacity: 1;
        z-index: 5;
      }
    }
</style>
