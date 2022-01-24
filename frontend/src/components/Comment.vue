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
  <div class="comment">
    <article class="media">
      <figure class="media-left is-hidden-mobile">
        <router-link v-if="user" :to="{ path: `/pantheon/${user.id}` }"
          ><div class="avatar">
            {{ (user.first_name[0] + user.last_name[0]) | uppercase }}
          </div></router-link
        >
      </figure>
      <div class="media-content has-background-light py-4 px-5 mb-5">
        <div class="container">
          <div class="is-flex is-justify-content-space-between">
            <div>
              <h1 class="title is-6" v-if="user">
                {{ user.first_name }} {{ user.last_name }}<slot></slot>
              </h1>
              <h2 class="subtitle is-6 has-text-grey-light mb-2" v-if="user">
                {{ user.job }}
              </h2>
            </div>
            <div>
              {{ timestamp }}
              <b-dropdown aria-role="list" position="is-bottom-left">
                <template #trigger>
                  <b-icon icon="dots-horizontal" type="is-primary"></b-icon>
                </template>
                <router-link v-if="user" :to="{ path: `/pantheon/${user.id}` }"
                  ><b-dropdown-item aria-role="listitem">{{
                    $t('comment.see_user_pantheon')
                  }}</b-dropdown-item></router-link
                >
                <router-link v-if="user" :to="{ path: `/contact?q=${reportText}` }">
                  <b-dropdown-item aria-role="listitem">{{
                    $t('comment.report_comment')
                  }}</b-dropdown-item></router-link
                >
                <b-dropdown-item
                  aria-role="listitem"
                  @click="confirmDelete"
                  v-if="
                    currentUser &&
                    (comment.author_id === currentUser.id || currentUser.is_superuser)
                  "
                  >{{ $t('comment.delete_comment') }}</b-dropdown-item
                >
              </b-dropdown>
            </div>
          </div>
          <p>
            {{ comment.text }}
          </p>
        </div>
        <ul class="mt-5" v-if="comment.fluff[0].link">
          <li v-for="(ref, index) in comment.fluff" :key="index">
            <a :href="ref.link" class="has-text-dark is-underlined">{{ ref.name }}</a>
            <b-icon icon="open-in-new" size="is-small" type="is-primary"> </b-icon>
          </li>
        </ul>
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
      currentUser: null,
    }
  },
  props: {
    comment: Object,
  },
  methods: {
    ...mapActions(['getUserById', 'deleteComment']),
    confirmDelete() {
      this.$buefy.dialog.confirm({
        title: this.$t('comment.delete_title'),
        message: this.$t('comment.delete_message'),
        confirmText: this.$t('comment.delete_button'),
        cancelText: this.$t('comment.cancel_button'),
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () =>
          this.deleteComment(this.comment.id)
            .then(() => {
              this.$el.parentNode.removeChild(this.$el)
              this.$router.go(-1)
            })
            .catch(() => {
              this.$buefy.toast.open({
                duration: 5000,
                message: this.$t('toast.credentials'),
                type: 'is-danger',
              })
            }),
      })
    },
  },
  async created() {
    await this.getUserById(this.comment.author_id)
    this.user = this.AuthModule.userDetails
    this.currentUser = this.AuthModule.currentUserDetails
  },
  computed: {
    ...mapState(['AuthModule']),
    timestamp: function () {
      return moment(this.comment.time_created).fromNow(true)
    },
    reportText: function () {
      return this.$t('comment.report_default', {
        user: this.user.first_name + ' ' + this.user.last_name,
        path: window.location,
      })
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
