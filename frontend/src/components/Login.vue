<template>
  <form @submit.prevent="onSubmit">
    <section class="modal-card-body px-6 py-6">
      <b-field label="Email" label-position="inside">
        <b-input type="email" v-model="user.email" placeholder="Your email" required expanded>
        </b-input>
      </b-field>

      <b-field label="Password" label-position="inside">
        <b-input type="password" v-model="user.password" password-reveal required expanded>
        </b-input>
      </b-field>

      <b-input type="submit" value="Login" custom-class="button is-primary"></b-input>
      <p class="block">
        {{ $t('login.no_account') }}
        <a @click="$emit('switchView')">{{ $t('login.create_one') }}</a>
      </p>
    </section>
  </form>
</template>

<script>
import { mapActions } from 'vuex'
import axios from 'axios'

export default {
  name: 'Login',
  data() {
    return {
      user: {
        email: null,
        password: null,
      },
    }
  },
  methods: {
    ...mapActions(['LogIn', 'getCurrentUserDetails']),
    async onSubmit() {
      try {
        await this.LogIn(this.user)
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.$store.getters.accessToken}`
        await this.getCurrentUserDetails()
        if (this.$store.getters.accessToken) {
	        this.$emit('close')
	        if (this.$router.currentRoute.name !== 'Celebrate') this.$router.go()
	    }
		else
			throw new Error('Invalid Credentials')
      } catch (error) {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Invalid credentials',
          type: 'is-danger',
        })
      }
    },
  },
}
</script>
