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
