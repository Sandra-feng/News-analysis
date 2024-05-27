<template>
  <div>
    <fieldset class="spider-intro">
      爬取数据
    </fieldset>

    <div class="block">
      <el-date-picker
          style="margin-top: 10px"
          v-model="timeValue"
          type="daterange"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          :default-time="['00:00:00', '23:59:59']">
      </el-date-picker>
      <el-button id="spider" type="primary" @click="onSpider">开始爬取</el-button>
    </div>
    <fieldset class="text-intro">
    新闻信息
    </fieldset>
    <div class="test">
        <el-form style="width: 75%" ref="form"  id="caseText" label-width="80px">
          <el-form-item style="margin-left: -18%;" >
            <el-input
                style="width: 100%;
                margin-top:20px"
                :rows="9"
                type="textarea"
                v-model="textValue">{{textValue}}
            </el-input>
          </el-form-item>
        </el-form>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      timeValue: []
    };
  },
  methods: {
    onSpider() {
      if (this.timeValue.length === 0) {
        this.$alert('请选择时间进行自动化爬取！', '未选择时间', {
          confirmButtonText: '确定',
        });
      } else {
        const path = 'http://localhost:5000/onSpider';
        const timeData = {
          startTime: this.timeValue[0].toLocaleDateString(),
          endTime: this.timeValue[1].toLocaleDateString()
        };
        axios.post(path, timeData)
          .then(response => {
            this.$alert('爬取完成: ' + response.data.message, '爬取成功', {
              confirmButtonText: '确定',
            });
          })
          .catch(error => {
            console.error('爬取失败:', error);
            this.$alert('爬取失败，请检查网络或服务器设置', '错误', {
              confirmButtonText: '确定',
            });
          });
      }
    }
  }
}
</script>

<style scoped>

  .spider-intro{
    margin-top: 20px;
    border: 0;
    font-size: large;
    font-family: 方正苏新诗柳楷简体;
    font-weight: bold;
    color:#FFFF;
  }
    .text-intro {
    margin-top: 20px;
    border: 0;
    color:#FFFF;
    font-size: large;
    font-weight: bold;
    font-family: 方正苏新诗柳楷简体;
  }
    .test{
    align-content: center;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    height : 240px;
    width: 50%;
    margin-left: 25%;
  }
</style>