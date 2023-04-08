<template>
  <div class="circle" :style="{'--color': color}">
    {{ value }}
  </div>
</template>

<script>
export default {
  name: "Circle",
  props: {
    color: {
      type: String,
      default: "#0069B4",
    },
    value: {
      type: Number,
      default: 50,
    }
  }
}
</script>

<style scoped>
.circle {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: table-cell;
  text-align: center;
  vertical-align: middle;
  background: var(--color);
}
</style>