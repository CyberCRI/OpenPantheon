import AuthService from '@/services/AuthService'

const state = {
    currentUserDetails: null,
    token: null,
    userDetails: null
}

const getters = {
    isAuthenticated: (state) => !!state.currentUserDetails,
    accessToken: (state) => state.token,
    // userById: (state) => (id) => {
    //     return state.users.find((user) => user.id === id)
    // },
    idUser: (state) => state.currentUserDetails.id,
}

const actions = {
    async Register({ dispatch }, user) {
        await AuthService.createUser(user)
    },
    // async Update({ commit }, user) {
    //     await AuthService.updateUser(user)
    // },
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
        .catch((error) => {
            console.log('There was an error:', error.response)
        })
    },
    getCurrentUserDetails({ commit }) {
	    return AuthService.getCurrentUserDetails().then((response) => {
	    	console.log(response)
        	commit('SET_CURRENT_USER_DETAILS', response.data)
        })
        .catch((error) => {
            console.log('There was an error:', error)
        })
    },
    getUserById({ commit }, id) {
    return AuthService.getUserById(id).then((response) => {
    	console.log(response)
    	commit('SET_USER_DETAILS', response.data)
    })
    .catch((error) => {
        console.log('There was an error:', error)
    })
    },
    // async getUsers({ commit }) {
    //     await axios.get('users').then(async (response) => {
    //         await commit('SET_USERS', response.data)
    //     })
    // },
    async LogOut({ commit }) {
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
    }
}

export default {
    state,
    getters,
    actions,
    mutations,
}
