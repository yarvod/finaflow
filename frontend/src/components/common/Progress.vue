<template>
  <div class="progress">
    <span :style="{'--color': color, '--progress': value + '%'}"></span>
  </div>
</template>

<script>
export default {
  name: "Progress",
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

.progress {
  width: 141px;
  height: 16px;
  margin: 20px 10px;
  border: 1px solid #000000;
  overflow: hidden;
  position: relative;
  background-color: rgb(255, 255, 255);
}

.progress span {
  background-color: var(--color);
  height: 100%;
  display: block;
  width: var(--progress);
  line-height: 30px;
  position: absolute;
  text-align: end;
  padding-right: 5px;
  border-right: 1px solid #000000;
}

</style>