import axios from 'axios'

// Function below forces logout in case JWT has expired for any reason

axios.interceptors.response.use(undefined, function (error) {
  return error.response.status === 401 ? this.store.dispatch('LogOut') : ''
})

export default {
  getCurrentUserDetails() {
    return axios.get('/users/me')
  },
  getUserById(id) {
    return axios.get('/users/' + id)
  },
  updateUser(user) {
    return axios.put('/users/me', user)
  },
  updateUserPantheon(id) {
    return axios.post('/users/me/pantheon/' + id)
  },
  createUser(user) {
    return axios.post('users/open', user)
  },
  deleteUser() {
    return axios.delete('users/me')
  },
  getToken(credentials) {
    return axios.post('login/access-token', credentials)
  },
}
