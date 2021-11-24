import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import LogReg from '../../views/login_register'
import newLog from '../../views/newLogin'
import nop from '../../views/nop'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    // {
    //   path: '/',
    //   name: 'LogReg',
    //   component: LogReg
    // },
    {path: '/', redirect: '/?#'},
    {
      path: '/?#',
      name: 'newLog',
      component: newLog
    },
    {
      path: '/nop',
      name:'nop',
      component: nop
    }
  ]
})
