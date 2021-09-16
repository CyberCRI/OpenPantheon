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
  <div class="box container">
    <div class="control is-clearfix my-6">
      <b-input
        type="text"
        icon="magnify"
        autocomplete="off"
        :placeholder="$t('details.search')"
        v-model="search"
      />
    </div>
    <Comment v-for="(comment, index) in filteredList" :key="index" :comment="comment" />
  </div>
</template>

<script>
import Comment from '@/components/Comment.vue'

export default {
  name: 'CommentsModal',
  data() {
    return {
      search: '',
    }
  },
  props: {
    comments: Array,
  },
  components: {
    Comment,
  },
  computed: {
    filteredList() {
      return this.comments.filter((comment) => {
        return comment.text.toLowerCase().includes(this.search.toLowerCase())
      })
    },
  },
}
</script>

<style type="scss" scoped></style>
