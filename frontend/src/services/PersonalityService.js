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

export default {
  getPantheonStats() {
    return axios.get('/personalities/stats')
  },
  getAll(loggedIn, skip, limit, personal, women, field, sort, region) {
    if (loggedIn)
      return axios.get(
        '/personalities/?skip=' +
          skip +
          '&limit=' +
          limit +
          '&personal=' +
          personal +
          '&women=' +
          women +
          '&field=' +
          field +
          '&region=' +
          region +
          '&sort=' +
          sort
      )
    else
      return axios.get(
        '/personalities/guest?skip=' +
          skip +
          '&limit=' +
          limit +
          '&women=' +
          women +
          '&field=' +
          field +
          '&region=' +
          region +
          '&sort=' +
          sort
      )
  },
  getById(id) {
    return axios.get('/personalities/' + id)
  },
  getByWikiId(id) {
    return axios.get('/personalities/wiki/' + id)
  },
  postPersonality(personality) {
    return axios.post('/personalities/', personality)
  },
  postComment(input) {
    return axios.post('/comments/', input)
  },
}
