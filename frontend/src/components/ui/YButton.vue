<template>
  <button :type="type" :disabled="disabled" class="button-text">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "YButton",
  props: {
    type: {
      type: String,
      default: '',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    color: {
      type: String,
      default: "#0069B4",
    },
    text_color: {
      type: String,
      default: "#F9FBF2",
    }
  }
}
</script>

<style lang="scss" scoped>
button {
  background-color: v-bind('color');
  border-radius: 4px;
  padding: 5px 20px;
  border: 2px solid v-bind('color');
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: .3s;

  &:after {
    position: absolute;
    transition: .3s;
    content: '';
    width: 0;
    left: 50%;
    bottom: 0;
    height: 3px;
    background: v-bind('color');
  }

  &:hover {
    cursor: pointer;
    box-shadow: 0 0 0 4px v-bind('color');

    &:after {
      width: 100%;
      left: 0;
    }
  }
}

.button-text {
  font-family: 'Fira Sans', sans-serif !important;
  font-style: normal !important;
  font-weight: 400 !important;
  font-size: 15px !important;
  color: v-bind('text_color');
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>