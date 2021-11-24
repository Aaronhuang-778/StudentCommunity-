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
  getPost(data) {  // # 根据post_id得到post，结合user_id得到是否点赞和踩,-1表示没有
    return request({
      url: 'http://localhost:8000/api/getPost',
      method: 'post',
      data
    })
  },
  publishPost(data) {  // # 根据post_id得到post，结合user_id得到是否点赞和踩,-1表示没有
    return request({
      url: 'http://localhost:8000/api/publishPost',
      method: 'post',
      data
    })
  }
}
