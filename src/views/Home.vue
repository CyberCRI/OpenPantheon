<template>
    <div>
        <section class="hero is-halfheight is-primary">
            <div class="hero-body is-flex is-flex-direction-column is-align-items-center">
                <p class="title">Large hero</p>
                <p class="subtitle">Large subtitle</p>
            </div>
        </section>
        <main class="section">
            <div class="columns is-8-desktop">
                <div class="column is-half">
                    <b-tabs type="is-boxed" size="is-medium" v-model="activeTab">
                        <b-tab-item label="Open Pantheon" value="open"> </b-tab-item>
                        <b-tab-item label="My Pantheon" value="personal"> </b-tab-item>
                    </b-tabs>
                </div>
                <div class="column is-half is-offset-1">Second column</div>
            </div>
            <div class="container">
                <CardList :personal="activeTab"></CardList>
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
        }
    },
    components: {
        CardList,
    },
}
</script>
