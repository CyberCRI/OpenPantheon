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
  <section class="modal-card-body px-6 py-6">
    <form v-show="!contactProvided" @submit.prevent="contactProvided = true">
      <b-field :label="$t('login.email')" label-position="inside">
        <b-input
          type="email"
          v-model="user.email"
          :placeholder="$t('login.your_email')"
          required
          expanded
        />
      </b-field>

      <b-field :label="$t('login.password')" label-position="inside">
        <b-input type="password" v-model="user.password" password-reveal required expanded>
        </b-input>
      </b-field>
      <b-input
        type="submit"
        :value="$t('register.signup')"
        custom-class="button is-primary"
        expanded
      ></b-input>
      <p class="block mt-4">
        {{ $t('register.already') }}<a @click="$emit('switchView')">{{ $t('register.login') }}</a
        >*
      </p>
    </form>
    <form v-show="contactProvided" @submit.prevent="captchaCheck">
      <p class="title">{{ $t('register.welcome') }}</p>
      <p class="is-size-6 has-text-weight-semibold">
        {{ $t('register.welcome_text') }}
      </p>
      <b-field class="mt-5" :label="$t('register.first_name')" label-position="inside">
        <b-input v-model="user.firstname" placeholder="John" required expanded />
      </b-field>

      <b-field :label="$t('register.last_name')" label-position="inside">
        <b-input v-model="user.lastname" placeholder="Doe" required expanded> </b-input>
      </b-field>

      <b-field :label="$t('register.job')" label-position="inside">
        <b-input v-model="user.job" expanded> </b-input>
      </b-field>

      <b-field :label="$t('register.organization')" label-position="inside">
        <b-input v-model="user.organization" expanded> </b-input>
      </b-field>
      <b-input
        type="submit"
        :value="$t('register.create')"
        custom-class="button is-primary"
        expanded
      ></b-input>
    </form>
  </section>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'

export default {
  name: 'Register',
  data() {
    return {
      contactProvided: false,
      user: {
        email: null,
        password: null,
        firstname: null,
        lastname: null,
        job: null,
        organization: null,
      },
    }
  },
  methods: {
    ...mapActions(['Register', 'LogIn', 'getCurrentUserDetails']),
    async captchaCheck() {
      // eslint-disable-next-line no-unused-vars
      let captchaToken = await new Promise((res, rej) => {
        grecaptcha.ready(function () {
          return grecaptcha
            .execute('6LcNBh4eAAAAAFMGAr6PiXoQBoAOdAr_eJGiajGI', { action: 'submit' })
            .then((token) => {
              return res(token)
            })
        })
      })
      if (captchaToken) this.onSubmit(captchaToken)
      else
        this.$buefy.toast.open({
          duration: 5000,
          message: this.$t('toast.credentials'),
          type: 'is-danger',
        })
    },
    async onSubmit(token) {
      try {
        axios.defaults.headers.common['captcha'] = token
        await this.Register(this.user)
        try {
          await this.LogIn(this.user)
          axios.defaults.headers.common[
            'Authorization'
          ] = `Bearer ${this.$store.getters.accessToken}`
          await this.getCurrentUserDetails()
          this.$emit('close')
          if (this.$router.currentRoute.name !== 'Celebrate') this.$router.go()
        } catch (error) {
          this.$buefy.toast.open({
            duration: 5000,
            message: this.$t('toast.credentials'),
            type: 'is-danger',
          })
        }
      } catch (error) {
        this.$buefy.toast.open({
          duration: 5000,
          message: this.$t('toast.email'),
          type: 'is-danger',
        })
      }
      this.$emit('close')
    },
  },
}
</script>
