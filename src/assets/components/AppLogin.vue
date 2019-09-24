<template>
<div id="test">
    <input v-model="message" required :placeholder="text" :type="types" title=""/>
    <span class="hello"/>
</div>
</template>

<script>
export default {
    props: {
        types: String,
        text: String,
    },
    data:() => {
        return{
            message: "",
        }
    }
}
</script>

<style lang="scss">
@import '@/assets/scss/AppLogin.model.scss'
</style>
