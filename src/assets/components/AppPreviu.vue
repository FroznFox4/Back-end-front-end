<template>
<div id="previu">
    <div class="window">
        <!--
        Video сделать autoplay
        -->
        <video class="video" loop preload="auto" controls>
            <source :src='require("@/assets/imgs/RoyalQuestVideo.mp4")' type='video/mp4'>
        </video>
        <div class="text" :text="govno">
        </div>
        <div class="login">
            <AppLogin
                types="email"
                text="Username"
            />
            <AppLogin
                types="password"
                text="Password"
            />
            <AppButton 
                url="http://localhost:8000/api/api-create/"
                text="Log In"
                paddingX= 6
                paddingY= 0.5
            />
        </div>
    </div>
</div>
</template>

<script>
import AppLogin from "@/assets/components/AppLogin"
import AppButton from "@/assets/components/AppButton"
export default{
    data(){
        return{
            govno:"Проснувшись однажды утром после беспокойного сна, Грегор Замза обнаружил, что он у себя в постели превратился в страшное насекомое. Лежа на панцирнотвердой спине, он видел, стоило ему приподнять голову, свой коричневый, выпуклый, разделенный дугообразными чешуйками живот, на верхушке которого еле держалось готовое вот-вот окончательно сползти одеяло. Его многочисленные, убого тонкие по сравнению с остальным телом ножки беспомощно копошились у него перед глазами. «Что со мной случилось?» – подумал он. Это не было сном. Его комната, настоящая, разве что слишком маленькая, но обычная комната, мирно покоилась в своих четырех хорошо знакомых стенах. Над столом, где были разложены распакованные образцы сукон – Замза был коммивояжером, – висел портрет, который он недавно вырезал из иллюстрированного журнала и вставил в красивую золоченую рамку."
        }
    },
    components:{
        AppLogin,
        AppButton,
    }
}
</script>

<style lang = "scss">
@import "@/assets/scss/AppPreviu.model.scss"
</style>

