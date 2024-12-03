import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import PADA from '../views/PADA.vue'
import PWD from '../views/PWD.vue'
import ManagerMain from '../views/manager/ManagerMain.vue'
import Register from '../views/manager/Register.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login,
  },
  {
    path: '/pada',
    name: 'PADA',
    component: PADA,
  },
  {
    path: '/pwd',
    name: 'PWD',
    component: PWD,
  },
  {
    path: '/manager',
    name: 'ManagerMain',
    component: ManagerMain,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
