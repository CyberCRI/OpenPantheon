<template>
  <div>
    <main class="section">
      <div class="columns is-8-desktop">
        <div class="column is-half">
          <b-tabs type="is-boxed" size="is-medium" v-model="activeTab">
            <b-tab-item label="Open Pantheon" value="open">
            	<p v-if="count">{{ count }} personalities - {{ parity }}% Women, {{ 100 - parity }}% Men</p>
						</b-tab-item>
            <b-tab-item label="My Pantheon" value="personal">
            </b-tab-item>
          </b-tabs>
        </div>
        <div class="column is-half is-offset-1">
          <b-dropdown multiple aria-role="list">
            <template #trigger>
              <b-button icon-right="menu-down"> Filter </b-button>
            </template>

            <b-dropdown-item aria-role="listitem">
              <b-field>
                <b-checkbox v-model="women"> Women only </b-checkbox>
              </b-field>
            </b-dropdown-item>

            <b-dropdown-item aria-role="listitem">
              <b-field>
                <b-checkbox v-model="field" native-value="Arts" ref="Arts" :disabled="hasField">
                  Arts
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
                  Science
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
                  Education
                </b-checkbox>
              </b-field>
            </b-dropdown-item>
          </b-dropdown>
          <b-dropdown v-model="sort" aria-role="list">
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
                  <h3>Most recent</h3>
                </div>
              </div>
            </b-dropdown-item>

            <b-dropdown-item value="celebrated" aria-role="listitem">
              <div class="media">
                <div class="media-content">
                  <h3>Most celebrated</h3>
                </div>
              </div>
            </b-dropdown-item>

            <b-dropdown-item value="old" aria-role="listitem">
              <div class="media">
                <div class="media-content">
                  <h3>Oldest</h3>
                </div>
              </div>
            </b-dropdown-item>
          </b-dropdown>
        </div>
      </div>
      <div class="container">
        <CardList :personal="activeTab" :women="women" :field="0" :sort="sort"></CardList>
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

<style type="scss" scoped>

</style>
