<template>
  <div class="box">
    <b-steps
      v-model="activeStep"
      animated
      rounded
      has-navigation
      label-position="bottom"
      @input="stepControl"
    >
      <b-step-item step="1" label="Choose a personality">
        <h1 class="title has-text-centered">{{ $t('celebrate.who') }}</h1>
        <h2 class="subtitle has-text-centered">
          {{ $t('celebrate.parity', { pctMen: '50%', pctWomen: '50%' }) }}
        </h2>
        <WikiAutocomplete @personalitySelected="createPersonality" />
      </b-step-item>

      <b-step-item step="2" label="Write a celebration">
        <h1 class="title has-text-centered">{{ $t('celebrate.why', { name: name })  }}</h1>
        <h2 class="subtitle has-text-centered">
          {{ $t('celebrate.explain') }}
        </h2>
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
        <b-field label="Want to add an external link ? (Optional)" required>
          <b-input type="name" v-model="comment.fluff" placeholder="Add an external link" lazy></b-input>
        </b-field>
      </b-step-item>

      <b-step-item step="3" label="Publish"> </b-step-item>

      <template #navigation="{ next }">
        <b-button outlined type="is-primary" :disabled="next.disabled" @click.prevent="next.action">
          Next
        </b-button>
      </template>
    </b-steps>
  </div>
</template>

<script>
// import { mapGetters, mapActions } from 'vuex'
import AuthModal from '@/components/AuthModal'
import WikiAutocomplete from '@/components/WikiAutocomplete'

export default {
  name: 'Celebrate',
  data() {
    return {
      activeStep: 0,
      name: null,
      personality: {},
      comment: {},
      alreadyInDB: null,
    }
  },
  props: {
    personalityProp: String,
    nameProp: String
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isAuthenticated
    },
  },
  components: {
    WikiAutocomplete,
  },
  mounted() {
    if (this.personalityProp && this.nameProp) {
      this.alreadyInDB = 1
      this.personality.wikipedia_id = this.personalityProp
        this.name = this.nameProp
        this.activeStep++
      this.stepControl(1)
    }
  },
  methods: {
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
          if (!this.$store.getters.listPersonalitiesCelebrated.includes(this.personality.wikipedia_id))
            this.createCommentAndLike()
          else {
             this.$buefy.toast.open({
              duration: 5000,
              message: "This personality is already in your pantheon",
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
    },
    async createCommentAndLike() {
      const personality = await this.$store.dispatch(
        'fetchPersonalityByWiki',
        this.personality.wikipedia_id
      )
      this.comment.author_id = this.$store.getters.idUser
      this.comment.personality_id = personality.id
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
