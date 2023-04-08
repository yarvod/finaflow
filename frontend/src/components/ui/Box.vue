<template>
  <div
      :class="$style.box"
  >
    <span :class="$style.text">
      <slot></slot>
    </span>
  </div>
</template>

<script>
export default {
  name: "Box",
  props: {
    color: {
      type: String,
      default: "#4CDA52",
    },
    radius: {
      type: String,
      default: '0px',
    },
    height: {
      type: String,
      default: 'auto',
    },
    width: {
      type: String,
      default: 'auto',
    },
    borderColor: {
      type: String,
      default: 'transparent'
    }
  }
}
</script>

<style lang="scss" module>

.box {
  float: contour;
  clear: both;
  background-color: v-bind('color');
  border-color: v-bind('borderColor');
  border-radius: v-bind('radius');
  height: v-bind('height');
  width: v-bind('width');
}

.text {
  padding: 2.5px 4px;
  font-style: normal;
  font-weight: 550;
  font-size: 12px;
  line-height: 10px;
}

</style>