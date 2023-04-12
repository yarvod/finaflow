<template>
  <BaseLayout head>
    <template #head>
      <h4>Категории</h4>
    </template>
    <template #body>
      <h5>В разработке...</h5>
    </template>
  </BaseLayout>
</template>

<script>
import BaseLayout from "@/components/BaseLayout";

export default {
  name: "CategoriesList",
  components: {
    BaseLayout,
  }
}
</script>

<style scoped>

</style>