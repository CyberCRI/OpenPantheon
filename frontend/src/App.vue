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
  <div>
    <TopBar />
    <router-view />
    <MoreAbout v-if="$route.name !== 'Account' && $route.name !== 'About'" />
    <Footer />
    <!--  Ensures component gets reloaded on pagination -->
  </div>
</template>

<script>
import TopBar from '@/components/TopBar'
import Footer from '@/components/Footer'
import MoreAbout from '@/components/MoreAbout'
// eslint-disable-next-line
import styles from '@/assets/sass/override.scss'

export default {
  name: 'root',
  components: { TopBar, Footer, MoreAbout },
  mounted() {
    if (localStorage.Lang) this.$i18n.locale = localStorage.Lang
  },
}
</script>

<style type="scss">
body {
  background: #fcfcfd;
}
</style>
