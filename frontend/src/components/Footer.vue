<template>
  <footer class="footer">
    <div class="container">
	  <div class="level mx-6">
	    <div class="level-left">
	      <div class="level-item" tag="router-link" :to="{ path: '/home' }">
	        <img id="logo" src="img/logo/logo_only@2x.png" alt="Logo OpenPantheon" />
	      </div>
	    </div>
	    <div class="level-right">
	      <b-navbar-item
	        tag="router-link"
	        :to="{ path: '/home' }"
	        >{{ $t('topbar.pantheon') }}</b-navbar-item
	      >
	      <b-navbar-item v-if="!isLoggedIn" @click="cardModal">{{
            $t('topbar.login')
          }}</b-navbar-item>
	      <b-navbar-item v-else @click="cardModal">{{
            $t('topbar.logout')
          }}</b-navbar-item>
	      <b-navbar-item
	        tag="router-link"
	        :to="{ path: '/about' }"
	        >{{ $t('topbar.about') }}</b-navbar-item
	      >
	      <b-navbar-item
	        tag="router-link"
	        :to="{ path: '/faq' }"
	        >{{ $t('topbar.faq') }}</b-navbar-item
	      >
	      <b-navbar-item
	        tag="router-link"
	        :to="{ path: '/contact' }"
	        >{{ $t('topbar.contact') }}</b-navbar-item
	      >
	      <b-navbar-item
            tag="router-link"
            :to="{ path: '/celebrate' }"
            >{{
              $t('topbar.celebrate')
            }}</b-navbar-item
          >
	    </div>

	    <b-navbar-dropdown class="is-dark" :label="$t('topbar.currentLang')">
	      <b-navbar-item @click="changeLocale('en')">{{ $t('topbar.en') }}</b-navbar-item>
	      <b-navbar-item @click="changeLocale('fr')">{{ $t('topbar.fr') }}</b-navbar-item>
	    </b-navbar-dropdown>
  	  </div>
  	  <hr>
  	  <div class="is-flex is-justify-content-center my-6">
        <img src="img/icons/facebook@1,5x.svg" alt="Logo Facebook" />
        <img src="img/icons/twitter@1,5x.svg" alt="Logo Twitter" />
        <img src="img/icons/linkedin@1,5x.svg" alt="Logo Linkedin" />  	  	
  	  </div>
  	  <div class="my-6 is-flex is-justify-content-center is-align-content-space-around">
  	  	<p class="is-align-self-center mr-6">
  	  		<strong>CRI people - 2019</strong>
  	  		<br>
			made with ❤ in CRI by IT-Team
		</p>
		<img id="logo-cri" src="img/logo/madeincri.png" alt="Made in Cri" />
  	  </div>
  	  <a class="is-flex is-justify-content-center"><p>Terms and conditions</p></a>
    </div>
  </footer>
</template>

<script>
import AuthModal from '@/components/AuthModal'

export default {
  name: 'Footer',
  data() {
    return {
      currentLang: 'Français',
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isAuthenticated
    },
  },
  methods: {
    cardModal() {
      this.$buefy.modal.open({
        parent: this,
        component: AuthModal,
        hasModalCard: true,
        customClass: '',
        trapFocus: true,
      })
    },
    async logout() {
      await this.$store.dispatch('LogOut')
      this.$router.go()
    },
    changeLocale(lg) {
      localStorage.Lang = lg
      this.$router.go()
    },
  }
}
</script>

<style type="scss" scoped>
img {
	margin: 15px;
}
#logo {
	width: 200px;
}
#logo-cri {
	width: 75px;

}
</style>
