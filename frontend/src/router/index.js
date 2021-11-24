import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import newLog from '../../views/newLogin'
import profile from '../../views/Profile'
import userProfile from '../../views/UserProfile'
import articlelist from '../../views/articlelist'
import articleDetails from "../../views/articleDetails";
import createArticle from '../../views/createArticle'
import about from '../../views/about'
import message from '../../views/message'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {path: '/', redirect: '/?#'},
    {
      path: '/?#',
      name: 'newLog',
      component: newLog
    },
    {
      path: '/profile/:user_id/:user_name',
      name: 'profile',
      props: true,
      component: profile,
      children: [
          {
            path: '/profile/userProfile/:user_id/:user_name',
            name: 'userProfile',
            props: true,
            component: userProfile
          },
          {
            path: '/profile/articlelist/:user_id/:user_name',
            name: 'articlelist',
            props:true,
            component: articlelist
          },
        {
      path: '/profile/articleDetails/:article_id/:user_id',
      name: 'articleDetails',
      props: true,
      component: articleDetails
    },
        {
            path: '/profile/createArticle/:user_id/:user_name',
            name: 'createArticle',
            props: true,
            component: createArticle
          },
        {
          path: '/profile/about/:user_id/:user_name',
            name: 'about',
          props:true,
            component: about
        },
        {
          path: '/profile/message/:user_id/:user_name',
            name: 'message',
          props:true,
            component: message
        }
      ]
    }
  ]
})
