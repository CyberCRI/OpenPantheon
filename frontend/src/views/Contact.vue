<template>
  <section class="section contact">
    <div class="container">
      <div class="box is-flex is-flex-direction-column is-align-items-center px-6">
        <p class="title">{{ $t('contact.hello') }}</p>
        <p class="is-size-6 has-text-weight-semibold">
          {{ $t('contact.text') }}
        </p>
        <form class="my-6" @submit.prevent="onSubmit">
          <b-field label="What are you contacting us about ?" custom-class="is-medium">
            <b-select size="is-medium" v-model="reason" expanded lazy>
              <option value="question" selected>{{ $t('contact.question') }}</option>
              <option value="abuse">{{ $t('contact.report') }}</option>
              <option value="feedback">{{ $t('contact.feedback') }}</option>
              <option value="other">{{ $t('contact.other') }}</option>
            </b-select>
          </b-field>
          <b-field label="Your message" custom-class="is-medium" required>
            <b-input
              minlength="10"
              maxlength="1000"
              type="textarea"
              custom-class="has-fixed-size is-medium"
              v-model="message"
              lazy
            ></b-input>
          </b-field>
          <b-field label="Name" label-position="inside" required>
            <b-input type="name" v-model="name" lazy></b-input>
          </b-field>
          <b-field label="Email address" label-position="inside" required>
            <b-input type="email" icon-right="email" v-model="email" lazy></b-input>
          </b-field>
          <b-input type="submit" value="Send" custom-class="button is-primary"></b-input>
        </form>
      </div>
      <section class="section is-medium has-text-centered">
      	<div class="container mx-6">
	        <h1 class="title mb-6">{{ $t('contact.faq') }}</h1>
	        <h2 class="subtitle mb-6">
	          {{ $t('contact.faq_explain') }}
	        </h2>
	        <router-link :to="{ path: '/faq' }" class="button is-primary is-medium"
	          >{{ $t('contact.faq_cta') }}</router-link
        	>
        </div>
      </section>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Contact',
  data() {
    return {
      name: null,
      email: null,
      reason: null,
      message: null,
    }
  },
  methods: {
    onSubmit() {
      // let contactForm = {
      //     name: this.name,
      //     email: this.email,
      //     reason: this.reason,
      //     message: this.message,
      // }
      this.name = null
      this.email = null
      this.reason = null
      this.message = null
      // API
    },
  },
}
</script>

<style type="scss" scoped>
.box > p {
  width: 75%;
  text-align: center;
}
</style>
