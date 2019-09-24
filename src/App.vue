<template>
    <div id="app">
        <router-view />
    </div>
</template>

<script>
    export default {
    data() {
        return {
        }
    },
    components: {
    },
}
</script>

<style lang="scss">
html{
    display: flex;
    width: 100%;
    height: 100%;
}
body{
    text-align: justify;
    display: flex;
    margin: 0;
    width: 100%;
    height: 100%;
    font-size: 1rem;
    font-family: 'Gayathri', sans-serif;
    -webkit-text-fill-color: rgb(175, 128, 0);
            
}
#app{
    width: 100%;
    height: 100%;
}
.div {
    min-width: 100%;
    min-height: 100%;
    display: flex;
}
</style>
