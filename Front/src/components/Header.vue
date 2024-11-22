<template>
    <el-page-header :icon="null">
      <template #content>
        <div class="flex items-center">
          <el-avatar
            :size="32"
            class="mr-3"
            src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
          />
          <!-- 上面接口用来获取用户头像，下面是显示用户信息 -->
           <!-- 后端接口：获取用户信息 -->
          <span class="text-large font-600 mr-3" v-if="!Logined" > {{ "你好，小航" }} </span>
          <span class="text-large font-600 mr-3" v-if="Logined" > {{"你好，" + UserName }} </span>
        </div>
      </template>
      <template #title>
        <a href="https://buaa.edu.cn" target="_blank">
          <img src="/Head-Title2.jpeg" height="58px" width="184px">
        </a>
      </template>
      <template #extra>
        <div class="flex items-center">
          <el-button @click="handleLogin" v-if="!Logined">登录</el-button>
          <el-button @click="handleRegister"  type="primary" class="ml-2" v-if="!Logined">注册</el-button>
          <el-button @click="handleExitLogin"  type="primary" class="ml-2" v-if="Logined">退出登录</el-button>
        </div>
      </template>
    </el-page-header>
</template>

<script lang="ts" setup>
import { ElMessage, ElMessageBox } from 'element-plus'
import type { Action } from 'element-plus'

const open = () => {
    ElMessageBox.alert('退出登录成功', '', {
        // if you want to disable its autofocus
        // autofocus: false,
        confirmButtonText: 'OK',
        // callback: (action: Action) => {
        // ElMessage({
        //     type: 'info',
        //     message: `action: ${action}`,
        // })
        // },
    })
}


import router from '@/router';
import { Logined, UserId, UserName} from '../scripts/UserStatus'

function handleLogin() {
  router.push('/login');
}

function handleRegister() {
  router.push('/register');
}

function handleExitLogin() {
  Logined.value = false;
  UserId.value = null;
  UserName.value = null;
  open();
  router.push('/login');
}

</script>