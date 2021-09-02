<template>
  <div>
    <figure v-if="data.claims && data.claims.P18" class="image is-square">
      <img
        :src="`https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/${data.claims.P18[0]}`"
      />
    </figure>
    <b-skeleton width=320px height=320px :active="isLoading"></b-skeleton>

    <p v-if="data.labels">{{ data.labels[$i18n.locale] }}</p>
    <b-skeleton size="is-small" :active="isLoading"></b-skeleton>

    <small v-if="data.descriptions">{{ data.descriptions[$i18n.locale] | capitalize({ onlyFirstLetter: true }) }}</small>
    <b-skeleton size="is-small" :active="isLoading"></b-skeleton>

    <br />

    <p v-if="data.claims">
      {{ celebrations }} {{ celebrations | pluralize('Celebration') }}
    </p>
    <b-skeleton size="is-medium" :active="isLoading"></b-skeleton>

    <p v-if="properties.notableWork">Notable Work : {{ properties.notableWork }}</p>
    <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

    <p v-if="properties.spouse">Spouse : {{ properties.spouse }}</p>
    <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

    <p v-if="properties.children">Children : {{ properties.children }}</p>
    <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

    <p v-if="properties.dob">Born : {{ properties.dob }}, {{ properties.pob }}</p>
    <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

    <p v-if="properties.dod">Died : {{ properties.dod }} (aged {{ properties.ageOfDeath }}), {{ properties.pod }}</p>
    <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

<!--     <p v-if="data.claims.P800">Notable Work : {{ data.claims.P800[$i18n.locale] }}</p>
    <p v-if="data.claims.P800">Notable Work : {{ data.claims.P800[$i18n.locale] }}</p>
    <p v-if="data.claims.P800">Notable Work : {{ data.claims.P800[$i18n.locale] }}</p>
    <p v-if="data.claims.P800">Notable Work : {{ data.claims.P800 }}</p> -->
  </div>
</template>

<script>
import wbk from 'wikidata-sdk'
import { mapState } from 'vuex'

export default {
  name: 'Details',
  data() {
    return {
      data: {},
      properties: {
      	spouse: '',
      	notableWork: '',
      	children: '',
      	dob: '',
      	dod: '',
      	pob: '',
      	pod: '',
      	ageOfDeath: ''
      },
      celebrations: null,
      isLoading: true,
      isLoadingProperties: true
    }
  },
  async created() {
    await this.$store.dispatch('fetchPersonality', this.$router.currentRoute.params.id)
    const personality = this.PersonalityModule.personality
    this.celebrations = personality.comments.length
    const url = wbk.getEntities({
      ids: personality.wikipedia_id,
      languages: [this.$i18n.locale],
    })
    await fetch(url, {
      headers: {
        'Accept-Encoding': 'gzip',
      },
    })
      .then((res) => res.json())
      .then(wbk.parse.wb.entities)
      .then((entities) => {
        this.data = entities[personality.wikipedia_id]
        this.isLoading = false
        this.getProperties()
        console.log(this.data)
      })
  },
  methods: {
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
          console.log(entities)
        })
    },
    dateFormatter(str) {
    	const formatter = new Intl.DateTimeFormat(this.$i18n.locale, {
    		year: 'numeric', month: 'long', day: 'numeric'
    	})
    	return formatter.format(new Date(str))
    },
    ageAtDeath(dob, dod) {
    	return new Date(new Date(dod) - new Date(dob).getTime()).getFullYear() - 1970
    },
    async getProperties() {
    	if (this.data.claims.P569) this.properties.dob = this.dateFormatter(this.data.claims.P569)
    	if (this.data.claims.P570) this.properties.dod = this.dateFormatter(this.data.claims.P570)
    	if (this.data.claims.P570) this.properties.ageOfDeath = this.ageAtDeath(this.data.claims.P569, this.data.claims.P570)
    	if (this.data.claims.P26) await this.getSimpleProperty(this.data.claims.P26, 'spouse')
        if (this.data.claims.P800) await this.getSimpleProperty(this.data.claims.P800, 'notableWork')
        if (this.data.claims.P19) await this.getSimpleProperty(this.data.claims.P19, 'pob')
        if (this.data.claims.P20) await this.getSimpleProperty(this.data.claims.P20, 'pod')
        // if (this.data.claims.P40) this.getProperty(this.data.claims.P40, 'children')
    	this.isLoadingProperties = false
    	return
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
