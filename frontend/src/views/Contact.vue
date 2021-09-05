<template>
  <section class="section contact">
    <div class="container">
      <div class="box is-flex is-flex-direction-column is-align-items-center px-6">
        <p class="title">{{ $t('contact.hello') }}Get in touch</p>
        <p class="is-size-6 has-text-weight-semibold">
          {{ $t('contact.text') }}Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eligendi, impedit culpa
          quibusdam eaque! Incidunt, error. In, fuga architecto esse soluta
        </p>
        <form class="my-6" @submit.prevent="onSubmit">
          <b-field label="What are you contacting us about ?" custom-class="is-medium">
            <b-select size="is-medium" v-model="reason" expanded lazy>
              <option value="question" selected>{{ $t('contact.question') }}I have a question about this project</option>
              <option value="abuse">{{ $t('contact.report') }}Report an abuse</option>
              <option value="feedback">{{ $t('contact.feedback') }}Comment / feedback on the website</option>
              <option value="other">{{ $t('contact.other') }}Other</option>
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
            <b-input type="email" icon-pack="fas" icon-right="email" v-model="email" lazy></b-input>
          </b-field>
          <b-input type="submit" value="Send" custom-class="button is-primary"></b-input>
        </form>
      </div>
      <div class="block is-flex is-flex-direction-column is-align-items-center">
        <h1 class="title">{{ $t('contact.faq') }}Find some answers in the FAQ</h1>
        <h1 class="subtitle">
          {{ $t('contact.faq_explain') }}
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad in esse, enim? Repellat
          labore, tempora, nostrum ducimus aliquid accusantium fugit illo ut eveniet, expedita
          veniam quisquam amet? Assumenda necessitatibus, cum?
        </h1>
        <router-link :to="{ path: '/faq' }" class="button is-primary is-medium"
          >{{ $t('contact.faq_cta') }}Visit the FAQ</router-link
        >
      </div>
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
