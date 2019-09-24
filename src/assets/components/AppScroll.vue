<template>
    <div class=imgs @click="click()">
        <div v-show="this.hello===0" class="text text1">
            <img id="one" src="@/assets/imgs/one.jpeg" width="30px" height="30px">
        </div>
        <div v-show="this.hello===1" class="text text2">
            <img id="two" src="@/assets/imgs/two.jpg" width="30px" height="30px">
        </div>
        <div v-show="this.hello===2" class="text text2">
            <img id="three" src="@/assets/imgs/user.png" width="30px" height="30px">
        </div>
    </div>
</template>

<script>
export default {
    data:()=>{
        return{
            hello: 0,
        }
    },
    mounted:{
      preload(){
          const one1 = document.querySelector("#one");
          const two1 = document.querySelector("#two");
          const three1 = document.querySelector("#three");
      }  
    },
    methods:{
        click(){
            if (this.hello===0) {
                this.hello=1
            }else if (this.hello===1){
                this.hello=2
            }else{
                this.hello=0
            }
            console.log(this.hello);
            
        }        
    }    
}
</script>

<style lang="scss">
.imgs{
    display: flex;
    position: absolute;
    .text{
        img{  
            width: 100px;
            height: 100px;
            transition: 1s all ease;
            &:focus{
                width: 500px;
            }
        }
    }
}


</style>