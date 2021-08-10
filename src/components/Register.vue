<template>
   <form action="">
        <div class="modal-card" style="width: auto">
            <header class="modal-card-head">
                <p class="modal-card-title">Register</p>
                <button
                    type="button"
                    class="delete"
                    @click="$emit('close')"/>
            </header>
            <section class="modal-card-body">
                <b-field label="Email">
                    <b-input
                        type="email"
                        :value="email"
                        placeholder="Your email"
                        required>
                    </b-input>
                </b-field>

                <b-field label="Password">
                    <b-input
                        type="password"
                        :value="password"
                        password-reveal
                        placeholder="Your password"
                        required>
                    </b-input>
                </b-field>

            </section>
            <footer class="modal-card-foot">
                <b-button
                    label="Close"
                    @click="$emit('close')" />
                <b-button
                    label="Register"
                    type="is-primary" />
            </footer>
        </div>
    </form>
</template>

<script>
export default {
    name: 'Register',
    props: ['email', 'password'],
}
</script>