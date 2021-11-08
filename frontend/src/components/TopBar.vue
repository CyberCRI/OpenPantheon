<!--
OpenPantheon: the pantheon for Education
Copyright (C) 2021 CRI

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
  <b-navbar spaced shadow>
    <template #brand>
      <b-navbar-item class="mr-6" tag="router-link" :to="{ path: '/home' }">
        <img src="img/logo/logo@2x-compressed.png" alt="Logo OpenPantheon" />
      </b-navbar-item>
    </template>
    <template #start>
      <b-navbar-item
        tag="router-link"
        class="is-tab is-expanded"
        active-class="is-active"
        :to="{ path: '/home' }"
        >{{ $t('topbar.pantheon') }}</b-navbar-item
      >
      <b-navbar-item
        tag="router-link"
        class="is-tab is-expanded"
        active-class="is-active"
        :to="{ path: '/about' }"
        >{{ $t('topbar.about') }}</b-navbar-item
      >
      <b-navbar-item
        tag="router-link"
        class="is-tab is-expanded"
        active-class="is-active"
        :to="{ path: '/faq' }"
        >{{ $t('topbar.faq') }}</b-navbar-item
      >
      <b-navbar-item
        tag="router-link"
        class="is-tab is-expanded"
        active-class="is-active"
        :to="{ path: '/contact' }"
        >{{ $t('topbar.contact') }}</b-navbar-item
      >
    </template>

    <template #end>
      <b-navbar-item tag="div">
        <div class="buttons">
          <router-link
            :to="{ path: '/celebrate' }"
            class="button is-medium has-text-small is-primary is-mobile"
            active-class=""
            ><strong class="is-size-6 has-text-black">{{
              $t('topbar.celebrate')
            }}</strong></router-link
          >
          <b-navbar-dropdown class="is-dark" :label="$t('topbar.currentLang')">
            <b-navbar-item @click="changeLocale('en')">{{ $t('topbar.en') }}</b-navbar-item>
            <b-navbar-item @click="changeLocale('fr')">{{ $t('topbar.fr') }}</b-navbar-item>
          </b-navbar-dropdown>
          <b-navbar-item v-if="!isLoggedIn" @click="cardModal">{{
            $t('topbar.login')
          }}</b-navbar-item>
          <b-navbar-item v-else @click="logout">{{ $t('topbar.logout') }}</b-navbar-item>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import AuthModal from '@/components/AuthModal.vue'

export default {
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

<style type="scss" scoped></style>
