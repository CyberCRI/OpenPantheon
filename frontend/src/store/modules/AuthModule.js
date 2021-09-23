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
import AuthService from '@/services/AuthService'

const state = {
  currentUserDetails: null,
  token: null,
  userDetails: null,
}

const getters = {
  isAuthenticated: (state) => !!state.currentUserDetails,
  accessToken: (state) => state.token,
  listPersonalitiesCelebrated: (state) =>
    state.currentUserDetails.personalities_celebrated.map(
      (personality) => personality.wikipedia_id
    ),
  // userById: (state) => (id) => {
  //     return state.users.find((user) => user.id === id)
  // },
  idUser: (state) => state.currentUserDetails.id,
}

const actions = {
  // eslint-disable-next-line
  async Register({ dispatch }, user) {
    await AuthService.createUser(user)
  },
  // eslint-disable-next-line
  addToPantheon({ commit }, personality_id) {
    return AuthService.updateUserPantheon(personality_id)
  },
  LogIn({ commit }, user) {
    const params = new URLSearchParams()
    params.append('username', user.email)
    params.append('password', user.password)
    return AuthService.getToken(params).then((response) => {
      commit('SET_TOKEN', response.data.access_token)
    })
  },
  getCurrentUserDetails({ commit }) {
    return AuthService.getCurrentUserDetails().then((response) => {
      commit('SET_CURRENT_USER_DETAILS', response.data)
    })
  },
  getUserById({ commit }, id) {
    return AuthService.getUserById(id).then((response) => {
      commit('SET_USER_DETAILS', response.data)
    })
  },
  // eslint-disable-next-line
  deleteComment({ commit }, id) {
    return AuthService.deleteComment(id)
  },
  LogOut({ commit }) {
    commit('SET_CURRENT_USER_DETAILS', null)
    commit('SET_TOKEN', null)
    sessionStorage.clear()
  },
}

const mutations = {
  SET_CURRENT_USER_DETAILS(state, user) {
    state.currentUserDetails = user
  },
  SET_USER_DETAILS(state, user) {
    state.userDetails = user
  },
  SET_TOKEN(state, token) {
    state.token = token
  },
  UPDATE_PERSONAL_PANTHEON(state, data) {
    state.currentUserDetails.personalities_celebrated.push(data)
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
