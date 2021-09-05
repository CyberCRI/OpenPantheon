<template>
  <div>
    <main class="section">
      <div class="level">
        <div class="level-left">
          <div class="level-item">
            <b-tabs type="is-boxed" size="is-medium" v-model="activeTab">
              <b-tab-item label="Open Pantheon" value="open">
                <p v-if="count">
                  {{ $t('home.personalities', {count: count, parityWomen: parity, parityMen: 100 - parity}) }}
                </p>
              </b-tab-item>
              <b-tab-item label="My Pantheon" value="personal"> </b-tab-item>
            </b-tabs>
          </div>
        </div>
        <div class="level-right">
          <div class="level-item">
            <b-dropdown multiple aria-role="list">
              <template #trigger>
                <b-button icon-right="menu-down"> {{ $t('home.filter') }}</b-button>
              </template>

              <b-dropdown-item aria-role="listitem">
                <b-field>
                  <b-checkbox v-model="women"> {{ $t('home.women_only') }}</b-checkbox>
                </b-field>
              </b-dropdown-item>

              <b-dropdown-item aria-role="listitem">
                <b-field>
                  <b-checkbox v-model="field" native-value="Arts" ref="Arts" :disabled="hasField">
                    {{ $t('home.arts') }}
                  </b-checkbox>
                </b-field>
              </b-dropdown-item>

              <b-dropdown-item aria-role="listitem">
                <b-field>
                  <b-checkbox
                    v-model="field"
                    native-value="Science"
                    ref="Science"
                    :disabled="hasField"
                  >
                    {{ $t('home.science') }}
                  </b-checkbox>
                </b-field>
              </b-dropdown-item>

              <b-dropdown-item aria-role="listitem">
                <b-field>
                  <b-checkbox
                    v-model="field"
                    native-value="Education"
                    ref="Education"
                    :disabled="hasField"
                  >
                    {{ $t('home.education') }}
                  </b-checkbox>
                </b-field>
              </b-dropdown-item>
            </b-dropdown>
          </div>
          <div class="level-item">
            <b-dropdown class="level-item" v-model="sort" aria-role="list">
              <template v-if="sort == 'recent'" #trigger>
                <b-button label="Most recent" icon-right="menu-down" />
              </template>

              <template v-else-if="sort == 'celebrated'" #trigger>
                <b-button label="Most celebrated" icon-right="menu-down" />
              </template>

              <template v-else #trigger>
                <b-button label="Oldest" icon-right="menu-down" />
              </template>

              <b-dropdown-item value="recent" aria-role="listitem">
                <div class="media">
                  <div class="media-content">
                    <h3>{{ $t('home.recent') }}</h3>
                  </div>
                </div>
              </b-dropdown-item>

              <b-dropdown-item value="celebrated" aria-role="listitem">
                <div class="media">
                  <div class="media-content">
                    <h3>{{ $t('home.celebrated') }}</h3>
                  </div>
                </div>
              </b-dropdown-item>

              <b-dropdown-item value="old" aria-role="listitem">
                <div class="media">
                  <div class="media-content">
                    <h3>{{ $t('home.oldest') }}</h3>
                  </div>
                </div>
              </b-dropdown-item>
            </b-dropdown>
          </div>
        </div>
      </div>
      <div class="container">
        <CardList
          :personal="activeTab"
          :women="women"
          :field="0"
          :sort="sort"
          :count="count"
        ></CardList>
      </div>
    </main>
  </div>
</template>

<script>
import CardList from '@/components/CardList.vue'

export default {
  name: 'Home',
  data() {
    return {
      activeTab: 'open',
      women: false,
      field: [],
      sort: null,
      count: null,
      parity: null,
    }
  },
  components: {
    CardList,
  },
  computed: {
    hasField() {
      return this.field.length > 0
    },
  },
  async created() {
    await this.$store.dispatch('getPantheonStats')
    this.count = this.$store.getters.pantheonCount
    this.parity = this.$store.getters.pantheonParity
  },
}
</script>

<style type="scss" scoped></style>
