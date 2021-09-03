import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
// import Faq from "./views/Faq.vue"
import Contact from './views/Contact.vue'
import Details from './views/Details.vue'
import Celebrate from './views/Celebrate.vue'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        { path: '/', name: 'Home', component: Home },
        { path: '/about', name: 'About', component: About },
        // { path: '/faq', name:"Faq", component: Faq },
        { path: '/contact', name: 'Contact', component: Contact },
        // { path: '/account', name:"Account", component: Account },
        // { path: '/user-pantheon/:user', name:"UserPantheon", component: UserPantheon, props: true },
        { path: '/details/:id', name: 'Details', component: Details, props: true },
        { path: '/celebrate', name: 'Celebrate', component: Celebrate },
    ],
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) return savedPosition
        return { x: 0, y: 0 }
    },
})

export default router
