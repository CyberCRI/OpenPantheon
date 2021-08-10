<template>
    <b-navbar spaced transparent>
        <template #brand>
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <img src="../assets/Logo@2x.png" alt="Logo OpenPantheon" />
            </b-navbar-item>
        </template>
        <template #start>
            <b-navbar-item tag="router-link" active-class="is-active" :to="{ path: '/' }"
                >The Pantheon</b-navbar-item
            >
            <b-navbar-item tag="router-link" active-class="is-active" :to="{ path: '/about' }"
                >About</b-navbar-item
            >
            <b-navbar-item tag="router-link" active-class="is-active" :to="{ path: '/faq' }"
                >FAQ</b-navbar-item
            >
            <b-navbar-item tag="router-link" active-class="is-active" :to="{ path: '/contact' }"
                >Contact</b-navbar-item
            >
        </template>

        <template #end>
            <b-navbar-item tag="div">
                <div class="buttons">
                    <b-navbar-item
                        tag="router-link"
                        :to="{ path: '/celebrate' }"
                        class="button is-medium has-text-small is-primary is-mobile"
                        ><strong class="is-size-6">Celebrate someone</strong></b-navbar-item
                    >
                    <b-navbar-dropdown label="English">
                        <b-navbar-item href="#">English</b-navbar-item>
                        <b-navbar-item href="#">French</b-navbar-item>
                    </b-navbar-dropdown>
                    <b-navbar-item @click="cardModal">Login</b-navbar-item>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>

import Login from '@/components/Login'

export default {
	methods: {
	    cardModal() {
		    this.$buefy.modal.open({
		        parent: this,
		        component: Login,
		        hasModalCard: true,
		        customClass: '',
		        trapFocus: true
		    })
		}
	}
}
</script>

<style type="scss" scoped>
.navbar {
    background-color: transparent;
}
</style>
