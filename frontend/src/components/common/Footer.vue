<template>
  <div class="footer">
    <p>{{ new Date().getFullYear() }} — <strong>Система НТП</strong></p>
  </div>
</template>

<script>
export default {
  name: "Footer",
}
</script>

<style lang="scss" scoped>

.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  height: $headerHeight;
  background-color: $Base1;
  color: $white;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>