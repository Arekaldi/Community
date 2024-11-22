<template>
    <div>
        <el-space wrap>
            <el-card style="height:400px; width: 600px">
                <template #header>
                    <div class="card-header">
                        <span style="font-size: 24px; align-items: center; justify-content: center; display: flex;" >登录账户</span>
                    </div>
                </template>
                <div><br /></div>
                <div><br /></div>
                <div style="justify-content: center; align-items: center; display: flex;">
                    <el-input
                        v-model="UserNameLogin"
                        style="width: 240px;"
                        placeholder="用户名"
                        :prefix-icon="User"
                    />
                </div>
                <div><br /></div>
                <div><br /></div>
                <div style="justify-content: center; align-items: center; display: flex;">
                    <el-input
                        v-model="PasswordLogin"
                        style="width: 240px;"
                        type="password"
                        placeholder="密码"
                        :prefix-icon="Lock"
                    />
                </div>
                <div><br /></div>
                <div style="justify-content: center; align-items: center; display: flex;">
                    <el-button type="primary" plain @click="goVerifyPassword">登录</el-button>                    
                </div>
                <div><br /></div>
                <div style="justify-content: center; align-items: center; display: flex; font-size: 12px">
                    <span>暂无账号？<router-link to="/register" style="text-decoration: none;" >注册</router-link></span>
                </div>
            </el-card>
        </el-space>
    </div>
</template>

<script lang="ts" setup>

import {
    User,
    Lock
} from "@element-plus/icons-vue"

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

import { ref } from 'vue'
import {Logined, UserId, UserName} from '../scripts/UserStatus'
import { ElAlert } from "element-plus";
import axios from 'axios'
import router from "@/router";

let UserNameLogin = ref('')
let PasswordLogin = ref('')

if(Logined.value === true) {
    router.push('/');
    ElMessage.error("您已经登录，请勿重复登录")    
}


async function goVerifyPassword() {
    if (UserNameLogin.value === '' || PasswordLogin.value === '') {
        ElMessage.error('账号或密码不能为空')
    }

    const data = {'User_Name': UserNameLogin.value}
    await axios.post('http://localhost:5000/login', data)
        .then(response => {
            if(response.data === 'User not found') {
                ElMessage.error('账号不存在')
                UserNameLogin.value = PasswordLogin.value = '';
            }
            else {
                if(response.data[2] === PasswordLogin.value) {
                    Logined.value = true;
                    UserId.value = response.data[0];
                    UserName.value = response.data[1];
                    ElMessage.success('登录成功')
                    router.push('/');
                }
                else {
                    ElMessage.error('账号或密码错误')
                    PasswordLogin.value = '';
                }
            }
        })
}

</script>

<style scoped>

    .el-space {
        position: absolute;
        top: 100px;
        left: 280px;
    }

</style>