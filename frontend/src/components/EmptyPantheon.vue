<template>
  <div class="container">
    <Back />
    <div class="box">
      <section class="section is-flex is-flex-direction-column is-align-items-center has-text-centered">
        <img src="img/binoculars.svg" />
        <h1 class="title mb-6 is-size-3">{{ $t('empty_pantheon.title') }}</h1>
        <h2 class="subtitle mb-6 is-size-5">
          {{ $t('empty_pantheon.text') }}
        </h2>
        <router-link :to="{ path: '/celebrate' }" class="button is-primary has-text-dark is-large is-size-4 pb-3">
          <strong class="is-size-6">{{$t('empty_pantheon.celebrate')}}</strong>
        </router-link>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EmptyPantheon',
}
</script>

<style type="scss" scoped>
.button {
  border-radius: 10px;
}
@media (min-width: 1024px) {
  .subtitle {
    width: 50%
  }
}
</style>
