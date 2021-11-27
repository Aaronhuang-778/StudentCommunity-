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
import myarticles from '../../views/MyArticles'

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
      path: '/profile/:user_id/:user_name/:picture',
      name: 'profile',
      props: true,
      component: profile,
      children: [
          {
            path: '/profile/userProfile/:user_id/:other_id',
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
          path: '/profile/articleDetails/:article_id/:user_id/:user_name',
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
          path: '/profile/myarticles/:user_id/:user_name',
            name: 'myarticles',
          props:true,
            component: myarticles
        },
        {
        path: '/profile/about/:user_id/:user_name',
            name: 'about',
          props:true,
            component: about
        }
        //,
        // {
        //   path: '/profile/message/:user_id/:user_name',
        //     name: 'message',
        //   props:true,
        //     component: message
        // }
      ]
    }
  ]
})
