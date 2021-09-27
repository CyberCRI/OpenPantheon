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
  <section class="section container">
    <Back />
    <div class="box">
      <!-- Head  -->

      <div class="section columns is-align-items-self-end" id="head">
        <div class="column is-3">
          <figure v-if="data.claims" class="image is-square" id="main_image_container">
            <img
              id="main_image"
              :src="
                data.claims.P18
                  ? `https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/${data.claims.P18[0].mainsnak.datavalue.value}&width=320`
                  : './img/silhouette.png'
              "
              :style="{ 'background-color': data.claims.P18 ? '' : '#202137' }"
            />
          </figure>
        </div>

        <div class="column is-3">
          <div v-if="!isLoading" class="container pb-3">
            <h1 v-if="data.labels && data.labels[$i18n.locale]" class="title is-spaced">
              {{ data.labels[$i18n.locale].value }}
            </h1>
            <h1 v-else class="title is-spaced">
              {{ $t('misc.name_unavailable') }}
            </h1>
            <h2 v-if="data.descriptions && data.descriptions[$i18n.locale]" class="subtitle is-6">
              {{ data.descriptions[$i18n.locale].value | capitalize({ onlyFirstLetter: true }) }}
            </h2>
            <h2 v-else class="subtitle is-6">
              {{ $t('misc.desc_unavailable') }}
            </h2>
            <small v-if="data.claims"
              >{{ celebrations }} {{ celebrations | pluralize('Celebration') }}</small
            >
          </div>

          <router-link
            :to="{
              path: `/celebrate?q=${personality.wikipedia_id}&n=${data.labels[$i18n.locale].value}`,
            }"
            class="button is-medium has-text-small is-primary is-mobile px-0"
            :class="{
              'is-hidden':
                $store.getters.isAuthenticated &&
                $store.getters.listPersonalitiesCelebrated.includes(personality.wikipedia_id),
            }"
            v-if="!isLoading && data.labels && data.labels[$i18n.locale]"
            ><strong class="is-size-6 mx-6">{{ $t('details.celebrate') }}</strong></router-link
          >
        </div>

        <div class="column is-3">
          <button
            @click="socialModal"
            class="button is-medium has-text-small px-0"
            v-if="!isLoading"
          >
            <strong class="is-size-6 mx-6">{{ $t('details.share') }}</strong>
          </button>
        </div>
        <div class="column is-3">
          <a
            :href="wikiLink"
            class="button is-medium has-text-small px-0"
            v-if="!isLoading && wikiLink"
            ><strong class="is-size-6 mx-6">{{ $t('details.wikipedia') }}</strong></a
          >
        </div>
      </div>

      <!-- Bio and factsheet  -->

      <div id="bio" class="section">
        <h2 id="title" class="title is-4">{{ $t('details.about') }}</h2>
        <div class="columns is-align-items-self-start">
          <p class="has-text-justified column is-7" v-if="bio">
            {{ bio }}
          </p>
          <div id="factsheet" class="column is-4 is-offset-1">
            <p v-if="properties.notableWork[0]">
              <span class="has-text-weight-bold">{{ $t('details.notable') }}</span>
              {{ properties.notableWork.join(', ') }}
            </p>
            <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

            <p v-if="properties.marriages[0]">
              <span class="has-text-weight-bold">{{ $t('details.spouse') }}</span>
              <span v-for="(marriage, index) in properties.marriages" :key="index">
                {{ marriage.spouse }} (m. {{ marriage.start }};
                {{ marriage.reason == 'death' ? 'died' : '' }} {{ marriage.end }})
              </span>
            </p>
            <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

            <p v-if="properties.children[0]">
              <span class="has-text-weight-bold">{{ $t('details.children') }}</span>
              {{ properties.children.join(', ') }}
            </p>
            <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

            <p v-if="properties.dateOfBirth && properties.placeOfBirth">
              <span class="has-text-weight-bold">{{ $t('details.born') }}</span>
              {{ properties.dateOfBirth }}, {{ properties.placeOfBirth }}
              {{ properties.extendedPlaceOfBirth.join(', ') }}
            </p>
            <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

            <p v-if="properties.dateOfDeath && properties.placeOfDeath">
              <span class="has-text-weight-bold">{{ $t('details.died') }}</span>
              {{ properties.dateOfDeath }} (aged {{ properties.ageOfDeath }}),
              {{ properties.placeOfDeath }} {{ properties.extendedPlaceOfDeath.join(', ') }}
            </p>
            <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>
          </div>
        </div>
      </div>

      <hr />

      <!-- Comments  -->

      <div class="section" v-if="personality.comments">
        <h2 id="title" class="title is-4" v-if="data.claims">
          {{ celebrations }} {{ celebrations | pluralize('Celebration') }}
        </h2>
        <div class="columns is-multiline is-centered">
          <Comment
            class="column is-6-desktop is-12-mobile"
            v-for="(comment, index) in personality.comments.slice(0, 6)"
            :key="index"
            :comment="comment"
          />
        </div>
        <div class="container has-text-centered">
          <button
            @click="commentModal"
            class="button is-medium has-text-small is-primary is-mobile"
            v-if="!isLoading"
          >
            <strong class="is-size-7 mx-6">{{ $t('details.show_celebrations') }}</strong>
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import wbk from 'wikidata-sdk'
import SocialModal from '@/components/SocialModal.vue'
import CommentsModal from '@/components/CommentsModal.vue'
import Comment from '@/components/Comment.vue'
import Back from '@/components/Back.vue'
import { mapState } from 'vuex'

