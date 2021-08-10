import axios from 'axios'

const apiClient = axios.create({
    baseURL: `http://localhost:3000`,
    withCredentials: false, // This is the default
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
    },
})

export default {
    getAll(perPage, page) {
        return apiClient.get('/personalities?_limit=' + perPage + '&_page=' + page)
    },
    getById(id) {
        return apiClient.get('/personalities/' + id)
    },
    postPersonality(personality) {
        return apiClient.post('/personalities', personality)
    },
    // postComment(personality) {
    //   return apiClient.post('/personalities', personality)
    // },
}
