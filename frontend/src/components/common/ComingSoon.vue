<template>
  <div class="centered">
    <transition name="fade" mode="out-in" appear>
      <div>
        <ion-img
          :src="pic"
          class="img"
          alt="Coming soon"
        ></ion-img>
        <ion-text class="centered">
          <h5>
            <slot name="text">Раздел в разработке...</slot>
          </h5>
        </ion-text>
      </div>
    </transition>
  </div>
</template>

<script>
import coming_pic from "@/assets/img/coming_soon.jpg";
import {IonImg, IonText} from "@ionic/vue";

export default {
  name: "ComingSoon",
  components: {
    IonText,
    IonImg,
  },
  data() {
    return {
      pic: coming_pic,
    }
  },
}
</script>

<style lang="scss" scoped>

.centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.img {
  max-width: 350px;
}

h5 {
  font-weight: lighter;
  text-align: center;
}

</style>