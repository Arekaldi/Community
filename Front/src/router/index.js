import { createWebHashHistory, createRouter } from 'vue-router'

import HomeView from '../components/HomeView.vue'
import StudyView from '../components/StudyView.vue'
import SportView from '../components/SportView.vue'
import EntertainmentView from '../components/EntertainmentView.vue'
// import CommentView from '../components/CommentView.vue'
import PublishPostView from '../components/PublishPostView.vue'
import LoginView from '../components/LoginView.vue'
import RegisterView from '../components/RegisterView.vue'
import PostDetail from '@/components/PostDetail.vue'

const routes = [
  { name: "Home", path: '/', component: HomeView },
  { name: "Study", path: '/study', component: StudyView },
  { name: "Sport", path: '/sport', component: SportView },
  { name: "Entertainment", path: '/entertainment', component: EntertainmentView },
  // { name: "Comment",  path: '/comment', component: CommentView },
  { name: "PublishPost", path: '/publishpost', component: PublishPostView },
  { name: "Login", path: '/login', component: LoginView },
  { name: "Register", path: '/register', component: RegisterView },
  { name: "PostDetail", path: '/post/:id', component: PostDetail },
]
  
const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router