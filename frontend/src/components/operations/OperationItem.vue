<template>
<div class="card bordered">
  {{operation}}
</div>
</template>

<script>
export default {
  name: "OperationItem",
  props: {
    operation: {
      required: true,
      type: Object,
    }
  }
}
</script>

<style lang="scss" scoped>
.card {
  border: $Gray300 1px solid;
  border-radius: 5px;
  padding: 5px;
  width: 100%;
}
</style>