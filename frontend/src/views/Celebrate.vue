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
          <b-step-item class="my-6" label="Choose a personality">
            <h1 class="title has-text-centered">{{ $t('celebrate.who') }}</h1>
            <h2 class="subtitle has-text-centered">
              {{ $t('celebrate.parity', { pctMen: 100 - parity, pctWomen: parity }) }}
            </h2>
            <WikiAutocomplete @personalitySelected="createPersonality" />
          </b-step-item>

          <b-step-item class="my-6" label="Write a celebration">
            <h1 class="title has-text-centered">{{ $t('celebrate.why', { name: name }) }}</h1>
            <h2 class="subtitle has-text-centered">
              {{ $t('celebrate.explain') }}
            </h2>
            <form @submit.prevent="stepControl(2)">
              <b-field label="" custom-class="is-medium" required>
                <b-input
                  minlength="10"
                  maxlength="1500"
                  type="textarea"
                  custom-class="has-fixed-size is-medium"
                  v-model="comment.text"
                  lazy
                  placeholder="Add a comment"
                ></b-input>
              </b-field>
              <b-field
                class="mb-6"
                grouped
                group-multiline
                v-for="(reference, index) in references"
                :key="index"
              >
                <b-field>
                  <b-button
                    icon-right="minus"
                    class="button"
                    @click="removeInput(index)"
                    v-if="references.length > 1"
                  ></b-button>
                </b-field>
                <b-field expanded>
                  <b-input
                    type="text"
                    v-model="reference.name"
                    placeholder="Name"
                    required
                  ></b-input>
                </b-field>
                <b-field expanded>
                  <b-input
                    type="url"
                    v-model="reference.link"
                    placeholder="Link"
                    required
                  ></b-input>
                </b-field>
                <b-field>
                  <b-button
                    icon-right="plus"
                    class="button"
                    @click="addInput(index)"
                    v-if="references.length < 10"
                  ></b-button>
                </b-field>
              </b-field>
              <input type="submit" class="button is-primary is-pulled-right" value="Submit" />
            </form>
          </b-step-item>

          <b-step-item class="my-6" label="Publish"> </b-step-item>
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
          console.log('new')
          this.celebrate()
        } else {
          console.log('update')
          if (
            !this.$store.getters.listPersonalitiesCelebrated.includes(this.personality.wikipedia_id)
          )
            this.createCommentAndLike()
          else {
            this.$buefy.toast.open({
              duration: 5000,
              message: 'This personality is already in your pantheon',
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
      const tab = this.references.map((ref) => ref.name + '|' + ref.link)
      this.comment.fluff = tab.join('~')
      await this.$store.dispatch('createComment', this.comment)
      await this.$store.dispatch('addToPantheon', personality.id)
      await this.$store.dispatch('getCurrentUserDetails')
      this.$router.push({ name: 'Home' })
    },
    async celebrate() {
      await this.$store
        .dispatch('createPersonality', this.personality)
        .then(async () => {
          this.$buefy.toast.open({
            duration: 5000,
            message: 'Success',
            type: 'is-success',
          })
          await this.$store.dispatch('getPantheonStats')
          await this.createCommentAndLike()
        })
        .catch((error) => {
          this.$buefy.toast.open({
            duration: 5000,
            message: "Sorry, we couldn't handle your request",
            type: 'is-danger',
          })
          console.log('There was a problem:', error.response)
        })
    },
  },
}
</script>

<style scoped></style>
