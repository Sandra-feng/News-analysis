<template>
  <div>
    <div class="input-button-container">
      <input type="text" v-model="newsUrl" placeholder="Enter news URL here">
      <button @click="fetchNews">Fetch News</button>
    </div>
    <div v-if="fetching">
      Fetching news...
    </div>

    <div v-else class="message">
      Enter a URL and click 'Fetch News' to display content.
    </div>
    <div v-if="newsData">
      <h1>{{ newsData.title }}</h1>
      <div v-html="newsData.content"></div>
      <div v-if="newsData.image_url && newsData.image_url !== 'No Image'">
        <img :src="newsData.image_url" alt="News Image">
      </div>
      <div v-else>
        wrong!
      </div>
    </div>
  </div>
</template>



  
  <script>
  export default {
    name: 'NewsFetcher',
    data() {
      return {
        newsData: null,
        newsUrl: '',
        fetching: false
      }
    },
    methods: {
      fetchNews() {
        const apiUrl = `http://127.0.0.1:5000/fetch-news?newsUrl=${encodeURIComponent(this.newsUrl)}`;
        fetch(apiUrl)
          .then(response => response.json())
          .then(data => {
            this.newsData = data;
            this.fetching = false;
          })
          .catch(error => {
            console.error('Error fetching news:', error);
            this.newsData = { title: 'Error fetching news', content: error.message, image_url: '' };
            this.fetching = false;
          });
      }
    }
  }
  </script>

 <style scoped>
 .input-button-container {
   display: flex;
   justify-content: center; /* 水平居中整个容器内容 */
   align-items: center; /* 垂直居中对齐子元素 */
 }

 .message {
  text-align: center;  /* 使文本水平居中 */
}
 input[type="text"] {
   width: 100%;
   max-width: 500px;
   padding: 10px;
   box-sizing: border-box;
   margin-right: 10px; /* 在输入框和按钮之间添加一些间隔 */
 }
 
 button {
   padding: 10px 20px;
 }
 
 h1 {
   margin: 20px;
   text-align: center;
   color: #2c3e50;
   margin-top: 60px;
   font-family: 方正苏新诗柳楷简体;
   font-size: 36px; 
 }

 div[v-html] {
  padding: 0 10%; /* 左右内边距设置为视口宽度的10% */
  margin: 20px 100%;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  font-family: 方正苏新诗柳楷简体;
  font-size: 28px; /* 增加字体大小 */
 }
 
 img {
   max-width: 100%;
   height: auto;
   display: block;
   margin-top: 20px;
   margin: 20px auto;
 }
 </style>
 
  
  
  