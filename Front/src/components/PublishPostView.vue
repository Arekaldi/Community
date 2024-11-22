<template>
  <el-input
    v-model="Title_Text"
    style="width: 400px; height: 60px; font-size: 20px; font-weight: 900;"
    :autosize="{minRows:1, maxRows:2}"
    type="textarea"
    placeholder="请输入标题"
  />
  <div style="margin: 20px" />
  <el-input
    v-model="Content_Text"
    style=" height:430px; width: 1000px;"
    :autosize="{minRows: 15, maxRows: 20}"
    type="textarea"
    placeholder="请输入内容"
  />
  <br/>
  <el-button type="primary" id="SubmitButton" size="large" @click="submitPost">提交</el-button>
</template>

<script lang="ts" setup>
  import { ElMessage, ElMessageBox } from 'element-plus'
  import type { Action } from 'element-plus'

  const open = () => {
    ElMessageBox.alert('This is a message', 'Title', {
      // if you want to disable its autofocus
      // autofocus: false,
      confirmButtonText: 'OK',
      callback: (action: Action) => {
        ElMessage({
          type: 'info',
          message: `action: ${action}`,
        })
      },
    })
  }
  import { useRoute } from 'vue-router'
  import { ref } from 'vue'
  import router from '../router'
  import axios from 'axios';
import { Logined, UserId, UserName} from '../scripts/UserStatus'
  const Title_Text = ref('')
  const Content_Text = ref('')
  const route = useRoute()
  const from = route.query.from;
  if(typeof(from) === "undefined")
    router.push({name: 'Home'})

  function GetNowTime() {
    let getTime = new Date().getTime();
    let time = new Date(getTime);
    let year = time.getFullYear();
    let month = (time.getMonth() + 1).toString().padStart(2, '0');
    let date = time.getDate().toString().padStart(2, '0');
    let hour = time.getHours().toString().padStart(2, '0');
    let minute = time.getMinutes().toString().padStart(2, '0');
    let second = time.getSeconds().toString().padStart(2, '0');
    return year + '-' + month + '-' + date + ' ' + hour + ':' + minute + ':' + second;
  }

  function submitPost() {
    if(Logined.value === false) {
        ElMessage.error("请先登录！");
        router.push({name: 'Login'})
        return;
    }
    if(Title_Text.value === '' || Content_Text.value === '') {
      ElMessage.error('标题或内容不能为空');
      return;
    }
    else if(Title_Text.value.length > 100) {
      ElMessage.error('标题不能超过100个字符');
      return;
    }
    else if(Content_Text.value.length > 2000) {
      ElMessage.error('内容不能超过2000个字符');
      return;
    }
    const data = {
        'User_id': UserId.value,
        'Title': Title_Text.value,
        'Text': Content_Text.value,
        'Time': GetNowTime(),
        'DATABASE': from
    };
    axios.post('http://localhost:5000/publishpost', data)
     .then( res => {
        if(res.data.includes('Error')) {
          ElMessage.error('发布失败')
        }
        else {
          ElMessage.success('发布成功')
          router.push({path: '/' + from})
        }
     })
  }

</script>

<style>
  #SubmitButton {
      position: absolute;
      right:310px;
      top:540px;
  }

  .el-textarea {
    font-family: PingFang SC, Microsoft YaHei, sans-serif;
  }
  
</style>
  