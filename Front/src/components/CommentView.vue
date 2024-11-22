<script setup>
import {Logined, UserId, UserName} from '../scripts/UserStatus'
</script>
<template>
    <p>{{Logined}}</p>
    <p>{{UserId}}</p>
    <p>{{UserName}}</p>
</template>