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

<style type="scss" scoped>
h1,
h2,
h3,
small {
  text-align: center;
}
</style>
