import request from './request'

export default {
  register(data) {  //注册
    return request({
      url: 'http://localhost:8000/api/register',
      method: 'post',
      data
    })
  },
  signin(data) {   //登录
    return request({
      url: 'http://localhost:8000/api/signin',
      method: 'post',
      data
    })
  },
  getPostList() {  //得到所有post
    return request({
      url: 'http://localhost:8000/api/getPostList',
      method: 'get'
    })
  },
  getKeywordList() {  //得到所有keyword
    return request({
      url: 'http://localhost:8000/api/getKeywordList',
      method: 'get'
    })
  },
  getPost(data) {  //根据post_id得到post，结合user_id得到是否点赞和踩,-1表示没有
    return request({
      url: 'http://localhost:8000/api/getPost',
      method: 'post',
      data
    })
  },
  publishPost(data) {  //根据post_id得到post，结合user_id得到是否点赞和踩,-1表示没有
    return request({
      url: 'http://localhost:8000/api/publishPost',
      method: 'post',
      data
    })
  },
  message(data) {  //留言
    return request({
      url: 'http://localhost:8000/api/message',
      method: 'post',
      data
    })
  },
  cancelmessage(data) {  //删除留言 message_id
    return request({
      url: 'http://localhost:8000/api/cancelmessage',
      method: 'get',
      params:{
        data
      }
    })
  },
  comment(data) {  //评论
    return request({
      url: 'http://localhost:8000/api/comment',
      method: 'post',
      data
    })
  },
  cancelcomment(data) {  //取消评论 comment_id
    return request({
      url: 'http://localhost:8000/api/cancelcomment',
      method: 'get',
      params:{
        data
      }
    })
  },
  delPost(data) {  //删除帖子 post_id
    return request({
      url: 'http://localhost:8000/api/delPost',
      method: 'get',
      params:{
        data
      }
    })
  },
  like(data) {  //点赞 post_id, user_id
    return request({
      url: 'http://localhost:8000/api/like',
      method: 'post',
      data
    })
  },
  cancellike(data) {  //取消点赞 like_id
    return request({
      url: 'http://localhost:8000/api/cancellike',
      method: 'post',
      data
    })
  },
  unlike(data) {  //踩 post_id, user_id
    return request({
      url: 'http://localhost:8000/api/unlike',
      method: 'post',
      data
    })
  },
  cancelunlike(data) {  //取消踩 unlike_id
    return request({
      url: 'http://localhost:8000/api/cancelunlike',
      method: 'post',
      data
    })
  },
  follow(data) {  //关注 follow_id, star_id
    return request({
      url: 'http://localhost:8000/api/follow',
      method: 'post',
      data
    })
  },
  cancelfollow(data) {  //取消关注 follow_star_id
    return request({
      url: 'http://localhost:8000/api/cancelfollow',
      method: 'post',
      data
    })
  },
  getUser(data) {  //根据user_id得到user详情 user_id
    return request({
      url: 'http://localhost:8000/api/getUser',
      method: 'post',
      data
    })
  },
  getMyPostList(data) {  //得到user_id得到其post user_id
    return request({
      url: 'http://localhost:8000/api/getMyPostList',
      method: 'post',
      params:{
        data
      }
    })
  },
  search(data) {
    return request({
      url: 'http://localhost:8000/api/search',
      method: 'post',
      data
    })
  },
  checkLogin(data) {
    return request({
      url: 'http://localhost:8000/api/checkLogin',
      method: 'get',
      data
    })
  },
  loginout() {
    return request({
      url: 'http://localhost:8000/api/loginout',
      method: 'get'
    })
  }
}
