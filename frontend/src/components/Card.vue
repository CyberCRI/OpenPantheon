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
  <router-link :to="{ name: 'Details', params: { id: personality.id } }">
    <div class="card" v-if="data">
      <div class="card-image">
        <figure class="image is-square">
          <img
            v-if="!isLoading && data"
            :src="
              data.claims.P18
                ? `https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/${data.claims.P18[0]}&width=320`
                : './img/silhouette.png'
            "
            :style="{ 'background-color': data.claims.P18 ? '' : '#202137' }"
            alt="Placeholder image"
          />
          <b-skeleton size="is-large" height="320px" :active="isLoading"></b-skeleton>
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <p class="mb-0 is-size-6" v-if="!isLoading">{{ data.labels[$i18n.locale] }}</p>
          <b-skeleton size="is-large" :active="isLoading"></b-skeleton>
          <p v-if="!isLoading" class="has-text-grey is-size-7 mb-2">
            {{
              data.descriptions[$i18n.locale] | capitalize({ onlyFirstLetter: true }) | truncate(30)
            }}
          </p>
          <b-skeleton size="is-small" :active="isLoading"></b-skeleton>
          <p v-if="!isLoading">
            {{ personality.comments.length }}
            {{ personality.comments.length | pluralize('celebration') }}
          </p>
          <b-skeleton width="120px" :active="isLoading"></b-skeleton>
          <slot class="my-5"></slot>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'Card',
  data() {
    return {}
  },
  props: {
    extended: Boolean,
    personality: Object,
    data: Object,
    isLoading: Boolean,
  },
  beforeUpdate() {
    if (!this.isLoading && !this.data.labels[this.$i18n.locale])
      this.data.labels[this.$i18n.locale] = this.$t('misc.name_unavailable')
    if (!this.isLoading && !this.data.descriptions[this.$i18n.locale])
      this.data.descriptions[this.$i18n.locale] = this.$t('misc.desc_unavailable')
  },
}
</script>

<style lang="scss" scoped>
.image {
  max-height: 320px;
}

img {
  max-height: 420px;
  object-fit: cover;
}

.card-image {
  display: block;
  position: relative;
  height: 320px;
  z-index: 0;
}

.card-content {
  background-color: white;
  z-index: 1;
  position: relative;
}
</style>
