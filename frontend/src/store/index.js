import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import PersonalityModule from './modules/PersonalityModule'
import AuthModule from './modules/AuthModule'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    PersonalityModule,
    AuthModule,
  },
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
    }),
  ],
})
