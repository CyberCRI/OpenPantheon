<template>
  <section class="section">
      <div class="container">
      <Back />
      <div class="box px-6">
      <!-- Head  -->
        <div class="avatar is-pulled-left mr-5" v-if="user">{{ user.first_name[0] + user.last_name[0] | uppercase }}</div>
        <div class="">
          <h1 class="title is-4" v-if="user">
            {{ user.first_name | capitalize }} {{ user.last_name | capitalize }}
          </h1>
          <h2 class="subtitle is-6 has-text-grey-light" v-if="user">
            {{ user.job }}
          </h2>
        </div>

        <div class="section columns">
          <div class="column is-9">
            <h1 class="title is-4 mb-6" v-if="user">
              {{ user.first_name | capitalize }}'s Pantheon
            </h1>
            <h2 class="subtitle is-6" v-if="count">
              {{ $t('home.personalities', {count: count, parityWomen: women, parityMen: 100 - women}) }}
            </h2>
          </div>
          <div class="column is-3">
            <button
              @click="socialModal"
              class="button is-large is-primary has-text-black has-text-small"
              ><strong class="is-size-6 mx-6">{{ $t('details.share') }}</strong></button
            >
          </div>
        </div>

        <div class="columns is-multiline mb-5">
          <b-loading :is-full-page="false" v-model="isLoading"></b-loading>
          <Card
            class="column is-one-third"
            v-for="personality in user.personalities_celebrated"
            :key="personality.id"
            :personality="personality"
            :data="data ? data[personality.wikipedia_id] : {}"
            :isLoading="isLoading"
          ><p class="comment">{{ findMyComment(personality) | truncate(50)}}</p></Card>
        </div>

      </div>
    </div>
  </section>
</template>

<script>
import wbk from 'wikidata-sdk'
import SocialModal from '@/components/SocialModal.vue'
import Back from '@/components/Back.vue'
import Card from '@/components/Card.vue'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Pantheon',
  data() {
    return {
      data: [],
      user: null,
      women: null,
      count: null,
      isLoading: true,
    }
  },
  methods: {
    ...mapActions(['getUserById']),
    socialModal() {
      this.$buefy.modal.open({
        parent: this,
        component: SocialModal,
        hasModalCard: false,
        customClass: '',
        trapFocus: true,
      })
    },
    findMyComment(personality) {
      return personality.comments.find((comment) => comment.author_id === this.user.id).text
    }
  },
  async created() {
    await this.getUserById(this.$router.currentRoute.params.user)
    this.user = this.AuthModule.userDetails
    this.user.personalities_celebrated.forEach((pers) => {
      if (pers.gender == 'f')
        this.women++
    })
    this.count = this.user.personalities_celebrated.length
    this.women = Math.floor(this.women / this.count * 100)
    let titles = this.user.personalities_celebrated.map(
        (personality) => personality.wikipedia_id
      )
    const url = await wbk.getEntities({
      ids: titles,
      languages: [this.$i18n.locale],
    })
    await fetch(url, {
      headers: {
        'Accept-Encoding': 'gzip',
      },
    })
      .then((res) => res.json()) //
      .then(wbk.parse.wb.entities)
      .then((entities) => {
        this.data = entities
        this.isLoading = false
      })
    this.findMyComment()
  },
  computed: mapState(['AuthModule', 'PersonalityModule']),
  components: {
    Back,
    Card
  }
}
</script>

<style type="scss" scoped>
#main_image {
  max-height: 240px;
  max-width: 240px;
  border-radius: 0.75rem;
  object-fit: cover;
}

#main_image_container {
  height: 240px;
  width: 240px;
}

hr {
  border-top: 1px solid #bbb;
}

.button {
  border-radius: 10px;
}

.comment {
  overflow-wrap: break-word;
}

</style>
