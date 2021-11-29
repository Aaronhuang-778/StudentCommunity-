<template>
  <div id="app">
<!--    <div class="header-background">-->
<!--    	<img src="./assets/seesky.jpg" width="100%" height="100%" style="opacity: 0.4" />-->
<!--    </div>`-->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  html,
  body,
  :root {
      /* COLORS */
      --white: #e9e9e9;
      --gray: #333;
      --blue: #0367a6;
      --lightblue: #008997;

      /* RADII */
      --button-radius: 0.7rem;

      /* SIZES */
      --max-width: 758px;
      --max-height: 420px;

      font-size: 16px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
        Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    }
  #app {
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
  border:0;
  }

  .header-background {
    position: absolute;
    top :0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
  }

  .el-textarea__inner,.el-input__inner{
        background: transparent ;
   }

</style>
