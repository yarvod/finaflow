<template>
  <BaseLayout head>
    <template #head>
      <ion-card-title>Категории</ion-card-title>
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
  name: "CategoriesList",
  components: {
    BaseLayout,
    IonCardTitle,
  }
}
</script>

<style scoped>

</style>