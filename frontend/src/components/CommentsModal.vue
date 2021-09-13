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
