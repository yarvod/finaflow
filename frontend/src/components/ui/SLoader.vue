<template>
  <div class="loader">
    <transition name="fade" mode="out-in" appear>
      <ion-spinner></ion-spinner>
    </transition>
  </div>
</template>

<script>
import {IonSpinner} from "@ionic/vue";

export default {
  name: "SLoader",
  components: {
    IonSpinner,
  },
}
</script>

<style lang="scss" scoped>

.loader {
  display: flex;
  justify-content: center;
  margin: 60px auto;
}

</style>