/*
 * OpenPantheon: the pantheon for Education
 * Copyright (C) 2022 Learning Planet Institute
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
import PersonalityService from '@/services/PersonalityService'

export default {
  state: {
    personalities: null,
    total: 0,
    personality: {},
    pantheonCount: 0,
    pantheonParity: 0,
  },
  mutations: {
    ADD_PERSONALITY(state, personality) {
      state.personalities.push(personality)
    },
    SET_PERSONALITIES(state, personalities) {
      state.personalities = personalities
    },
    SET_TOTAL(state, total) {
      state.total = total
    },
    SET_PANTHEON_COUNT(state, count) {
      state.pantheonCount = count
    },
    SET_PANTHEON_PARITY(state, percent) {
      state.pantheonParity = percent
    },
    SET_PERSONALITY(state, personality) {
      state.personality = personality
    },
  },
  actions: {
    getPantheonStats({ commit }) {
      return PersonalityService.getPantheonStats().then((response) => {
        commit('SET_PANTHEON_COUNT', response.data.count)
        commit('SET_PANTHEON_PARITY', response.data.parity)
      })
    },
    createPersonality({ commit }, personality) {
      return PersonalityService.postPersonality(personality).then((response) => {
        commit('ADD_PERSONALITY', response.data)
      })
    },
    // eslint-disable-next-line
    createComment({ commit }, input) {
      return PersonalityService.postComment(input)
    },
    fetchAll({ commit }, { loggedIn, skip, limit, personal, women, field, sort, region }) {
      return PersonalityService.getAll(
        loggedIn,
        skip,
        limit,
        personal,
        women,
        field,
        sort,
        region
      ).then((response) => {
        commit('SET_TOTAL', Number(response.headers['x-total-count']))
        commit('SET_PERSONALITIES', response.data)
        return response.data
      })
    },
    fetchPersonality({ commit }, id) {
      return PersonalityService.getById(id)
        .then((response) => {
          commit('SET_PERSONALITY', response.data)
          return response.data
        })
        .catch(() => {
          this.$buefy.toast.open({
            duration: 5000,
            message: this.$t('toast.unknown'),
            type: 'is-danger',
          })
        })
    },
    fetchPersonalityByWiki({ commit }, id) {
      return PersonalityService.getByWikiId(id)
        .then((response) => {
          commit('SET_PERSONALITY', response.data)
          return response.data
        })
        .catch(() => {
          this.$buefy.toast.open({
            duration: 5000,
            message: this.$t('toast.unknown'),
            type: 'is-danger',
          })
        })
    },
  },
  getters: {
    personalityByWikiId: (state) => (wikipedia_id) => {
      return state.personalities.find((personality) => personality.wikipedia_id === wikipedia_id)
    },
    personalityById: (state) => (id) => {
      return state.personalities.find((personality) => personality.id === id)
    },
    personality: (state) => {
      return state.personality
    },
    pantheonCount: (state) => {
      return state.pantheonCount
    },
    pantheonParity: (state) => {
      return state.pantheonParity
    },
  },
}
