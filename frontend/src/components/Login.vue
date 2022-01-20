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
  <form @submit.prevent="onSubmit">
    <section class="modal-card-body px-6 py-6">
      <b-field :label="$t('login.email')" label-position="inside">
        <b-input
          type="email"
          v-model="user.email"
          :placeholder="$t('login.your_email')"
          required
          expanded
        >
        </b-input>
      </b-field>

      <b-field :label="$t('login.password')" label-position="inside">
        <b-input type="password" v-model="user.password" password-reveal required expanded>
        </b-input>
      </b-field>

      <b-input type="submit" :value="$t('login.login')" custom-class="button is-primary"></b-input>
      <p class="block mt-4">
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
        } else throw new Error('Invalid Credentials')
      } catch (error) {
        this.$buefy.toast.open({
          duration: 5000,
          message: this.$t('toast.credentials'),
          type: 'is-danger',
        })
      }
    },
  },
}
</script>
