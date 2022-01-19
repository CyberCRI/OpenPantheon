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
  <div class="box container my-6" v-if="AuthModule.currentUserDetails.is_superuser">
    <div
      class="columns is-multiline"
      v-for="(comment, index) in AuthModule.unapprovedComments"
      :key="index"
    >
      <Comment class="column is-12" :comment="comment" />
      <b-button type="is-primary" @click="approveComment(comment.id)" expanded>Approve</b-button>
    </div>
  </div>
</template>

<script>
import Comment from '@/components/Comment.vue'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'CommentsApproval',
  components: {
    Comment,
  },
  created() {
    this.getUnapprovedComments()
  },
  methods: {
    ...mapActions(['getUnapprovedComments', 'approveComment']),
  },
  computed: mapState(['AuthModule']),
}
</script>
