<template>
  <div>

    <div class="background-card">


            <el-card :body-style="{ padding: '0px' }" class="card1">
              <img src="../assets/smile.png" class="image">
              <div style="padding: 14px;">
                <span class="intro1">情感分析</span>
                <br>
                <br>
                <span class="intro2">检测新闻偏见和倾向性、舆情预警</span>
              </div>
            </el-card>

      <el-card :body-style="{ padding: '0px' }" class="card2">
        <img src="../assets/lawHall.png" class="image">
        <div style="padding: 14px;">
          <span class="intro1">假新闻检测</span>
          <br>
          <br>
          <span class="intro2">保护公众免受错误信息影响</span>
        </div>
      </el-card>

      <el-card :body-style="{ padding: '0px' }" class="card3">
        <img src="../assets/sum.png" class="image">
        <div style="padding: 14px;">
          <span class="intro1">文本总结</span>
          <br>
          <br>
          <span class="intro2">提高效率，提升用户体验</span>
        </div>
      </el-card>

    </div>

    <div style="background:linear-gradient(to left,#FFFFFF,#b6b6b6,#FFFFFF);
    height:3px;
    position: relative;
    margin-top: 30px"></div>

  </div>
</template>

<script>
export default {
  name: "cardBody"
}
</script>

<style scoped>

  .background-card{
    position: relative;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    background-color: #F5F9FC;
    height: 250px;
    width: 74%;
    margin-top: 30px;
    margin-left: 13%;
  }

  .card1{
    position: absolute;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
    background-color: #F0FFFF;
    height: 73%;
    width: 30%;
    top:15%;
    left:2%;
    z-index: 1;
  }
  .card2{
    position: absolute;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
    background-color: #F0FFFF;
    height: 73%;
    width: 30%;
    top:15%;
    left:35%;
    z-index: 1;
  }
  .card3{
    position: absolute;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
    background-color: #F0FFFF;
    height: 73%;
    width: 30%;
    top:15%;
    left:68%;
    z-index: 1;
  }

  .intro1{
    font-family: "思源宋体 CN Heavy";
    font-size: xx-large;
    color: #1D5C93;

  }

  .intro2{
    font-family: "方正苏新诗柳楷简体";
    font-size: medium;
    color: #2C3E50;
  }

  .image {
    width: 20%;
    margin-left: 40%;
    margin-top: 4%;;
    display: block;
  }

</style>

