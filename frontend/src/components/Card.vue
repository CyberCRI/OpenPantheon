<template>
  <router-link :to="{ name: 'Details', params: { id: personality.id } }">
    <div class="card">
      <div class="card-image">
        <figure class="image">
          <img
            v-if="!isLoading && data"
            :src="
              data.claims.P18
                ? `https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/${data.claims.P18[0]}`
                : 'https://bulma.io/images/placeholders/480x480.png'
            "
            alt="Placeholder image"
          />
          <b-skeleton size="is-large" height="320px" :active="isLoading"></b-skeleton>
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <p v-if="!isLoading">{{ data.labels[$i18n.locale] }}</p>
          <b-skeleton size="is-large" :active="isLoading"></b-skeleton>
          <small v-if="!isLoading">{{
            data.descriptions[$i18n.locale] | capitalize({ onlyFirstLetter: true }) | truncate(30)
          }}</small>
          <b-skeleton size="is-small" :active="isLoading"></b-skeleton>
          <br />
          <p v-if="!isLoading">
            {{ personality.comments.length }}
            {{ personality.comments.length | pluralize('Celebration') }}
          </p>
          <b-skeleton width="120px" :active="isLoading"></b-skeleton>
          <slot></slot>
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
}
</script>

<style type="scss" scoped>
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
