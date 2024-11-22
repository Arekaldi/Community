//TODO 增加帖子长度、增加帖子详情页、增加评价区功能、增加更改昵称、更改头像功能、加强安全性


<script setup>
import Header from './components/Header.vue';
import Navigation from './components/Navigation.vue';
import { RouterView } from 'vue-router';
import { ElContainer, ElHeader, ElAside, ElMain, ElFooter } from 'element-plus';

</script>

<template>

<el-container>
    <el-header>
        <Header />
    </el-header>
    <el-container>
        <el-aside>
            <Navigation />
        </el-aside>
        <el-container>
            <el-main>
                <img draggable="false" src="../../public/background-image.jpeg" alt="backgroundimg">
                <RouterView />
            </el-main>
        </el-container>
        
    </el-container>
    
    
</el-container>

</template>

<style>

.el-main {
    img {
        opacity: 0.2;
        position: absolute;
        height: 580px;
        left: 300px;
        display: inline;
    }
    position: relative;
    width: 1300px;
    height:600px;
}

#publish-btn {
    position: absolute;
    top: 50px;
    right:0;
}

</style>