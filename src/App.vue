<!-- <template>
  <div id="app">
    <div>
      <head-title style="position: fixed; top: 0; z-index: 4"></head-title>
    </div>

    <div>
      <news-fetcher style="margin-top: 100px; z-index: 4"></news-fetcher>
    </div>

    <div>
      <card-body></card-body>
    </div> -->

    <!-- <div>
      <main-body style="margin-bottom: 100px"></main-body>
    </div> -->

    <!-- <div>
      <end-title style="position: fixed; bottom: -15px; z-index: 4"></end-title>
    </div>
  </div>
</template>

<script>
import headTitle from "@/components/headTitle";
// import textTitle from "@/components/textTitle";
import NewsFetcher from './components/NewsFetcher';
// import cardBody from "@/components/cardBody";
// import mainBody from "@/components/mainBody";
import endTitle from "@/components/endTitle";


export default {
  name: 'App',
  components: {
    headTitle,
    NewsFetcher,
    // mainBody,
    endTitle,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif, 方正苏新诗柳楷简体;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> --> 

<template>
  <el-container style="height: 100vh;">
    <el-header style="height: auto; padding: 0;">
      <head-title></head-title>
    </el-header>

    <el-container>
      <el-aside width="200px" style="background-color: #35495e; color: white;">
        <el-menu
          default-active="1"
          background-color="transparent"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="handleSelect">
          <el-menu-item index="1">新闻爬取</el-menu-item>
          <el-menu-item index="2">理解功能</el-menu-item>
          <el-menu-item index="3">新闻分类</el-menu-item>
        </el-menu>
      </el-aside>

      <el-main>
        <div>
          <news-fetcher style="margin-top: 100px; z-index: 4"></news-fetcher>
        </div>
        <div v-if="activeComponent === '理解'">
          <h1>理解功能 (待实现)</h1>
        </div>
        <div v-if="activeComponent === '分类'">
          <h1>功能 (待实现)</h1>
        </div>
      </el-main>
    </el-container>

    <el-footer style="height: auto; padding: 0;">
      <end-title></end-title>
    </el-footer>
  </el-container>
</template>

<script>
import headTitle from '@/components/headTitle';
import NewsFetcher from './components/NewsFetcher';
import endTitle from '@/components/endTitle';

export default {
  name: 'App',
  components: {
    headTitle,
    NewsFetcher,
    endTitle,
  },
  data() {
    return {
      activeComponent: ''  // 控制激活的组件
    };
  },
  methods: {
    handleSelect(key) {
      this.activeComponent = key;
    }
  }
}
</script>

<style>
.el-header, .el-footer { background: #333; color: white; }
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif, 方正苏新诗柳楷简体;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
