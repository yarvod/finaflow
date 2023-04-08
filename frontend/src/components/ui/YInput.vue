<template>
  <div class="float-container">
    <label :for="label">{{ label }}</label>
    <input
        :type="type"
        :id="label"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        :disabled="disabled"
    >
  </div>
</template>

<script>
export default {
  name: "YInput",
  props: {
    type: {
      type: String,
      default: ''
    },
    label: {
      type: String,
      default: "Лэйбл"
    },
    modelValue: {
      type: String,
      default: '',
      required: true
    },
    disabled: {
      type: Boolean,
      default: false,
    }
  }
}
</script>

<style lang="scss" scoped>

/** float container */
.float-container {
  display: flex;
  flex-direction: column;
  border: 1px solid $Base1;
  box-sizing: border-box;
  width: 100%;
  height: 32px;
  background-color: $white;

  input {
    border: none;
    font-size: 16px;
    outline: 0;
    padding-left: 10px;
  }

  label {
    color: $black;
    font-family: $base-font;
    font-style: normal;
    font-weight: 400;
    font-size: 8px;
    line-height: 7px;
    padding-left: 2px;
    padding-top: 1px;
  }
}

</style>