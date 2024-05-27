<template>
  <div>
    <Inputnews>
      <!-- 文本输入框 -->
    <fieldset class="text-intro">
        <legend>新闻信息</legend>
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


    <!--&lt;!&ndash; 图片上传组件 &ndash;&gt;-->
    <!--<el-upload-->
      <!--class="upload-demo"-->
      <!--action="http://localhost:5000/upload_image"-->
      <!--list-type="picture-card"-->
      <!--:on-preview="handlePicturePreview"-->
      <!--:on-remove="handlePictureRemove"-->
      <!--:before-remove="beforePictureRemove"-->
      <!--:on-change="handleChange"-->
      <!--:auto-upload="false">-->
      <!--<i class="el-icon-plus"></i>-->
    <!--</el-upload>-->

    <!--<el-button type="primary" @click="submitAll">提交所有数据</el-button>-->

    <!--<el-dialog :visible.sync="dialogVisible">-->
      <!--<img width="100%" :src="dialogImageUrl" alt="预览图片" />-->
    <!--</el-dialog>-->

    </Inputnews>

  </div>
</template>


<script>
// import axios from 'axios';
export default {
  name: "Inputnews",
  // data() {
  //   return {
  //     textValue: '', // 绑定到文本输入框的数据
  //     fileList: [], // 存储上传的图片列表
  //     dialogImageUrl: '', // 图片预览的 URL
  //     dialogVisible: false // 控制预览对话框的显示
  //   };
  }
//   methods: {
//     // handlePicturePreview(file) {
//     //   this.dialogImageUrl = file.url;
//     //   this.dialogVisible = true;
//     // },
//     // handlePictureRemove(file, fileList) {
//     //   this.fileList = fileList;
//     // },
//     // beforePictureRemove(file, fileList) {
//     //   return this.$confirm(`确定移除 ${file.name}？`);
//     // },
//     // handleChange(file, fileList) {
//     // // 可以选择立即上传文件，或者只处理最后选择的文件
//     //     this.uploadFile(file.raw);
//     //  },
//     // uploadFile(file) {
//     //   const formData = new FormData();
//     //   formData.append('file', file);
//     //   axios.post('http://localhost:5000/upload_image', formData, {
//     //       headers: {
//     //     'Content-Type': 'multipart/form-data'
//     //           }
//     //   })
//     //  .then(() => {
//     //    this.$message.success('上传成功！');
//     //  })
//     //  .catch(() => {
//     //    this.$message.error('上传失败！');
//     //  });
//     //  },
//     // submitAll() {
//     //   const formData = new FormData();
//     //   this.fileList.forEach(file => {
//     //     formData.append('files', file.raw);
//     //   });
//     //   formData.append('text', this.textValue);
//     //
//     //   axios.post('http://localhost:5000/upload_data', formData, {
//     //     headers: {
//     //       'Content-Type': 'multipart/form-data'
//     //     }
//     //   })
//       // .then(response => {
//       //   this.$message.success('上传成功！');
//       // })
//       // .catch(error => {
//       //   this.$message.error('上传失败！');
//       // });
//     }
//   }
// }
</script>
<style>
  .text-intro {
    margin-top: 20px;
    border: 0;
    border-top: 2px solid #ddd;
    text-align: center;
  }
</style>