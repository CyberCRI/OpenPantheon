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
  <section class="section">
    <Back />
    <div class="container">
      <div class="box">
        <div class="container mx-6 my-6 has-text-centered">
          <h1 class="title my-6 is-size-4">{{ $t('celebrate.title') }}</h1>
          <h2 class="subtitle mb-6 is-size-6">
            {{ $t('celebrate.subtitle') }}
          </h2>
        </div>
        <b-steps
          v-model="activeStep"
          animated
          rounded
          :has-navigation="false"
          label-position="bottom"
          @input="stepControl"
        >
          <b-step-item class="my-6" :label="$t('celebrate.choose')">
            <h1 class="title has-text-centered">{{ $t('celebrate.who') }}</h1>
            <h2 class="subtitle has-text-centered">
              {{ $t('celebrate.parity', { pctMen: 100 - parity, pctWomen: parity }) }}
            </h2>
            <WikiAutocomplete @personalitySelected="createPersonality" />
          </b-step-item>

          <b-step-item class="my-6" :label="$t('celebrate.write')">
            <h1 class="title has-text-centered">{{ $t('celebrate.why', { name: name }) }}</h1>
            <h2 class="subtitle has-text-centered">
              {{ $t('celebrate.explain') }}
            </h2>
            <form @submit.prevent="checkForm()">
              <b-field label="" custom-class="is-medium">
                <b-input
                  minlength="10"
                  maxlength="1500"
                  type="textarea"
                  custom-class="has-fixed-size is-medium"
                  v-model="comment.text"
                  :placeholder="$t('celebrate.add')"
                  required
                ></b-input>
              </b-field>
              <h2 class="subtitle is-size-6">
                {{ $t('celebrate.links') }}
              </h2>
              <b-field
                class="mb-6"
                grouped
                group-multiline
                v-for="(reference, index) in references"
                :key="index"
              >
                <b-field v-if="references.length > 1">
                  <b-button
                    icon-right="minus"
                    class="button"
                    @click="removeInput(index)"
                  ></b-button>
                </b-field>
                <b-field expanded>
                  <b-input
                    type="text"
                    v-model="reference.name"
                    :placeholder="$t('celebrate.link_title')"
                    ref="name"
                  ></b-input>
                </b-field>
                <b-field expanded>
                  <b-input
                    type="url"
                    v-model="reference.link"
                    :placeholder="$t('celebrate.link_target')"
                    ref="link"
                  ></b-input>
                </b-field>
                <b-field v-if="references.length < 10">
                  <b-button icon-right="plus" class="button" @click="addInput(index)"></b-button>
                </b-field>
              </b-field>
              <p class="has-text-danger" v-if="error">{{ error }}</p>
              <input
                type="submit"
                class="button is-primary is-pulled-right"
                :value="$t('celebrate.submit')"
              />
            </form>
          </b-step-item>

          <b-step-item class="my-6" :label="$t('celebrate.publish')"> </b-step-item>
        </b-steps>
      </div>
      <section class="section is-medium has-text-centered">
        <div class="container mx-6">
          <h1 class="title is-size-4 mb-6">{{ $t('contact.faq') }}</h1>
          <h2 class="subtitle is-size-6 mb-6">
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
// import { mapGetters, mapActions } from 'vuex'
import AuthModal from '@/components/AuthModal'
import WikiAutocomplete from '@/components/WikiAutocomplete'
import Back from '@/components/Back'
import { continents, countries } from 'countries-list'
import wbk from 'wikidata-sdk'

