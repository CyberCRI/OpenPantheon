<template>
  <b-field label="Find a personality">
    <b-autocomplete
      :data="data"
      placeholder="Search someone through wikpedia..."
      field="title"
      :value="name"
      :loading="isFetching"
      @typing="getAsyncData"
      @select="fetchWikidata"
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
                  ? `https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/${props.option.claims.P18[0]}`
                  : 'https://bulma.io/images/placeholders/480x480.png'
              "
            />
          </div>
          <div class="media-content">
            {{ props.option.labels[$i18n.locale] }}
            <br />
            <small>
              {{ props.option.descriptions[$i18n.locale] }}
            </small>
          </div>
          <div class="media-right">
            <p v-if="props.option.celebrations > 0">
              {{ props.option.celebrations }} celebration(s)
            </p>
            <p v-else>Add to the pantheon</p>
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
  name: 'Celebrate',
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
          console.log('why', this.data)
        })

      if (!name.length) {
        this.data = []
        return
      }
      this.isFetching = true
      console.log('ok', this.data)
    }, 250),
    fetchWikidata(option) {
      this.name = option.labels[this.$i18n.locale]
      this.$emit('personalitySelected', option)
    },
    inPantheon(id, entity) {
      return this.$store
        .dispatch('fetchPersonalityByWiki', id)
        .then((response) => {
          console.log('proof', response)
          if (!response) entity.celebrations = 0
          else entity.celebrations = response.comments.length
        })
        .catch((error) => console.log(error))
    },
  },
}
</script>
