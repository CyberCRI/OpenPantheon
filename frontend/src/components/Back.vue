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
  <div class="level is-mobile">
    <span class="level-left" id="back" @click="$router.back()">
      <b-icon icon="chevron-left" size="is-medium" type="is-primary" class="level-item"> </b-icon>
      <span class="level-item">Back</span>
    </span>
  </div>
</template>

<script>
export default {
  name: 'Back',
}
</script>

<style lang="scss" scoped>
#back {
  cursor: pointer;
}
</style>
