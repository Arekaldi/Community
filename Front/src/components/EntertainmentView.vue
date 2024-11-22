<template>
    <!-- 下文为搜索框，暂时不用，后续有需求再添加 -->
    <!-- <form @keypress.enter="SearchFor">
        <el-input
            class="search-input"
            v-model="search_input"
            style="width: 240px"
            placeholder="搜索"
            :prefix-icon="Search"
        />
    </form> -->
    <el-col
    v-if=" (res_from_server.length === 0) "
    style="color:black; align-items:center; display:flex; height: 600px; font-size: 40px; position:absolute; left: 29.5%;"
    >
        {{ '暂无帖子，快来发布吧！' }}
    </el-col>
    <el-scrollbar style="width: 1050px">
        <el-space direction="vertical">
            <div v-for="(Article, index) in res_from_server">
                <el-card id="card-info" style="height: 60px; background-color:#409EFF">
                    <el-row :span="24" style="font-size:20px; color:white">
                        <!-- 接口：用户昵称 -->
                        <el-col :span="8" > 
                            {{ 'from:' + post_User_Name[res_from_server.length - 1 - index] }}
                            <el-button type="info" :icon="Delete" circle
                            @click="handleDelete(res_from_server[res_from_server.length - 1 - index][5])"
                            v-if="res_from_server[res_from_server.length - 1 - index][0] === UserId"></el-button>
                            <el-button type="info" :icon="Delete" circle
                            @click="handleDelete(res_from_server[res_from_server.length - 1 - index][5])"
                            v-else-if="UserId.toString() === '100000'"></el-button>
                        </el-col>
                        <el-col :span="10" :push="10"> {{ res_from_server[res_from_server.length - 1 - index][3].slice(0, Article[3].length - 3) }} </el-col>
                    </el-row>
                </el-card>
                <el-card class="box-card" style="width: 1000px; height: 280px;">
                    <template #header>
                        <div class="card-header">
                            <span style="font-size: 25px"> {{res_from_server[res_from_server.length - 1 - index][1]}}</span>
                        </div>
                    </template>
                    <div style="font-size: 20px;"> {{ res_from_server[res_from_server.length - 1 - index][2] }} </div>
                </el-card>
            </div>
        </el-space>
        <el-divider />
    </el-scrollbar>
    <!-- <ul v-for="Article in res_from_server">
        <li> {{ 'User_id' }}: {{ Article[0] }} </li>
        <li> {{ 'Title' }}: {{ Article[1] }} </li>
        <li> {{ 'Content' }}: {{ Article[2] }} </li>
        <li> {{ 'Time' }}: {{ Article[3] }} </li>
        <li> {{ 'Position' }}: {{ Article[4] }} </li>
    </ul> -->
    <el-button type="primary" id="publish-btn" size="large" @click="publishPost">
        <el-icon class="el-icon"><UploadFilled /></el-icon>
        发布帖子
    </el-button>

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

import {
    UploadFilled,
    Search,
    Delete
} from "@element-plus/icons-vue"


import HomeView from '../components/HomeView.vue'
import { nextTick } from "vue";
import router from "@/router";
import { ref, toRefs } from "vue";
import axios from "axios"
import { Logined, UserId, UserName} from '../scripts/UserStatus'

// res_from_server = {};
let res_from_server = ref(null);
let post_User_Name = ref([]);

function getContent() {
    axios.get("http://localhost:5000/entertainment")
    .then(Response => {
        res_from_server.value = Response.data;
        for(let i = 0; i < res_from_server.value.length; i++) {
            axios.post('http://localhost:5000/get_name_by_id', { 'User_id': res_from_server.value[i][0] })
                .then(response => {
                    post_User_Name.value[i] = response.data;
                })
        }
    })
}

getContent();
console.log(typeof(UserId.value));
console.log(UserId.value);

function publishPost() {
    if(Logined.value === false) {
        ElMessage.error("请先登录！");
        return;
    }
        
    router.push({ name: 'PublishPost', query: { from: "entertainment" } })
}

function handleDelete(Post_id) {
    ElMessageBox.confirm('确认删除该帖子吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
    }).then(() => {
        axios.post('http://localhost:5000/delete_post', { 'Post_id': Post_id })
        getContent();
        getContent();
        ElMessage.success('删除成功！');
    }).catch(() => {
        ElMessage.info('已取消删除');
    });

}

</script>

<style>

.search-input {
    position: absolute;
    top: 40px;
    right: 0;
}
.example-pagination-block + .example-pagination-block {
  margin-top: 10px;
}
.example-pagination-block .example-demonstration {
  margin-bottom: 16px;
}
.el-card {
    #card-info {
        --el-card-padding:0;
    }
}

</style>