<template>
  <div class="centered">
    <transition name="fade" mode="out-in" appear>
      <div>
        <ion-img
          :src="pic"
          class="img"
          alt="Alone bird"
        ></ion-img>
        <ion-text class="centered">
          <h5>У вас еще нет ни одной операции :(</h5>
          <slot name="action"></slot>
        </ion-text>
      </div>
    </transition>
  </div>
</template>

<script>
import empty_pic from "@/assets/img/empty.jpeg";
import {IonImg, IonText} from "@ionic/vue";

export default {
  name: "EmptyOperations",
  components: {
    IonText,
    IonImg,
  },
  data() {
    return {
      pic: empty_pic,
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

</style>