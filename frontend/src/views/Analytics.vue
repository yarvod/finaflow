<template>
  <BaseLayout head>
    <template #head>
      <ion-card-title>Аналитика</ion-card-title>
    </template>
    <template #body>
      <ComingSoon/>
    </template>
  </BaseLayout>
</template>

<script>
import BaseLayout from "@/components/BaseLayout.vue";
import {IonCardTitle} from "@ionic/vue";
import ComingSoon from "@/components/common/ComingSoon.vue";

export default {
  name: "Analytics.vue",
  components: {
    BaseLayout,
    IonCardTitle,
    ComingSoon,
  }
}
</script>

<style scoped>

</style>