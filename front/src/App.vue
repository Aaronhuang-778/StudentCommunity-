<template>
  <div id="app">
    <Nav v-if="isShowNav" />
      <router-view />
    <ArrowUp></ArrowUp>
  </div>
</template>
<script lang="ts">
import { Vue, Watch } from "vue-property-decorator";
import Component from "vue-class-component";
import { Route } from "vue-router";
import Nav from "@/components/nav.vue"; // @ is an alias to /src
import Slider from "@/components/slider.vue"; // @ is an alias to /src
import Footer from "@/components/footer.vue"; // @ is an alias to /src
import ArrowUp from "@/components/arrowUp.vue"; // @ is an alias to /src


@Component({
  components: {
    Nav,
    Slider,
    ArrowUp,
    Footer
  }
})
export default class App extends Vue {
  private isShowNav: boolean = false;
  private isShowSlider: boolean = false;
  mounted(): void {
    this.routeChange(this.$route, this.$route);
  }
  @Watch("$route")
  routeChange(val: Route, oldVal: Route): void {
    const referrer: any = document.getElementById("referrer");
    if (val.path === "/") {
      this.isShowNav = false;
      referrer.setAttribute("content", "always");
    } else {
      this.isShowNav = true;
      referrer.setAttribute("content", "never");
    }
    if (
      val.path === "/articles" ||
      val.path === "/ground" ||
      val.path === "/archive" ||
      val.path === "/release" ||
      val.path === "/project" ||
      val.path === "/timeline" ||
      val.path === "/message"
    ) {
      this.isShowSlider = true;
    } else {
      this.isShowSlider = false;
    }
  }
}
</script>

<style lang="less">
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
@import url("./less/index.less");

#app {
  margin: 0;
  padding: 0;
  height: 100%;
}
img {
  vertical-align: bottom;
}
</style>
