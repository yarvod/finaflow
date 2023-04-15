<template>
  <BaseLayout head>
    <template #head>
      <ion-card-title>Категории</ion-card-title>
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
  name: "CategoriesList",
  components: {
    BaseLayout,
    IonCardTitle,
    ComingSoon,
  }
}
</script>

<style scoped>

</style>