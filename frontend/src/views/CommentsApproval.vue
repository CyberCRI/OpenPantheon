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
  <div class="box container my-6" v-if="AuthModule.currentUserDetails.is_superuser">
    <div
      class="columns is-multiline"
      v-for="(comment, index) in AuthModule.unapprovedComments"
      :key="index"
    >
      <Comment class="column is-12" :comment="comment"
        >, about <i>{{ personalities[index] }}</i></Comment
      >
      <b-button type="is-primary" @click="approval(comment.id)" expanded>Approve</b-button>
    </div>
  </div>
</template>

<script>
import Comment from '@/components/Comment.vue'
import wbk from 'wikidata-sdk'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'CommentsApproval',
  data() {
    return {
      personalities: [],
    }
  },
  components: {
    Comment,
  },
  async created() {
    await this.getUnapprovedComments()
    this.AuthModule.unapprovedComments.forEach((c) => this.getPersonalityName(c.personality_id))
  },
  methods: {
    ...mapActions(['getUnapprovedComments', 'approveComment']),
    async getPersonalityName(id) {
      await this.$store.dispatch('fetchPersonality', id)
      const personality = this.PersonalityModule.personality
      const url = wbk.getEntities({
        ids: personality.wikipedia_id,
        languages: [this.$i18n.locale],
      })
      return fetch(url, {
        headers: {
          'Accept-Encoding': 'gzip',
        },
      })
        .then((res) => res.json())
        .then((res) => {
          this.personalities.push(
            res.entities[personality.wikipedia_id].labels[this.$i18n.locale].value
          )
        })
    },
    approval(id) {
      this.approveComment(id)
        .then((response) => {
          this.$router.go()
          return response.data
        })
        .catch(() => {
          this.$buefy.toast.open({
            duration: 5000,
            message: this.$t('toast.unknown'),
            type: 'is-danger',
          })
        })
    },
  },
  computed: mapState(['AuthModule', 'PersonalityModule']),
}
</script>
