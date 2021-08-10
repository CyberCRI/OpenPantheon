<template>
    <section class="section">
        <div class="columns is-multiline">
            <Card
                class="column is-one-quarter"
                v-for="personality in mode"
                :key="personality.id"
                :personality="personality"
            ></Card>
        </div>
        <b-pagination
            :total="modeTotal || PersonalityModule.total"
            v-model="page"
            order="is-centered"
            rounded
            :per-page="perPage"
            icon-prev="chevron-left"
            icon-next="chevron-right"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
        />
    </section>
</template>

<script>
import Card from '@/components/Card.vue'
import { mapState } from 'vuex'
export default {
    name: 'CardList',
    data() {
        return {
            perPage: 16,
            page: 1,
            modeTotal: undefined
        }
    },
    props: {
        personal: String,
        id: Number,
        randomSelection: Boolean,
        extended: Boolean,
        filter: String,
        isWomen: Boolean,
        field: String,
        sort: String,
    },
    components: {
        Card,
    },
    computed: {
    	mode() {
    		let filteredTab
    		if (this.personal == 'open' && !this.filter && !this.isWomen && !this.field && !this.sort)
    		{
    			this.modeTotal = undefined
    			return this.PersonalityModule.personalities
    		}
    		else {
    			filteredTab = this.PersonalityModule.personalities.filter((item) => item.name == "Louinis Boudaa")
    			this.modeTotal = filteredTab.length
    			return filteredTab
    		}
    	},
    	...mapState(['PersonalityModule'])
	},
    watch: {
        page: {
            handler() {
                this.$store.dispatch('fetchAll', {
                    perPage: this.perPage,
                    page: this.page,
                })
            },
            immediate: true,
        },
    },
}
</script>

<style type="scss" scoped>

</style>
