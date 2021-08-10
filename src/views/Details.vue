<template>
    <div>
        <p v-for="(trait, index) in PersonalityModule.personality" :key="index">{{ trait }}</p>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'Details',
    props: ['id'],
    created() {
        this.$store.dispatch('fetchPersonality', this.id)
    },
    computed: mapState(['PersonalityModule']),
}
</script>