export default {
  name: 'Celebrate',
  data() {
    return {
      activeStep: 0,
      name: null,
      personality: {},
      comment: {},
      alreadyInDB: null,
      references: [
        {
          link: '',
          name: '',
        },
      ],
      parity: null,
      error: null,
      input: [],
    }
  },
  props: {
    personalityProp: String,
    nameProp: String,
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isAuthenticated
    },
  },
  components: {
    WikiAutocomplete,
    Back,
  },
  mounted() {
    if (this.personalityProp && this.nameProp) {
      this.alreadyInDB = 1
      this.personality.wikipedia_id = this.personalityProp
      this.name = this.nameProp
      this.activeStep++
      this.stepControl(1)
    }
    this.parity = this.$store.getters.pantheonParity
  },
  methods: {
    checkForm() {
      let flag = 1
      this.references.forEach((ref, index) => {
        if (
          (this.$refs.name[index].$refs.input._value &&
            !this.$refs.link[index].$refs.input._value) ||
          (!this.$refs.name[index].$refs.input._value && this.$refs.link[index].$refs.input._value)
        ) {
          flag = 0
          if (!this.$refs.link[index].$refs.input._value)
            this.$refs.link[index].$refs.input.className += ' is-danger'
          else this.$refs.name[index].$refs.input.className += ' is-danger'
          this.error = this.$t('celebrate.warning')
        }
      })
      if (flag) this.stepControl(2)
    },
    addInput(index) {
      this.references.splice(index + 1, 0, { link: '', name: '' })
    },
    removeInput(index) {
      this.references.splice(index, 1)
    },
    stepControl(step) {
      if (step == '1') {
        if (!this.isLoggedIn) {
          this.$buefy.modal.open({
            parent: this,
            component: AuthModal,
            hasModalCard: true,
            customClass: '',
            trapFocus: true,
            canCancel: false,
          })
        }
      } else if (step == '2') {
        if (!this.alreadyInDB) {
          this.celebrate()
        } else {
          if (
            !this.$store.getters.listPersonalitiesCelebrated.includes(this.personality.wikipedia_id)
          )
            this.createCommentAndLike()
          else {
            this.$buefy.toast.open({
              duration: 5000,
              message: this.$t('toast.already_in_pantheon'),
              type: 'is-danger',
            })
            this.$router.push({ name: 'Home' })
          }
        }
      }
    },
    createPersonality(entity) {
      this.personality.wikipedia_id = entity.id
      this.name = entity.labels[this.$i18n.locale]
      this.personality.gender = entity.claims.P21[0] == 'Q6581072' ? 'f' : 'm'
      this.personality.field = ''
      let url = wbk.sparqlQuery(`
ASK
WHERE
{
  wd:${this.personality.wikipedia_id} wdt:P106 ?occupation.
  ?occupation wdt:P31*/wdt:P279* wd:Q901.
}
      `)
      fetch(url)
        .then((response) => response.json())
        .then((response) => (response.boolean == true ? (this.personality.field += 'science') : ''))
      url = wbk.sparqlQuery(`
ASK
WHERE
{
  wd:${this.personality.wikipedia_id} wdt:P106 ?occupation.
  ?occupation wdt:P31*/wdt:P279* wd:Q483501.
}
      `)
      fetch(url)
        .then((response) => response.json())
        .then((response) => (response.boolean == true ? (this.personality.field += 'art') : ''))
      url = wbk.sparqlQuery(`
ASK
WHERE
{
  wd:${this.personality.wikipedia_id} wdt:P106 ?occupation.
  ?occupation wdt:P425 ?field.
  ?field wdt:P31*/wdt:P279* wd:Q8434
}
      `)
      fetch(url)
        .then((response) => response.json())
        .then((response) =>
          response.boolean == true ? (this.personality.field += 'education') : ''
        )
      url = wbk.sparqlQuery(`
SELECT ?code_iso
WHERE
{
wd:${this.personality.wikipedia_id} wdt:P27 [ wdt:P297 ?code_iso ].
}
      `)
      fetch(url)
        .then((response) => response.json())
        .then((response) => {
          this.personality.continent =
            continents[countries[response.results.bindings[0].code_iso.value].continent]
        })

      this.alreadyInDB = entity.celebrations
      this.activeStep++
      this.stepControl(1)
    },
    async createCommentAndLike() {
      const personality = await this.$store.dispatch(
        'fetchPersonalityByWiki',
        this.personality.wikipedia_id
      )
      this.comment.author_id = this.$store.getters.idUser
      this.comment.personality_id = personality.id
      this.input.push(this.comment)
      this.input.push(...this.references)

      await this.$store.dispatch('createComment', this.input)
      this.input = []
      await this.$store.dispatch('addToPantheon', personality.id)
      await this.$store.dispatch('getCurrentUserDetails')
      this.$router.push({ name: 'Details', params: { id: personality.id } })
    },
    async celebrate() {
      await this.$store
        .dispatch('createPersonality', this.personality)
        .then(async () => {
          this.$buefy.toast.open({
            duration: 5000,
            message: this.$t('toast.success'),
            type: 'is-success',
          })
          await this.$store.dispatch('getPantheonStats')
          await this.createCommentAndLike()
        })
        .catch(() => {
          this.$buefy.toast.open({
            duration: 5000,
            message: this.$t('toast.unknown'),
            type: 'is-danger',
          })
        })
    },
  },
}
</script>

<style scoped></style>
