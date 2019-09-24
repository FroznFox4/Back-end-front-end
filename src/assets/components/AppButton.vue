<template :href="url">
    <div id="mask" class="CustomButton">
        <div class="StyleButton one" @click='ClickTest()' :style="{padding: paddingY+'rem '+ paddingX + 'rem'}"><div class="lable" v-text="text"></div></div>
    </div>
</template>

<script>
const axios = require('axios').default;
const mymodule = require("@/assets/js/ButtonLogin.module.js").default;
export default {
    props:{
        text: String,
        url: String,
        paddingX: String,
        paddingY: String,
        urle: String,
    },
    data:()=>{
        return{
        }
    },
    methods:{
        ClickGet(url){
            axios
                .get(url, {
                    id: 12345,
                    if: 12345,   
                })
                .then(function (response){
                    console.log(response);
                })
                .catch(function (error){
                    console.log(error);
                })
        },
        ClickTest(){
            mymodule.click();
        }
    },
} 
</script>

<style lang="scss">
@import "@/assets/scss/AppButton.module.scss"
</style>