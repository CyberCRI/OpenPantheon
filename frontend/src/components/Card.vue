<template>
  <router-link :to="{ name: 'Details', params: { id: personality.id } }">
    <div class="card" v-if="data">
      <div class="card-image">
        <figure class="image">
          <img
            :src="
              data.claims.P18
                ? `https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/${data.claims.P18[0]}`
                : 'https://bulma.io/images/placeholders/480x480.png'
            "
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <p>{{ data.labels[$i18n.locale] }}</p>
          <small>{{
            data.descriptions[$i18n.locale] | capitalize({ onlyFirstLetter: true }) | truncate(35)
          }}</small>
          <br />
          <p>
            {{ personality.comments.length }}
            {{ personality.comments.length | pluralize('Celebration') }}
          </p>
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
  },
}
</script>

<style type="scss" scoped>
.image {
  max-height: 320px;
}

img {
  max-height: 420px;
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
