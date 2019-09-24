<template>
    <div id="test">
        <div class = "flex">
            <div class ="card">
                <i data-feather="circle"></i>
                <img class ="imgstop" src="https://upload.wikimedia.org/wikipedia/commons/f/f1/Vue.png"/>
                <div class = "text">
                    Hello
                </div>
                <div class = "textfields">
                    <img class= "imgs" src="@/assets/scss/imgs/user.png"/>
                    <input class = "inputing" type="email" placeholder="Username" size="10"/>
                </div>
                <div class = "textfields">
                    <img class= "imgs" src="@/assets/scss/imgs/user.png"/>
                    <input class = "inputing" type="password" placeholder="Password" size="10"/>
                </div>
                <div class = "but mb-base">
                    <button :style="{'background-color': bool ? 'green' : 'cyan'}"  @click="bool = !bool"><p>Sing in</p></button>        
                </div>
                <div>
                    <div class="box box-up"></div>
                    <div class="box box-front"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                bool: true,
                objects: {
                    "border-color": 'green',
                }
            }
        }
    }
</script>

<style lang = "scss">
#test{

    width: 100%;
    height: 100%;
    font-family: 'Chilanka', cursive;

    .flex{  
        background-image: url(http://hq-oboi.ru/photo/siniy_tuman_1920x1200.jpg);
        width: 100%;
        height: 100%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        align-content: center;

        .card{
            width: 400px;
            height: 90%;

            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: center;
            align-items: center;
            align-content: center;
            background:linear-gradient(to bottom, 
                                    rgba(46, 24, 128, 0.178) 0%,
                                    rgba(0, 0, 0, 0.6) 100%);
            .text{
                padding: 20px;
                height: 1rem;
                color: rgba(0, 0, 0, 1);
            }

            .mb-base {
               
                margin-bottom: 2.2rem;

               
            }           
            
            .imgstop{
                width: 20%;
            }
            .textfields{
                opacity: 1;
                display: flex;
                justify-content: space-between;
                width: 300px;
                height: 50px;
                border-bottom: 1px solid;
                border-color: blue;
                $pipl: 300px;

                
                .inputing{
                    display: flex;
                    height: 1em;
                    width: 80%;
                    background: transparent;
                    border: 0px;
                    margin-top: 8%;
                    font-family: 'Chilanka', cursive;
                    outline: none;
                       
                }
                
                .imgs{
                    display: flex;
                    height: 100%-10%;
                    width: 20%-5%;
                    padding: 2px;
                }
            }
            .but{
                margin-top: 20px;
                button{
                    border-radius: 25px;
                    width: 200px;
                    height: 50px;
                    border-color: rgba(0, 0, 255, 0.137);
                    outline: none;
                    p{
                        color: white;
                    }

                }
            }
        }
        
    }
}


</style>

