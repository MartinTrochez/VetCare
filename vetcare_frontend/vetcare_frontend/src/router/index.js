import { createRouter, createWebHistory } from 'vue-router'
import LoginView from "@/views/LoginView.vue";
import HitorialMascoteroView from "@/views/HitorialMascoteroView.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: LoginView
    },
    {
      path: '/historial-mascotero',
      name: 'HistorialMascotero',
      component: HitorialMascoteroView,
      beforeEnter: (_to, _from, next) => {
        const token = localStorage.getItem('token');
        if (token) {
          next();
        } else {
          next('/');
        }
      },
    }
  ]
})

export default router
