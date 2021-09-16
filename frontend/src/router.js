import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
// import Faq from "./views/Faq.vue"
import Contact from './views/Contact.vue'
import Details from './views/Details.vue'
import Pantheon from './views/Pantheon.vue'
import Celebrate from './views/Celebrate.vue'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    { path: '/home', name: 'Home', component: Home, alias: '/' },
    { path: '/about', name: 'About', component: About },
    // { path: '/faq', name:"Faq", component: Faq },
    { path: '/contact', name: 'Contact', component: Contact },
    // { path: '/account', name:"Account", component: Account },
    // { path: '/user-pantheon/:user', name:"UserPantheon", component: UserPantheon, props: true },
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

export default router
