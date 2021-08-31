<template>
    <div>
        <TopBar />
        <router-view />
        <Footer />
        <!--  Ensures component gets reloaded on pagination -->
    </div>
</template>

<script>
import TopBar from '@/components/TopBar'
import Footer from '@/components/Footer'

export default {
    name: 'root',
    components: { TopBar, Footer },
    mounted() {
    	 if (localStorage.Lang !== null)
    	 	this.$i18n.locale = localStorage.Lang; 
    }
}
</script>

<style type="scss">
body {
    background: #fcfcfd;
}
</style>
