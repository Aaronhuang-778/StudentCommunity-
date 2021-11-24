import request from './request'

export default {
  register(data) {  //注册
    return request({
      url: 'http://localhost:8000/api/register',
      method: 'post',
      data
    })
  },
  signin(data) {
    return request({
      url: 'http://localhost:8000/api/signin',
      method: 'post',
      data
    })
  },
  getPost(data) {
    return request({
      url: 'http://localhost:8000/api/getPost',
      method: 'post',
      data
    })
  }
}
