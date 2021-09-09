import axios from 'axios'

export default {
  getPantheonStats() {
    return axios.get('/personalities/stats')
  },
  getAll(loggedIn, skip, limit, personal, women, field, sort) {
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
          '&sort=' +
          sort
      )
    else
      return axios.get(
        '/personalities/guest/?skip=' +
          skip +
          '&limit=' +
          limit +
          '&women=' +
          women +
          '&field=' +
          field +
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
    return axios.post('/personalities', personality)
  },
  postComment(input) {
    return axios.post('/comments', input)
  },
}
