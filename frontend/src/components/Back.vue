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

<style type="scss" scoped>
#back {
  cursor: pointer;
}
</style>
