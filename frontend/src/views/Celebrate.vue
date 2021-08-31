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
        <h1 class="title has-text-centered">Who do you want to celebrate ?</h1>
        <h2 class="subtitle has-text-centered">
          There is currently 50% men and 50% women on the Pantheon. Let's try to maintain a gender
          parity !
        </h2>
        <WikiAutocomplete @personalitySelected="createPersonality" />
      </b-step-item>

      <b-step-item step="2" label="Write a celebration">
        <h1 class="title has-text-centered">Why do you want to celebrate {{ name }} ?</h1>
        <h2 class="subtitle has-text-centered">
          Let us know briefly why that person is special to you and why you'd like to add them to
          the Pantheon.
        </h2>
        <input v-model="comment.text" type="text" placeholder="Add a comment" />
        <input v-model="comment.fluff" type="text" placeholder="Add some fluff" />
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
  computed: {
    isLoggedIn() {
      return this.$store.getters.isAuthenticated
    },
  },
  components: {
    WikiAutocomplete,
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
          this.createCommentAndLike()
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
