import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
import router from './router'
import store from './store'
import i18n from './i18n'
import axios from 'axios'
import Vue2Filters from 'vue2-filters'

Vue.use(Vue2Filters)

const token = store.getters.accessToken

axios.defaults.withCredentials = false
axios.defaults.baseURL = `${process.env.VUE_APP_BACKEND_URL}/api/v1`
axios.defaults.headers.common['Authorization'] = token ? `Bearer ${token}` : undefined

Vue.config.productionTip = false
Vue.use(Buefy)

new Vue({
  router,
  store,
  i18n,
  render: (h) => h(App),
}).$mount('#app')
