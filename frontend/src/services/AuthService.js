/*
 * OpenPantheon: the pantheon for Education
 * Copyright (C) 2021 CRI
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
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
    return axios.put('/users/me/', user)
  },
  updateUserPantheon(id) {
    return axios.post('/users/me/pantheon/' + id)
  },
  createUser(user) {
    return axios.post('/users/open', user)
  },
  deleteUser() {
    return axios.delete('/users/me/')
  },
  deleteComment(id) {
    return axios.delete('/comments/' + id)
  },
  getToken(credentials) {
    return axios.post('/login/access-token', credentials)
  },
  sendMail(content) {
    return axios.post('/utils/contact', content)
  },
}
