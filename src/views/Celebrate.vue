<template>
    <div>
        <form @submit.prevent="celebrate">
            <h3>Name & describe your personality</h3>
            <div class="field">
                <label>Name</label>
                <input
                    v-model="personality.name"
                    type="text"
                    placeholder="Add an personality name"
                />
            </div>

            <div class="field">
                <label>Bio</label>
                <input v-model="personality.bio" type="text" placeholder="Add a bio" />
            </div>

            <h3>Where is the job?</h3>
            <div class="field">
                <label>Job</label>
                <input v-model="personality.job" type="text" placeholder="Add a job" />
            </div>

            <h3>Any comments ?</h3>
            <div class="field">
                <label>Comment</label>
                <input v-model="personality.comments[0]" type="text" placeholder="Add a comment" />
            </div>

            <input type="submit" class="button -fill-gradient" value="Submit" />
        </form>
    </div>
</template>

<script>
export default {
    name: 'Celebrate',
    data() {
        return {
            personality: this.createPersonalityObject(),
        }
    },
    methods: {
        celebrate() {
            this.$store
                .dispatch('createPersonality', this.personality)
                .then(() => {
                    this.$buefy.toast.open({
                        duration: 5000,
                        message: 'Success',
                        type: 'is-success',
                    })
                    this.$router.push({ name: 'Home' })
                    this.personality = this.createPersonalityObject()
                })
                .catch((error) => {
                    this.$buefy.toast.open({
                        duration: 5000,
                        message: "Sorry, we couldn't handle your request",
                        type: 'is-danger',
                    })
                    console.log('There was a problem:', error.response)
                })
        },
        createPersonalityObject() {
            // const user = this.$store.state.user
            return {
                name: '',
                bio: '',
                job: '',
                image: 'https://bulma.io/images/placeholders/480x480.png',
                comments: [],
            }
        },
    },
}
</script>

<style scoped></style>
