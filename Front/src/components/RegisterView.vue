<template>
    <div>
        <el-space wrap>
            <el-card style="height:400px; width: 600px">
                <template #header>
                    <div class="card-header">
                        <span style="font-size: 24px; align-items: center; justify-content: center; display: flex;" >注册账户</span>
                    </div>
                </template>
                <div><br /></div>
                <div><br /></div>
                <div style="justify-content: center; align-items: center; display: flex;">
                    <el-input
                        v-model="UserNameRegister"
                        style="width: 240px;"
                        placeholder="用户名"
                        :prefix-icon="User"
                    />
                </div>
                <div><br /></div>
                <div><br /></div>
                <div style="justify-content: center; align-items: center; display: flex;">
                    <el-input
                        v-model="PasswordRegister"
                        style="width: 240px;"
                        type="password"
                        placeholder="密码"
                        :prefix-icon="Lock"
                    />
                </div>
                <div><br /></div>
                <div style="justify-content: center; align-items: center; display: flex;">
                    <el-button type="primary" plain @click="goVerifyPassword">注册</el-button>                    
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
import { Logined, UserId, UserName} from '../scripts/UserStatus'
import { ElAlert } from "element-plus";
import axios from 'axios'
import route from 'vue-router'
import router from "@/router";

let UserNameRegister = ref('')
let PasswordRegister = ref('')


if(Logined.value === true) {
    router.push('/');
    ElMessage.error("您已经登录，无需注册")    
}

async function goVerifyPassword() {
    if (UserNameRegister.value === '' || PasswordRegister.value === '') {
        ElMessage.error('账号或密码不能为空')
    }

    const UserId_tot = ref<any>(null)
    await axios.get('http://localhost:5000/latest_user_id')
        .then(response => {
            UserId_tot.value = response.data;
        })

    const data = {
        'User_Id': UserId_tot.value,
        'User_Name': UserNameRegister.value,
        'User_Password': PasswordRegister.value
    }
    await axios.post('http://localhost:5000/register', data)
       .then(response => {
            if(response.data.includes('Error')) {
                ElMessage.error('注册失败，该昵称已被占用')
                console.log(response.data)
            }
            else {
                ElMessage.success('注册成功')
                router.push('/');
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