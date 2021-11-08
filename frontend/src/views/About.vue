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
  <section class="section">
    <div class="container section box content px-6 py-6 has-text-justified">
      <div class="section">
        <h1 class="title mb-6 pb-6">{{ $t('about.main_title') }}</h1>

        <strong>{{ $t('about.first_step') }}</strong>
        <p>
          {{ $t('about.first_step_paragraph') }}
        </p>

        <strong>{{ $t('about.second_step') }}</strong>
        <p>
          {{ $t('about.second_step_paragraph') }}
        </p>
      </div>
      <div class="section">
        <h3 class="subtitle">{{ $t('about.first_section_title') }}</h3>
        <p>
          {{ $t('about.first_section_first_paragraph') }}
        </p>

        <p>
          {{ $t('about.first_section_second_paragraph') }}
        </p>

        <p>
          {{ $t('about.first_section_third_paragraph') }}
        </p>

        <p>
          {{ $t('about.first_section_fourth_paragraph') }}
        </p>
        <p>
          {{ $t('about.first_section_fifth_paragraph') }}
        </p>

        <p>
          {{ $t('about.first_section_sixth_paragraph') }}
        </p>

        <small>
          {{ $t('about.first_section_addendum') }}
        </small>
      </div>
      <div class="section">
        <h3 class="subtitle">{{ $t('about.second_section_title') }}</h3>
        <p>
          {{ $t('about.second_section_first_paragraph') }}
        </p>

        <small>
          {{ $t('about.second_section_addendum') }}
        </small>
      </div>
      <div class="section">
        <h3 class="subtitle">{{ $t('about.third_section_title') }}</h3>

        <p>
          {{ $t('about.third_section_first_paragraph') }}
        </p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'About',
  components: {},
}
</script>

<style lang="scss" scoped>
h1,
h2,
h3,
small {
  text-align: center;
}
</style>
