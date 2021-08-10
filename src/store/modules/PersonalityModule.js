import PersonalityService from '@/services/PersonalityService'

export default {
    state: {
        personalities: null,
        total: 0,
        personality: {}
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
        SET_PERSONALITY(state, personality) {
        	state.personality = personality
        }
    },
    actions: {
        createPersonality({ commit }, personality) {
            return PersonalityService.postPersonality(personality).then(() => {
                commit('ADD_PERSONALITY', personality)
            })
        },
        fetchAll({ commit }, { perPage, page }) {
            PersonalityService.getAll(perPage, page)
                .then((response) => {
                	commit('SET_TOTAL', response.headers['x-total-count'])
                    commit('SET_PERSONALITIES', response.data)
                })
                .catch((error) => {
                	this.$buefy.toast.open({
                        duration: 5000,
                        message: "Sorry, please try again later",
                        type: 'is-danger',
                    })
                    console.log('There was an error:', error.response)
                })
        },
        fetchPersonality({ commit, getters }, id) {
        	const personality = getters.searchById(id)
        	if (personality)
        		commit('SET_PERSONALITY', personality)
        	else {
	        	PersonalityService.getById(id)
	        		.then((response) => {
	        			commit('SET_PERSONALITY', response.data)
	        		})
	        		.catch((error) => {
	                	this.$buefy.toast.open({
	                        duration: 5000,
	                        message: "Sorry, please try again later",
	                        type: 'is-danger',
	                    })
	        			console.log("There was an error:", error.response)
	        		})
	        }
        }
    },
    getters: {
        searchById: (state) => (id) => {
            return state.personalities.find((personality) => personality.id === id)
        },
    }
}