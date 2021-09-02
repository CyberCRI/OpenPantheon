<template>
  <section>
    <div class="columns is-multiline">
   	  <b-loading :is-full-page=false v-model="isLoading"></b-loading>
      <Card
        class="column is-one-quarter"
        v-for="personality in PersonalityModule.personalities"
        :key="personality.id"
        :personality="personality"
        :data="data ? data[personality.wikipedia_id] : {}"
        :isLoading="isLoading"
      ></Card>
    </div>
    <b-pagination
      :total="PersonalityModule.total"
      v-model="page"
      order="is-centered"
      rounded
      :per-page="perPage"
      icon-prev="chevron-left"
      icon-next="chevron-right"
      aria-next-label="Next page"
      aria-previous-label="Previous page"
      aria-page-label="Page"
      aria-current-label="Current page"
    >
    </b-pagination>
  </section>
</template>

<script>
import wbk from 'wikidata-sdk'
import Card from '@/components/Card.vue'
import { mapState } from 'vuex'

export default {
  name: 'CardList',
  data() {
    return {
      perPage: 16,
      page: 1,
      data: null,
      isLoading: false
    }
  },
  methods: {
    async populateList() {
   	  this.isLoading = true
      await this.$store.dispatch('fetchAll', {
        loggedIn: this.$store.getters.isAuthenticated,
        skip: (this.page - 1) * this.perPage,
        limit: this.perPage,
        personal: this.personal == 'open' ? 0 : 1,
        women: this.women,
        field: this.field,
        sort: this.sort,
      })
      let titles = this.PersonalityModule.personalities.map(
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
    },
  },
  props: {
    personal: String,
    id: Number,
    randomSelection: Boolean,
    extended: Boolean,
    filter: Number,
    women: Boolean,
    field: Number,
    sort: String,
  },
  components: {
    Card,
  },
  computed: {
    ...mapState(['PersonalityModule']),
  },
  mounted() {
      this.isLoading = true
  },
  watch: {
    page: {
      handler() {
        this.populateList()
      },
      immediate: true,
    },
    personal: {
      handler() {
        this.populateList()
      },
    },
    women: {
      handler() {
        this.populateList()
      },
    },
    field: {
      handler() {
        this.populateList()
      },
    },
    sort: {
      handler() {
        this.populateList()
      },
    },
  },
}
</script>

<style type="scss" scoped></style>
