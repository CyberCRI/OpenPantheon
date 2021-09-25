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
  <section class="section contact">
    <div class="container">
      <div class="box is-flex is-flex-direction-column is-align-items-center px-6">
        <p class="title">{{ $t('contact.hello') }}</p>
        <p class="is-size-6 has-text-weight-semibold">
          {{ $t('contact.text') }}
        </p>
        <form class="my-6" @submit.prevent="onSubmit">
          <b-field :label="$t('contact.why')" custom-class="is-medium">
            <b-select size="is-medium" v-model="reason" expanded>
              <option value="question" selected>{{ $t('contact.question') }}</option>
              <option value="abuse">{{ $t('contact.report') }}</option>
              <option value="feedback">{{ $t('contact.feedback') }}</option>
              <option value="other">{{ $t('contact.other') }}</option>
            </b-select>
          </b-field>
          <b-field :label="$t('contact.your_message')" custom-class="is-medium">
            <b-input
              minlength="10"
              maxlength="1000"
              type="textarea"
              custom-class="has-fixed-size is-medium"
              v-model="message"
              required
            ></b-input>
          </b-field>
          <b-field :label="$t('contact.name')" label-position="inside">
            <b-input type="name" v-model="name" required></b-input>
          </b-field>
          <b-field :label="$t('contact.mail')" label-position="inside">
            <b-input type="email" icon-right="email" v-model="email" required></b-input>
          </b-field>
          <b-input
            type="submit"
            :value="$t('contact.send')"
            custom-class="button is-primary"
          ></b-input>
        </form>
      </div>
      <section class="section is-medium has-text-centered">
        <div class="container mx-6">
          <h1 class="title mb-6">{{ $t('contact.faq') }}</h1>
          <h2 class="subtitle mb-6">
            {{ $t('contact.faq_explain') }}
          </h2>
          <router-link :to="{ path: '/faq' }" class="button is-primary is-medium">{{
            $t('contact.faq_cta')
          }}</router-link>
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
      reason: this.report ? 'abuse' : 'question',
      message: this.report ? this.report : null,
    }
  },
  props: {
    report: {
      type: String,
      default: '',
    },
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
