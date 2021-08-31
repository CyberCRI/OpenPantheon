<template>
  <div>
    <figure class="image is-square">
      <img
        :src="
          data.claims.P18
            ? `https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/${data.claims.P18[0]}`
            : 'https://bulma.io/images/placeholders/480x480.png'
        "
        alt="Placeholder image"
      />
    </figure>
    <!--         <p v-for="(trait, index) in PersonalityModule.personality" :key="index">{{ trait }}</p>
 -->
    <p>{{ data.labels[$i18n.locale] }}</p>
    <small>{{ data.descriptions[$i18n.locale] | capitalize({ onlyFirstLetter: true }) }}</small>
    <br />
    <p>
      {{ personality.comments.length }} {{ personality.comments.length | pluralize('Celebration') }}
    </p>

    <p v-if="properties.notableWork">Notable Work : {{ properties.notableWork[$i18n.locale] }}</p>
    <p v-if="properties.spouse">Spouse : {{ properties.spouse[$i18n.locale] }}</p>
    <p v-if="data.claims.P800">Notable Work : {{ data.claims.P800[$i18n.locale] }}</p>
    <p v-if="data.claims.P800">Notable Work : {{ data.claims.P800[$i18n.locale] }}</p>
    <p v-if="data.claims.P800">Notable Work : {{ data.claims.P800[$i18n.locale] }}</p>
    <p v-if="data.claims.P800">Notable Work : {{ data.claims.P800 }}</p>
  </div>
</template>

<script>
import wbk from 'wikidata-sdk'
import { mapState } from 'vuex'

export default {
  name: 'Details',
  props: ['id'],
  data() {
    return {
      data: {},
      personality: {},
      properties: {},
    }
  },
  created() {
    this.$store.dispatch('fetchPersonality', this.id)
    this.personality = this.PersonalityModule.personality
    const url = wbk.getEntities({
      ids: this.personality.wikipedia_id,
      languages: ['en', 'fr'],
    })
    fetch(url, {
      headers: {
        'Accept-Encoding': 'gzip',
      },
    })
      .then((res) => res.json())
      .then(wbk.parse.wb.entities)
      .then((entities) => {
        this.data = entities[this.personality.wikipedia_id]
        this.getProperty(this.data.claims.P26, 'spouse')
        this.getProperty(this.data.claims.P800, 'notableWork')
        console.log(this.data)
      })
  },
  methods: {
    getProperty(id, propertyName) {
      const url = wbk.getEntities({
        ids: id,
        languages: ['en', 'fr'],
      })
      fetch(url, {
        headers: {
          'Accept-Encoding': 'gzip',
        },
      })
        .then((res) => res.json())
        .then(wbk.parse.wb.entities)
        .then((entities) => {
          this.properties[propertyName] = entities[id].labels
          console.log(entities[id])
        })
    },
  },
  computed: mapState(['PersonalityModule']),
}
</script>

<style type="scss" scoped>
.image {
  max-height: 320px;
  max-width: 320px;
  padding-top: 30%;
}

img {
  max-height: 420px;
  max-width: 420px;
}
</style>
