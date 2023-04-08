<template>
  <div class="border">
    <div class="legendItem">
      <div class="legendLabel">
        Разработка
      </div>
      <div
          class="box round"
      ></div>
    </div>
    <div class="legendItem">
      <div class="legendLabel">
        Продукт
      </div>
      <div
          class="box"
      ></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GraphLegend"
}
</script>

<style lang="scss" scoped>

.border {
  border: 0.3px solid $Gray200;
  padding: 5px;
  border-radius: 5px;
}

.legendItem {
  display: flex;
  justify-content: end;
  align-items: center;

  &:last-of-type {
    margin-top: 7px;
  }
}

.legendLabel {
  margin-right: 8px;
  font-size: 12px;
  color: $Gray500;
}

.box {
  float: right;
  width: 17px;
  height: 17px;
  clear: both;
  border: 0.3px solid $Gray500;
  background-color: transparent;
  border-radius: 2px;
}

.round {
  border-radius: 50%;
}

</style>