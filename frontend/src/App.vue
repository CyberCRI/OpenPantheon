<template>
    <div>
        <TopBar />
        <router-view />
    	<MoreAbout v-if="$route.name !== 'Account' && $route.name !== 'About'" />
        <Footer />
        <!--  Ensures component gets reloaded on pagination -->
    </div>
</template>

<script>
import TopBar from '@/components/TopBar'
import Footer from '@/components/Footer'
import MoreAbout from '@/components/MoreAbout'

export default {
    name: 'root',
    components: { TopBar, Footer, MoreAbout },
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
