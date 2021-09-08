<template>
  <div class="comment">
    <article class="media">
      <figure class="media-left">
        <router-link v-if="user" :to="{ path: `/pantheon/${user.id}` }"
          ><div class="avatar">
            {{ (user.first_name[0] + user.last_name[0]) | uppercase }}
          </div></router-link
        >
      </figure>
      <div class="media-content has-background-light py-5 px-5 my-5 mx-2">
        <div class="container">
          <div class="is-flex is-justify-content-space-between">
            <div>
              <h1 class="title is-6" v-if="user">{{ user.first_name }} {{ user.last_name }}</h1>
              <h2 class="subtitle is-6 has-text-grey-light" v-if="user">
                {{ user.job }}
              </h2>
            </div>
            <div>
              {{ timestamp }}
            </div>
          </div>
          <p>
            {{ comment.text }}
          </p>
        </div>
        <ul>
          <li v-for="(ref, index) in references" :key="index">
            <a :href="ref.link">{{ ref.name }}</a>
          </li>
        </ul>
      </div>
      <div class="media-right">
        <!--           <button class="delete"></button>
 -->
      </div>
    </article>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import moment from 'moment'

moment.locale('en', {
  relativeTime: {
    future: 'in %s',
    past: '%s ago',
    s: 'seconds',
    ss: '%ss',
    m: '1m',
    mm: '%dm',
    h: '1h',
    hh: '%dh',
    d: '1d',
    dd: '%dd',
    M: '1M',
    MM: '%dM',
    y: '1Y',
    yy: '%dY',
  },
})

export default {
  name: 'Comment',
  data() {
    return {
      user: null,
      references: [],
    }
  },
  props: {
    comment: Object,
  },
  methods: mapActions(['getUserById']),
  async created() {
    if (this.comment.fluff) {
      const tab = this.comment.fluff.split('~')
      tab.forEach((ref) => {
        const tmp = ref.split('|')
        this.references.push({ name: tmp[0], link: tmp[1] })
      })
    }
    await this.getUserById(this.comment.author_id)
    this.user = this.AuthModule.userDetails
  },
  computed: {
    ...mapState(['AuthModule']),
    timestamp: function () {
      return moment(this.comment.time_created).fromNow(true)
    },
  },
}
</script>

<style scoped lang="scss">
.comment {
  overflow-wrap: anywhere;
}
.media-content {
  border-radius: 10px;
}
</style>
