<template>
  <BaseLayout head>
    <template #head>
      <ion-card-title>Аналитика</ion-card-title>
    </template>
    <template #body>
      <h5>В разработке...</h5>
    </template>
  </BaseLayout>
</template>

<script>
import BaseLayout from "@/components/BaseLayout";
import {IonCardTitle} from "@ionic/vue";

export default {
  name: "Analytics.vue",
  components: {
    BaseLayout,
    IonCardTitle,
  }
}
</script>

<style scoped>

</style>