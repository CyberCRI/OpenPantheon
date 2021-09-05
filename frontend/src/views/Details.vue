<template>
  <section class="section container box">

    <!-- Head  -->

    <div class="columns is-align-items-self-end">
      <div class="section column is-3">
        <figure v-if="data.claims && data.claims.P18" class="image is-1by1" id="main_image_container">
          <img id="main_image"
            :src="`https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/${data.claims.P18[0].mainsnak.datavalue.value}`"
          />
        </figure>
        <b-skeleton width="320px" height="320px" :active="isLoading"></b-skeleton>
      </div>

      <div class="section column is-3">
        <div class="container pb-3">
          <h1 v-if="data.labels" class="title is-spaced">{{ data.labels[$i18n.locale].value }}</h1>
          <b-skeleton size="is-small" :active="isLoading"></b-skeleton>

          <h2 v-if="data.descriptions" class="subtitle is-6">
            {{ data.descriptions[$i18n.locale].value | capitalize({ onlyFirstLetter: true }) }}
          </h2>
          <b-skeleton size="is-small" :active="isLoading"></b-skeleton>

          <small v-if="data.claims"
            >{{ celebrations }} {{ celebrations | pluralize('Celebration') }}</small
          >
          <b-skeleton size="is-medium" :active="isLoading"></b-skeleton>
        </div>

        <router-link
          :to="{ path: `/celebrate?q=${personality.wikipedia_id}&n=${data.labels[$i18n.locale].value}` }"
          class="button is-medium has-text-small is-primary is-mobile"
          v-if="!isLoading"
          ><strong class="is-size-6 mx-6">Celebrate</strong></router-link
        >
      </div>

      <div class="section column is-3">
        <button
          @click="socialModal"
          class="button is-medium has-text-small is-mobile"
          v-if="!isLoading"
          ><strong class="is-size-6 mx-6">Share profile</strong></button
        >
      </div>
      <div class="section column is-3">
        <a
          :href="wikiLink"
          class="button is-medium has-text-small is-mobile"
          v-if="!isLoading && wikiLink"
          ><strong class="is-size-6 mx-6">Visit Wikipedia</strong></a
        >
      </div>
    </div>

    <!-- Bio and factsheet  -->

    <div id="bio" class="section">
      <h2 id="title" class="title is-4">About</h2>
      <div class="columns is-align-items-self-start">
        <p class="has-text-justified column is-6">
          Lorem ipsum dolor, sit amet consectetur adipisicing, elit. Assumenda eligendi est dicta
          odio veniam explicabo asperiores ab, deserunt necessitatibus, quo tempore a quidem
          distinctio eos nostrum placeat saepe repellat dolore! Lorem, ipsum dolor sit amet
          consectetur adipisicing elit. Itaque similique, voluptate veniam eius praesentium laborum
          sint, officia cupiditate necessitatibus dolores ducimus. Fuga, rerum. Quis, saepe numquam
          modi, voluptatibus nam voluptate. Lorem ipsum dolor sit amet consectetur, adipisicing
          elit. Mollitia ipsa dolores temporibus quas qui eligendi pariatur, ipsum facilis porro,
          aut excepturi illo, deleniti, error doloribus. Eos debitis, consectetur provident eaque.
        </p>
        <div id="factsheet" class="column is-6">
          <p v-if="properties.notableWork[0]">
            <span class="has-text-weight-bold">Notable Work :</span>
            {{ properties.notableWork.join(', ') }}
          </p>
          <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

          <p v-if="properties.marriages[0]">
            <span class="has-text-weight-bold">Spouse(s) :</span>
            <span v-for="(marriage, index) in properties.marriages" :key="index">
              {{ marriage.spouse }} (m. {{ marriage.start }};
              {{ marriage.reason == 'death' ? 'died' : '' }} {{ marriage.end }})
            </span>
          </p>
          <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

          <p v-if="properties.children[0]">
            <span class="has-text-weight-bold">Children :</span> {{ properties.children.join(', ') }}
          </p>
          <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

          <p v-if="properties.dateOfBirth && properties.placeOfBirth">
            <span class="has-text-weight-bold">Born :</span> {{ properties.dateOfBirth }},
            {{ properties.placeOfBirth }}
          </p>
          <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>

          <p v-if="properties.dateOfDeath && properties.placeOfDeath">
            <span class="has-text-weight-bold">Died :</span> {{ properties.dateOfDeath }} (aged
            {{ properties.ageOfDeath }}),
            {{ properties.placeOfDeath }}
          </p>
          <b-skeleton size="is-medium" :active="isLoadingProperties"></b-skeleton>
        </div>
      </div>
    </div>

    <hr />

    <!-- Comments  -->

    <div class="section" v-if="personality.comments">
      <h2 id="title" class="title is-4" v-if="data.claims">{{ celebrations }} {{ celebrations | pluralize('Celebration') }}</h2>
      <div class="columns is-multiline is-centered">
        <Comment class="column is-6-desktop" v-for="(comment, index) in personality.comments.slice(0, 6)" :key="index" :comment=comment />
      </div>
      <div class="container has-text-centered">
        <button
         @click="commentModal"
         class="button is-medium has-text-small is-primary is-mobile"
         v-if="!isLoading"
         ><strong class="is-size-7 mx-6">Show all celebrations</strong></button>
      </div>
    </div>

  </section>
