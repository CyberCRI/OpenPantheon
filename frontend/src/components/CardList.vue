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
  <section>
    <div class="columns is-multiline" v-if="PersonalityModule.personalities">
      <b-loading :is-full-page="false" v-model="isLoading"></b-loading>
      <Card
        class="column is-one-quarter"
        v-for="personality in PersonalityModule.personalities"
        :key="personality.id"
        :personality="personality"
        :data="data ? data[personality.wikipedia_id] : {}"
        :isLoading="isLoading"
      ></Card>
    </div>
    <div class="content" v-else>
      <h1>{{ $t('home.empty') }}</h1>
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
      isLoading: true,
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
        region: this.region,
      })
      if (this.PersonalityModule.personalities.length == 0) {
        this.isLoading = false
        this.data = []
        return
      }
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
    field: String,
    sort: String,
    region: String,
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
    region: {
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
