<template>
  <section class="modal-card is-flex is-flex-direction-column is-align-items-center px-6">
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
