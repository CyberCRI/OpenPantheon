<template>
    <div>
        <TopBar />
        <router-view :key="$route.fullPath"/> <!--  Ensures component gets reloaded on pagination -->
    </div>
</template>

<script>
import TopBar from '@/components/TopBar'

export default {
    name: 'root',
    components: { TopBar },
}
</script>

<style type="scss">
	body {
		background: #FCFCFD;
	}
</style>