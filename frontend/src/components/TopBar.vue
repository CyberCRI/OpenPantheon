<template>
  <b-navbar spaced transparent>
    <template #brand>
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <img src="../assets/Logo@2x.png" alt="Logo OpenPantheon" />
      </b-navbar-item>
    </template>
    <template #start>
      <b-navbar-item tag="router-link" active-class="is-active" :to="{ path: '/' }">{{
        $t('topbar.pantheon')
      }}</b-navbar-item>
      <b-navbar-item tag="router-link" active-class="is-active" :to="{ path: '/about' }">{{
        $t('topbar.about')
      }}</b-navbar-item>
      <b-navbar-item tag="router-link" active-class="is-active" :to="{ path: '/faq' }">{{
        $t('topbar.faq')
      }}</b-navbar-item>
      <b-navbar-item tag="router-link" active-class="is-active" :to="{ path: '/contact' }">{{
        $t('topbar.contact')
      }}</b-navbar-item>
    </template>

    <template #end>
      <b-navbar-item tag="div">
        <div class="buttons">
          <b-navbar-item
            tag="router-link"
            :to="{ path: '/celebrate' }"
            class="button is-medium has-text-small is-primary is-mobile"
            ><strong class="is-size-6">{{ $t('topbar.celebrate') }}</strong></b-navbar-item
          >
          <b-navbar-dropdown :label="$t('topbar.currentLang')">
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

<style type="scss" scoped>
.navbar {
  background-color: transparent;
}
</style>