export default {
  name: 'Details',
  data() {
    return {
      data: {},
      properties: {
        spouses: [],
        marriages: [],
        notableWork: [],
        children: [],
        dateOfBirth: '',
        dateOfDeath: '',
        placeOfBirth: '',
        extendedPlaceOfBirth: [],
        placeOfDeath: '',
        extendedPlaceOfDeath: [],
        ageOfDeath: '',
      },
      personality: {},
      bio: '',
      celebrations: null,
      isLoading: true,
      isLoadingProperties: true,
      wikiLink: null,
    }
  },
  async created() {
    await this.$store.dispatch('fetchPersonality', this.$router.currentRoute.params.id)
    this.personality = this.PersonalityModule.personality
    this.celebrations = this.personality.comments.length
    const url = wbk.getEntities({
      ids: this.personality.wikipedia_id,
      languages: [this.$i18n.locale],
    })
    await fetch(url, {
      headers: {
        'Accept-Encoding': 'gzip',
      },
    })
      .then((res) => res.json())
      .then(async (res) => {
        this.data = res.entities[this.personality.wikipedia_id]
        if (res.entities[this.personality.wikipedia_id].sitelinks[this.$i18n.locale + 'wiki']) {
          this.wikiLink = wbk.getSitelinkUrl(
            res.entities[this.personality.wikipedia_id].sitelinks[this.$i18n.locale + 'wiki'].site,
            res.entities[this.personality.wikipedia_id].sitelinks[this.$i18n.locale + 'wiki'].title
          )
          await fetch(
            `https://${
              this.$i18n.locale
            }.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=${
              res.entities[this.personality.wikipedia_id].sitelinks[this.$i18n.locale + 'wiki']
                .title
            }&origin=*`,
            {
              headers: {
                'Accept-Encoding': 'gzip',
              },
            }
          )
            .then((res) => res.json())
            .then(
              (response) =>
                (this.bio = response.query.pages[Object.keys(response.query.pages)[0]].extract)
            )
        }
        this.isLoading = false
        this.getProperties()
      })
  },
  methods: {
    socialModal() {
      this.$buefy.modal.open({
        parent: this,
        component: SocialModal,
        hasModalCard: false,
        customClass: '',
        trapFocus: true,
      })
    },
    commentModal() {
      this.$buefy.modal.open({
        parent: this,
        component: CommentsModal,
        props: { comments: this.personality.comments },
        hasModalCard: false,
        customClass: '',
        trapFocus: true,
      })
    },
    getArrayOfProperties(id, propertyName) {
      const url = wbk.getEntities({
        ids: id,
        languages: [this.$i18n.locale],
      })
      return fetch(url, {
        headers: {
          'Accept-Encoding': 'gzip',
        },
      })
        .then((res) => res.json())
        .then(wbk.parse.wb.entities)
        .then((entities) => {
          this.properties[propertyName].push(entities[id].labels[this.$i18n.locale])
        })
    },
    getSimpleProperty(id, propertyName) {
      const url = wbk.getEntities({
        ids: id,
        languages: [this.$i18n.locale],
      })
      return fetch(url, {
        headers: {
          'Accept-Encoding': 'gzip',
        },
      })
        .then((res) => res.json())
        .then(wbk.parse.wb.entities)
        .then((entities) => {
          this.properties[propertyName] = entities[id].labels[this.$i18n.locale]
        })
    },
    dateFormatter(str) {
      str = wbk.wikibaseTimeToISOString(str)
      const formatter = new Intl.DateTimeFormat(this.$i18n.locale, {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      })
      return formatter.format(new Date(str))
    },
    ageAtDeath(dateOfBirth, dateOfDeath) {
      dateOfBirth = wbk.wikibaseTimeToISOString(dateOfBirth)
      dateOfDeath = wbk.wikibaseTimeToISOString(dateOfDeath)
      return new Date(new Date(dateOfDeath) - new Date(dateOfBirth).getTime()).getFullYear() - 1970
    },
    async getProperties() {
      let birth = ''
      let death = ''
      if (this.data.claims.P569) birth = this.data.claims.P569[0].mainsnak.datavalue.value.time
      if (this.data.claims.P570) death = this.data.claims.P570[0].mainsnak.datavalue.value.time
      if (this.data.claims.P19) {
        await this.getSimpleProperty(
          this.data.claims.P19[0].mainsnak.datavalue.value.id,
          'placeOfBirth'
        )
        if (this.data.claims.P19[0].qualifiers) {
          if (this.data.claims.P19[0].qualifiers.P131)
            this.data.claims.P19[0].qualifiers.P131.forEach(async (key) => {
              await this.getArrayOfProperties(key.datavalue.value.id, 'extendedPlaceOfBirth')
            })
          if (this.data.claims.P19[0].qualifiers.P17)
            this.data.claims.P19[0].qualifiers.P17.forEach(async (key) => {
              await this.getArrayOfProperties(key.datavalue.value.id, 'extendedPlaceOfBirth')
            })
        }
      }
      if (this.data.claims.P20) {
        await this.getSimpleProperty(
          this.data.claims.P20[0].mainsnak.datavalue.value.id,
          'placeOfDeath'
        )
        if (this.data.claims.P20[0].qualifiers) {
          if (this.data.claims.P20[0].qualifiers.P131)
            this.data.claims.P20[0].qualifiers.P131.forEach(async (key) => {
              await this.getArrayOfProperties(key.datavalue.value.id, 'extendedPlaceOfDeath')
            })
          if (this.data.claims.P20[0].qualifiers.P17)
            this.data.claims.P20[0].qualifiers.P17.forEach(async (key) => {
              await this.getArrayOfProperties(key.datavalue.value.id, 'extendedPlaceOfDeath')
            })
        }
      }
      if (birth) this.properties.dateOfBirth = this.dateFormatter(birth)
      if (death) this.properties.dateOfDeath = this.dateFormatter(death)
      if (this.properties.dateOfDeath) this.properties.ageOfDeath = this.ageAtDeath(birth, death)
      if (this.data.claims.P26) {
        for (const spouse of this.data.claims.P26)
          await this.getArrayOfProperties(spouse.mainsnak.datavalue.value.id, 'spouses')
        this.data.claims.P26.forEach((spouse, index) => {
          this.properties.marriages.push({
            spouse: this.properties.spouses[index],
            start:
              spouse.qualifiers && spouse.qualifiers.P580
                ? wbk
                    .wikibaseTimeToDateObject(spouse.qualifiers.P580[0].datavalue.value.time)
                    .getFullYear()
                : '',
            end:
              spouse.qualifiers && spouse.qualifiers.P582
                ? wbk
                    .wikibaseTimeToDateObject(spouse.qualifiers.P582[0].datavalue.value.time)
                    .getFullYear()
                : '',
            reason:
              spouse.qualifiers &&
              spouse.qualifiers.P1534 &&
              spouse.qualifiers.P1534[0].datavalue.value.id == 'Q24037741'
                ? 'death'
                : '',
            order:
              spouse.qualifiers && spouse.qualifiers.P1545
                ? spouse.qualifiers.P1545[0].datavalue.value
                : 0,
          })
        })
        this.properties.marriages.sort((a, b) => a.order - b.order)
      }
      if (this.data.claims.P40) {
        for (const child of this.data.claims.P40) {
          await this.getArrayOfProperties(child.mainsnak.datavalue.value.id, 'children')
        }
      }
      if (this.data.claims.P800) {
        this.data.claims.P800.forEach(async (work) => {
          await this.getArrayOfProperties(work.mainsnak.datavalue.value.id, 'notableWork')
        })
      }
      this.isLoadingProperties = false
      return
    },
  },
  computed: mapState(['PersonalityModule']),
  components: {
    Comment,
    Back,
  },
}
</script>

<style type="scss" scoped>
#main_image {
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
  #head .is-square {
    padding: 0;
    display: inline-block;
  }
}
</style>
