import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import('./assets/components/AppPreviu.vue'),
    },
    {
      path: '/test',
      component: () => import('./assets/components/AppScroll.vue'),
    },
    {
      path: '/test1',
      component: () => import('./assets/components/SlotAplic2.vue'),
    },
    {
      path: '/button',
      component: () => import('./assets/components/AppButton.vue'),
    }
  ]
})
