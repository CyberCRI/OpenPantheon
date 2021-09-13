import PersonalityService from '@/services/PersonalityService'

export default {
    state: {
        personalities: null,
        total: 0,
        personality: {},
        pantheonCount: 0,
        pantheonParity: 0
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
        createComment({ commit }, input) {
            return PersonalityService.postComment(input)
        },
        fetchAll({ commit }, { loggedIn, skip, limit, personal, women, field, sort, region }) {
            return PersonalityService.getAll(loggedIn, skip, limit, personal, women, field, sort, region)
                .then((response) => {
                    commit('SET_TOTAL', Number(response.headers['x-total-count']))
                    commit('SET_PERSONALITIES', response.data)
                    return response.data
                })
                .catch((error) => {
                    console.log('There was an error:', error.response)
                })
        },
        fetchPersonality({ commit, getters }, id) {
            return PersonalityService.getById(id)
                .then((response) => {
                    commit('SET_PERSONALITY', response.data)
                    return response.data
                })
                .catch((error) => {
                    this.$buefy.toast.open({
                        duration: 5000,
            			message: this.$t('toast.unknown'),
                        type: 'is-danger',
                    })
                    console.log('There was an error:', error.response)
                })
        },
        fetchPersonalityByWiki({ commit, getters }, id) {
            return PersonalityService.getByWikiId(id)
                .then((response) => {
                    commit('SET_PERSONALITY', response.data)
                    return response.data
                })
                .catch((error) => {
                    this.$buefy.toast.open({
                        duration: 5000,
            			message: this.$t('toast.unknown'),
                        type: 'is-danger',
                    })
                    console.log('There was an error:', error.response)
                })
        }
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
