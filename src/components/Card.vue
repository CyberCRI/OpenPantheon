<template>
    <router-link :to="{ name: 'Details', params: { id: personality.id } }">
        <div class="card">
            <div class="card-image">
                <figure class="image is-square">
                    <img :src="personality.image" alt="Placeholder image" />
                </figure>
            </div>
            <div class="card-content">
                <div class="content">
                    <p>{{ personality.name }}</p>
                    <p>{{ personality.job }}</p>
                    <a href="#">{{ personality.comments.length }} Celebrations</a>
                    <slot></slot>
                </div>
            </div>
        </div>
    </router-link>
</template>

<script>
export default {
    name: 'Card',
    data() {
        return {}
    },
    props: {
        extended: Boolean,
        personality: Object,
    },
}
</script>

<style type="scss" scoped></style>
