<template>
  <section class="modal-card-body px-6 py-6">
    <form v-show="!contactProvided" @submit.prevent="contactProvided = true">
      <b-field label="Email" label-position="inside">
        <b-input type="email" v-model="user.email" placeholder="Your email" required expanded />
      </b-field>

      <b-field label="Password" label-position="inside">
        <b-input type="password" v-model="user.password" password-reveal required expanded>
        </b-input>
      </b-field>
      <b-input type="submit" value="Sign up" custom-class="button is-primary" expanded></b-input>
      <p class="block">
        {{ $t('register.already') }}<a @click="$emit('switchView')">{{ $t('register.login') }}</a
        >*
      </p>
    </form>
    <form v-show="contactProvided" @submit.prevent="onSubmit">
      <p class="title">{{ $t('register.welcome') }}</p>
      <p class="is-size-6 has-text-weight-semibold">
        {{ $t('register.welcome_text') }}
      </p>
      <b-field label="First name" label-position="inside">
        <b-input v-model="user.firstName" placeholder="John" required expanded />
      </b-field>

      <b-field label="Last name" label-position="inside">
        <b-input v-model="user.lastName" placeholder="Doe" required expanded> </b-input>
      </b-field>

      <b-field label="Your job title / role (optional)" label-position="inside">
        <b-input v-model="user.job" placeholder="Artist" expanded> </b-input>
      </b-field>

      <b-field label="Your organization (optional)" label-position="inside">
        <b-input v-model="user.organization" placeholder="Artist" expanded> </b-input>
      </b-field>
      <b-input
        type="submit"
        value="Create my account"
        custom-class="button is-primary"
        expanded
      ></b-input>
    </form>
  </section>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Register',
  data() {
    return {
      contactProvided: false,
      user: {
        email: null,
        password: null,
        firstName: null,
        lastName: null,
        job: null,
        organization: null,
      },
    }
  },
  methods: {
    ...mapActions(['Register']),
    async onSubmit() {
      try {
        await this.Register(this.user)
      } catch (error) {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'This email is already in use',
          type: 'is-danger',
        })
      }
      this.$emit('close')
    },
  },
}
</script>
