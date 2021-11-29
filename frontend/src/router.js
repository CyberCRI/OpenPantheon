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
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Faq from './views/Faq.vue'
import Contact from './views/Contact.vue'
import Details from './views/Details.vue'
import Pantheon from './views/Pantheon.vue'
import Celebrate from './views/Celebrate.vue'
import { pageViewed } from './analytics'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    { path: '/home', name: 'Home', component: Home, alias: '/' },
    { path: '/about', name: 'About', component: About },
    { path: '/faq', name: 'Faq', component: Faq },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact,
      props: (route) => ({ report: route.query.q }),
    },
    { path: '/details/:id', name: 'Details', component: Details, props: true },
    { path: '/pantheon/:user', name: 'Pantheon', component: Pantheon, props: true },
    {
      path: '/celebrate',
      name: 'Celebrate',
      component: Celebrate,
      props: (route) => ({ personalityProp: route.query.q, nameProp: route.query.n }),
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    return { x: 0, y: 0 }
  },
})

router.afterEach((to) => {
  pageViewed({
    name: to.name,
    url: window.location.href,
  })
})

export default router
