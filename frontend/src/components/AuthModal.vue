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
  <section class="modal-card is-flex is-flex-direction-column is-align-items-center">
    <Login v-if="view == 'Login'" @switchView="changeView" @close="$emit('close')" />
    <Register v-else @switchView="changeView" @close="$emit('close')" />
  </section>
</template>

<script>
import Login from '@/components/Login.vue'
import Register from '@/components/Register.vue'

export default {
  name: 'AuthModal',
  data() {
    return {
      view: 'Login',
    }
  },
  methods: {
    changeView() {
      if (this.view == 'Login') this.view = 'Register'
      else this.view = 'Login'
    },
  },
  components: {
    Login,
    Register,
  },
}
</script>
