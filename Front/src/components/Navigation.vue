<template>
  <el-row class="tac">
    <el-col :span="12">
      <el-menu
        default-active= '/'
        class="el-menu"
        lang="zh-CN"
        router
      >
      <!-- @open="handleOpen"
      @close="handleClose" -->
        <!-- <el-sub-menu index="1"> -->
          <!-- <el-menu-item-group title="Group One">
            <el-menu-item index="1-1">item one</el-menu-item>
            <el-menu-item index="1-2">item two</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="Group Two">
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          <el-sub-menu index="1-4">
            <template #title>item four</template>
            <el-menu-item index="1-4-1">item one</el-menu-item>
          </el-sub-menu> -->
        <!-- </el-sub-menu> -->
        <el-menu-item index="/" >
          <el-icon><home-filled /></el-icon>
          <span>首页</span>
        </el-menu-item>
        <el-menu-item index="Study" >
          <el-icon><notebook /></el-icon>
          <span>学习区</span>
        </el-menu-item>
        <el-menu-item index="Sport" >
          <el-icon><football /></el-icon>
          <span>体育区</span>
        </el-menu-item>
        <el-menu-item index="Entertainment" >
          <el-icon><monitor /></el-icon>
          <span>娱乐区</span>
        </el-menu-item>
        <!-- <el-menu-item index="Comment" >
          <el-icon><comment /></el-icon>
          <span>评价区</span>
        </el-menu-item> -->
      </el-menu>
    </el-col>
  </el-row>
</template>

<script>

import router from '@/router';
import {
  Notebook,
  HomeFilled,
  Comment,
  Football,
  Monitor
} from '@element-plus/icons-vue'

export default {

  data() {
    return {

    }
  },
  components: {
    Notebook,
    HomeFilled,
    Comment,
    Football,
    Monitor
  },
}



</script>

<style>

  .el-menu {
    width: 220px;
  }

</style>