<template>
  <b-navbar spaced shadow>
    <template #brand>
      <b-navbar-item class="mr-6" tag="router-link" :to="{ path: '/home' }">
        <img src="img/logo/logo@2x.png" alt="Logo OpenPantheon" />
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
          <b-navbar-item
            tag="router-link"
            :to="{ path: '/celebrate' }"
            class="button is-medium has-text-small is-primary is-mobile"
            active-class=""
            ><strong class="is-size-6 has-text-black">{{
              $t('topbar.celebrate')
            }}</strong></b-navbar-item
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
