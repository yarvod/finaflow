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
          <h5 class="emptyText">
            У вас еще нет операции за <span class="date">{{ date }}</span>
          </h5>
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
  props: {
    date: {
      type: String,
      default: "выбранный период",
    }
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

.emptyText {
  font-weight: lighter;
  text-align: center;
}

.date {
  font-weight: bolder;
}

</style>