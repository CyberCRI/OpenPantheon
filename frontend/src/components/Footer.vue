<!--
OpenPantheon: the pantheon for Education
Copyright (C) 2022 Learning Planet Institute

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
-->
<template>
  <footer class="footer">
    <div class="container">
      <div class="level mx-6">
        <div class="level-left">
          <div class="level-item" tag="router-link" :to="{ path: '/home' }">
            <img id="logo" src="img/logo/logo_only@2x-compressed.png" alt="Logo OpenPantheon" />
          </div>
        </div>
        <div class="level-right">
          <b-navbar-item tag="router-link" :to="{ path: '/home' }">{{
            $t('footer.pantheon')
          }}</b-navbar-item>
          <b-navbar-item v-if="!isLoggedIn" @click="cardModal">{{
            $t('footer.login')
          }}</b-navbar-item>
          <b-navbar-item v-else @click="cardModal">{{ $t('footer.logout') }}</b-navbar-item>
          <b-navbar-item tag="router-link" :to="{ path: '/about' }">{{
            $t('footer.about')
          }}</b-navbar-item>
          <b-navbar-item tag="router-link" :to="{ path: '/faq' }">{{
            $t('footer.faq')
          }}</b-navbar-item>
          <b-navbar-item tag="router-link" :to="{ path: '/contact' }">{{
            $t('footer.contact')
          }}</b-navbar-item>
          <b-navbar-item tag="router-link" :to="{ path: '/celebrate' }">{{
            $t('footer.celebrate')
          }}</b-navbar-item>
        </div>

        <b-navbar-dropdown class="is-dark" :label="$t('footer.currentLang')">
          <b-navbar-item @click="changeLocale('en')">{{ $t('footer.en') }}</b-navbar-item>
          <b-navbar-item @click="changeLocale('fr')">{{ $t('footer.fr') }}</b-navbar-item>
        </b-navbar-dropdown>
      </div>
      <hr />
      <!--       <div class="is-flex is-justify-content-center my-6">
        <img src="img/icons/facebook@1,5x.svg" alt="Logo Facebook" />
        <img src="img/icons/twitter@1,5x.svg" alt="Logo Twitter" />
        <img src="img/icons/linkedin@1,5x.svg" alt="Logo Linkedin" />
      </div> -->
      <div class="my-6 is-flex is-justify-content-center is-align-content-space-around">
        <p class="is-align-self-center mr-6 has-text-grey-lighter">
          {{ $t('footer.madeInCRI') }}
          <br />
          <a href="https://github.com/CyberCRI/OpenPantheon">{{ $t('footer.sourceCode') }}</a>
        </p>
        <img id="logo-cri" src="img/logo/madeincri.png" alt="Made in Cri" />
      </div>
      <a class="is-flex is-justify-content-center" href="/documents/OpenPantheon CGU VF.pdf"
        ><p>{{ $t('footer.terms') }}</p></a
      >
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
  },
}
</script>

<style lang="scss" scoped>
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