</template>

<script>
import wbk from 'wikidata-sdk'
import SocialModal from '@/components/SocialModal.vue'
import CommentsModal from '@/components/CommentsModal.vue'
import Comment from '@/components/Comment.vue'
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
        placeOfDeath: '',
        ageOfDeath: '',
      },
      personality: {},
      exintro: '',
      celebrations: null,
      isLoading: true,
      isLoadingProperties: true,
      wikiLink: null
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
      .then((res) => {
        this.data = res.entities[this.personality.wikipedia_id]
        console.log(res)
        this.wikiLink = wbk.getSitelinkUrl(
          res.entities[this.personality.wikipedia_id].sitelinks[this.$i18n.locale + 'wiki'].site,
         res.entities[this.personality.wikipedia_id].sitelinks[this.$i18n.locale + 'wiki'].title
         )
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
      console.log(id)
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
      console.log('ok', formatter.format(new Date(str)))
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
      if (this.data.claims.P19)
        await this.getSimpleProperty(
          this.data.claims.P19[0].mainsnak.datavalue.value.id,
          'placeOfBirth'
        )
      if (this.data.claims.P20)
        await this.getSimpleProperty(
          this.data.claims.P20[0].mainsnak.datavalue.value.id,
          'placeOfDeath'
        )
      if (birth) this.properties.dateOfBirth = this.dateFormatter(birth)
      if (death) this.properties.dateOfDeath = this.dateFormatter(death)
      if (this.properties.dateOfDeath) this.properties.ageOfDeath = this.ageAtDeath(birth, death)
      if (this.data.claims.P26) {
        for (const spouse of this.data.claims.P26)
          await this.getArrayOfProperties(spouse.mainsnak.datavalue.value.id, 'spouses')
        this.data.claims.P26.forEach((spouse, index) => {
          this.properties.marriages.push({
            spouse: this.properties.spouses[index],
            start: wbk
              .wikibaseTimeToDateObject(spouse.qualifiers.P580[0].datavalue.value.time)
              .getFullYear(),
            end: wbk
              .wikibaseTimeToDateObject(spouse.qualifiers.P582[0].datavalue.value.time)
              .getFullYear(),
            reason:
              spouse.qualifiers.P1534 &&
              spouse.qualifiers.P1534[0].datavalue.value.id == 'Q24037741'
                ? 'death'
                : '',
            order: spouse.qualifiers.P1545 ? spouse.qualifiers.P1545[0].datavalue.value : 0,
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

      // if (this.data.claims.P40) this.getProperty(this.data.claims.P40, 'children')
      this.isLoadingProperties = false
      return
    },
  },
  computed: mapState(['PersonalityModule']),
  components: {
    Comment
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

</style>
