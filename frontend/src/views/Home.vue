<template>
  <div>
    <main class="section">
      <div class="level">
        <div class="level-left">
          <div class="level-item">
            <b-tabs type="is-boxed" size="is-medium" v-model="activeTab">
              <b-tab-item :label="$t('home.open')" value="open">
                <p v-if="count">
                  {{
                    $t('home.personalities', {
                      count: count,
                      parityWomen: parity,
                      parityMen: 100 - parity,
                    })
                  }}
                </p>
              </b-tab-item>
              <b-tab-item :label="$t('home.personal')" value="personal"> </b-tab-item>
            </b-tabs>
          </div>
        </div>
        <div class="level-right">
          <div class="level-item">
            <WikiAutocomplete />
          </div>
          <div class="level-item filter_menu">
            <b-dropdown multiple aria-role="list">
              <template #trigger>
                <b-button icon-right="chevron-down" size="is-large" class="filter">
                  {{ $t('home.filter') }}</b-button
                >
              </template>

              <b-dropdown-item aria-role="listitem">
                <b-field>
                  <b-checkbox v-model="women"> {{ $t('home.women_only') }}</b-checkbox>
                </b-field>
              </b-dropdown-item>

              <b-dropdown-item separator>
                <hr />
              </b-dropdown-item>

              <fieldset id="field">
                <b-dropdown-item aria-role="listitem">
                  <b-radio v-model="field" native-value="" ref="" name="field">
                    {{ $t('home.all') }}
                  </b-radio>
                </b-dropdown-item>

                <b-dropdown-item aria-role="listitem">
                  <b-radio v-model="field" native-value="art" ref="Arts" name="field">
                    {{ $t('home.arts') }}
                  </b-radio>
                </b-dropdown-item>

                <b-dropdown-item aria-role="listitem">
                  <b-radio v-model="field" native-value="science" ref="Science" name="field">
                    {{ $t('home.science') }}
                  </b-radio>
                </b-dropdown-item>

                <b-dropdown-item aria-role="listitem">
                  <b-radio v-model="field" native-value="education" ref="Education" name="field">
                    {{ $t('home.education') }}
                  </b-radio>
                </b-dropdown-item>
              </fieldset>

              <b-dropdown-item separator>
                <hr />
              </b-dropdown-item>

              <fieldset id="region">
                <b-dropdown-item aria-role="listitem">
                  <b-radio v-model="region" native-value="" ref="" name="region">
                    {{ $t('home.all') }}
                  </b-radio>
                </b-dropdown-item>

                <b-dropdown-item aria-role="listitem">
                  <b-radio v-model="region" native-value="Africa" ref="Africa" name="region">
                    {{ $t('home.africa') }}
                  </b-radio>
                </b-dropdown-item>

                <b-dropdown-item aria-role="listitem">
                  <b-radio v-model="region" native-value="Asia" ref="Asia" name="region">
                    {{ $t('home.asia') }}
                  </b-radio>
                </b-dropdown-item>

                <b-dropdown-item aria-role="listitem">
                  <b-radio v-model="region" native-value="Europe" ref="Europe" name="region">
                    {{ $t('home.europe') }}
                  </b-radio>
                </b-dropdown-item>

                <b-dropdown-item aria-role="listitem">
                  <b-radio
                    v-model="region"
                    native-value="North America"
                    ref="North America"
                    name="region"
                  >
                    {{ $t('home.northamerica') }}
                  </b-radio>
                </b-dropdown-item>

                <b-dropdown-item aria-role="listitem">
                  <b-radio
                    v-model="region"
                    native-value="Insular Oceania"
                    ref="Insular Oceania"
                    name="region"
                  >
                    {{ $t('home.oceania') }}
                  </b-radio>
                </b-dropdown-item>

                <b-dropdown-item aria-role="listitem">
                  <b-radio
                    v-model="region"
                    native-value="South America"
                    ref="South America"
                    name="region"
                  >
                    {{ $t('home.southamerica') }}
                  </b-radio>
                </b-dropdown-item>
              </fieldset>
            </b-dropdown>
          </div>
          <div class="level-item">
            <b-dropdown class="level-item" v-model="sort" aria-role="list">
              <template v-if="sort == 'recent'" #trigger>
                <b-button
                  class="filter"
                  :label="$t('home.recent')"
                  icon-right="chevron-down"
                  size="is-large"
                />
              </template>

              <template v-else-if="sort == 'celebrated'" #trigger>
                <b-button
                  class="filter"
                  :label="$t('home.celebrated')"
                  icon-right="chevron-down"
                  size="is-large"
                />
              </template>

              <template v-else #trigger>
                <b-button
                  class="filter"
                  :label="$t('home.oldest')"
                  icon-right="chevron-down"
                  size="is-large"
                />
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
        <EmptyPantheon
          v-if="
            activeTab === 'personal' &&
            (!isLoggedIn || !$store.getters.listPersonalitiesCelebrated.length)
          "
        />
        <CardList
          v-else
          :personal="activeTab"
          :women="women"
          :field="field"
          :sort="sort"
          :count="count"
          :region="region"
        ></CardList>
      </div>
    </main>
  </div>
</template>

<script>
import WikiAutocomplete from '@/components/WikiAutocomplete.vue'
import CardList from '@/components/CardList.vue'
import EmptyPantheon from '@/components/EmptyPantheon.vue'

export default {
  name: 'Home',
  data() {
    return {
      activeTab: 'open',
      women: false,
      field: '',
      sort: null,
      count: null,
      parity: null,
      region: '',
    }
  },
  components: {
    CardList,
    WikiAutocomplete,
    EmptyPantheon,
  },
  async created() {
    await this.$store.dispatch('getPantheonStats')
    this.count = this.$store.getters.pantheonCount
    this.parity = this.$store.getters.pantheonParity
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isAuthenticated
    },
  },
}
</script>

<style type="scss" scoped>
.field .label {
  display: none;
}

.filter_menu a.dropdown-item.is-active {
  background-color: white;
  color: #4a4a4a;
}

.filter {
  background-color: #f2f2f3;
  border-width: 0;
  border-radius: 10px;
  font-size: 1rem;
  padding: 1.5rem;
  text-align: left;
}
</style>
