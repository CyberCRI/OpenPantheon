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
  <div class="container">
    <div class="box">
      <section
        class="section is-flex is-flex-direction-column is-align-items-center has-text-centered"
      >
        <img src="img/binoculars.svg" />
        <h1 class="title mb-6 is-size-3">{{ $t('empty_pantheon.title') }}</h1>
        <h2 class="subtitle mb-6 is-size-5">
          {{ $t('empty_pantheon.text') }}
        </h2>
        <router-link
          :to="{ path: '/celebrate' }"
          class="button is-primary has-text-dark is-large is-size-4 pb-3"
        >
          <strong class="is-size-6">{{ $t('empty_pantheon.celebrate') }}</strong>
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

<style lang="scss" scoped>
.button {
  border-radius: 10px;
}
@media (min-width: 1024px) {
  .subtitle {
    width: 50%;
  }
}
</style>
