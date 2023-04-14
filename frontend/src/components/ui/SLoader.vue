<template>
  <div class="loader">
    <ion-spinner></ion-spinner>
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