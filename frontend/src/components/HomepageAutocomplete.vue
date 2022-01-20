<!--
OpenPantheon: the pantheon for Education
Copyright (C) 2022 Learning Planet Institute

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
  <b-field>
    <b-autocomplete
      id="autocomplete"
      :data="data"
      :placeholder="$t('wiki.search')"
      field="title"
      icon="magnify"
      :value="name"
      :loading="isFetching"
      @typing="getAsyncData"
      @select="redirect"
      expanded
    >
      <template slot-scope="props">
        <div class="media">
          <div class="media-left">
            <img
              class="image is-48x48"
              width="48"
              height="48"
              :src="
                props.option.claims.P18
                  ? `https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/${props.option.claims.P18[0]}&width=48`
                  : './img/silhouette.png'
              "
              :style="{ 'background-color': props.option.claims.P18 ? '' : '#202137' }"
            />
          </div>
          <div class="media-content">
            {{ props.option.labels[$i18n.locale] }}
          </div>
          <div class="media-right is-hidden-mobile">
            <p v-if="props.option.celebrations > 0">
              {{ props.option.celebrations }} celebration(s)
            </p>
            <p v-else>{{ $t('wiki.add') }}</p>
          </div>
        </div>
      </template>
    </b-autocomplete>
  </b-field>
</template>

<script>
import wbk from 'wikidata-sdk'
import debounce from 'lodash/debounce'

export default {
  name: 'HomepageAutocomplete',
  data() {
    return {
      data: [],
      selected: null,
      isFetching: false,
      name: null,
    }
  },
  methods: {
    getAsyncData: debounce(async function (name) {
      const url = wbk.cirrusSearchPages({
        search: `${name}`,
        haswbstatement: ['P31=Q5'],
        limit: 5,
        profile: 'popular_inclinks_pv',
        sort: 'just_match',
      })
      fetch(url)
        .then((res) => res.json())
        .then(wbk.parse.wb.pagesTitles)
        .then((titles) => {
          const entitiesUrl = wbk.getEntities({
            ids: titles,
            languages: ['en', 'fr'],
          })
          return fetch(entitiesUrl)
        })
        .then((res) => res.json())
        .then(wbk.parse.wb.entities)
        .then(async (entities) => {
          this.data = []
          wbk.simplify.entity(entities)
          Object.keys(entities).forEach(async (key) => {
            const id = entities[key].id
            await this.inPantheon(id, entities[key])
            this.data.push(entities[key])
          })
          this.isFetching = false
        })

      if (!name.length) {
        this.data = []
        return
      }
      this.isFetching = true
    }, 250),
    redirect(option) {
      if (option.celebrations) this.$router.push(`/details/${option.db_id}`)
      else this.$router.push(`/celebrate?q=${option.id}&n=${option.labels[this.$i18n.locale]}`)
    },
    inPantheon(id, entity) {
      return this.$store.dispatch('fetchPersonalityByWiki', id).then((response) => {
        if (!response) entity.celebrations = 0
        else {
          entity.celebrations = response.comments.length
          entity.db_id = response.id
        }
      })
    },
  },
}
</script>

<style scoped>
img {
  object-fit: cover;
}
@media (min-width: 1280px) {
  .field {
    width: 100%;
  }
}
</style>
