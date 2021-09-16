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
  <section class="section is-medium has-background-grey-lightest">
    <div class="container mx-6">
      <h1 class="title mb-6">{{ $t('moreabout.title') }}</h1>
      <h2 class="subtitle mb-6">
        {{ $t('moreabout.text') }}
      </h2>
      <router-link :to="{ path: '/about' }" class="button px-5 py-5"
        ><strong>{{ $t('moreabout.button') }}</strong></router-link
      >
    </div>
  </section>
</template>

<script>
export default {
  name: 'MoreAbout',
}
</script>

<style type="scss" scoped>
.section {
  background: #f2f2f3 url('../../public/img/bubble/bubble@1,5x.svg');
  background-repeat: no-repeat;
  background-position-x: right;
  background-position-y: center;
}
.button {
  border-radius: 10px;
  border-width: 0;
}
.subtitle {
  max-width: 50%;
}
</style>
