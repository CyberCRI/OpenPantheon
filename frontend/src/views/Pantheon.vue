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
    <div class="container">
      <Back />
      <div class="box px-6">
        <!-- Head  -->
        <div class="avatar is-pulled-left mr-5" v-if="user">
          {{ (user.first_name[0] + user.last_name[0]) | uppercase }}
        </div>
        <div class="">
          <h1 class="title is-4" v-if="user">
            {{ user.first_name | capitalize }} {{ user.last_name | capitalize }}
          </h1>
          <h2 class="subtitle is-6 has-text-grey-light" v-if="user">
            {{ user.job }}
          </h2>
        </div>

        <div id="head" class="section columns">
          <div class="column is-9">
            <h1 class="title is-4 mb-6" v-if="user">
              {{ user.first_name | capitalize }}'s Pantheon
            </h1>
            <h2 class="subtitle is-6" v-if="count">
              {{
                $t('home.personalities', {
                  count: count,
                  parityWomen: women,
                  parityMen: 100 - women,
                })
              }}
            </h2>
          </div>
          <div class="column is-3">
            <button
              @click="socialModal"
              class="button is-medium is-primary has-text-black has-text-small"
            >
              <strong class="is-size-6">{{ $t('details.share') }}</strong>
            </button>
          </div>
        </div>

        <div class="columns is-multiline mb-5" v-if="user && data">
          <b-loading :is-full-page="false" v-model="isLoading"></b-loading>
          <Card
            class="column is-one-third-desktop is-half"
            v-for="personality in personalities"
            :key="personality.id"
            :personality="personality"
            :data="data ? data[personality.wikipedia_id] : {}"
            :isLoading="isLoading"
            ><p class="comment">{{ findMyComment(personality) | truncate(50) }}</p></Card
          >
        </div>
        <b-pagination
          :total="count"
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
      perPage: 50,
      page: 1,
      personalities: [],
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
    },
    changePage() {
      this.isLoading = true
      this.populateTab()
      window.scrollTo({ top: 168 })
    },
    async populateTab() {
      this.personalities = this.user.personalities_celebrated.slice(
        (this.page - 1) * this.perPage,
        this.page * this.perPage
      )
      let titles = this.personalities.map((personality) => personality.wikipedia_id)
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
  async created() {
    await this.getUserById(this.$router.currentRoute.params.user)
    this.user = this.AuthModule.userDetails
    this.user.personalities_celebrated.forEach((pers) => {
      if (pers.gender == 'f') this.women++
    })
    this.count = this.user.personalities_celebrated.length
    this.women = Math.floor((this.women / this.count) * 100)
    this.populateTab()
  },
  computed: mapState(['AuthModule', 'PersonalityModule']),
  components: {
    Back,
    Card,
  },
  watch: {
    page: {
      handler() {
        this.changePage()
      },
    },
  },
}
</script>

<style type="scss" scoped>
hr {
  border-top: 1px solid #bbb;
}

.button {
  border-radius: 10px;
}

.comment {
  overflow-wrap: break-word;
}

@media (max-width: 1408px) {
  #head {
    flex-direction: column;
    width: 100%;
    height: 100%;
  }
  #head .column {
    width: unset;
    align-self: center;
    text-align: center;
  }
}

@media (max-width: 420px) {
  .box {
    padding: 0 !important;
    box-shadow: unset;
  }
}
</style>
