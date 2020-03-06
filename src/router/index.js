import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Jails from '@/components/Jails'
import Jail from '@/components/Jail'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/jails',
      name: 'Jails',
      component: Jails
    },
    {
      path: '/jail/:jailname',
      name: 'Jail',
      component: Jail
    }
  ]
})
