<template>
  <input
      type="range"
      min="0"
      max="100"
      step="1"
      :value="value"
      @input="updateSlider"
      :style="{backgroundSize: backgroundSize}"
      disabled
  />
</template>

<script>

export default {
  name: "YSlider",
  props: {
    value: {
      type: Number,
      default: 50,
    }
  },
  data() {
    return {
      backgroundSize: '20% 100%',
    }
  },
  methods: {
    updateSlider(e) {
      let clickedElement = e.target,
          min = clickedElement.min,
          max = clickedElement.max,
          val = clickedElement.value;
      this.backgroundSize = (val - min) * 100 / (max - min) + '% 100%';
      this.$emit('update', val)
    }
  }
}
</script>

<style lang="scss" scoped>
input[type=range] {
  -webkit-appearance: none;
  margin: 18px 0;
  width: 100%;
  background-color: $Base0;
}
input[type=range]:focus {
  outline: none;
}
input[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 1px;
  background: $Base1;
}
input[type=range]::-webkit-slider-thumb {
  height: 16px;
  width: 16px;
  border-radius: 50%;
  border: 0;
  background: $Base1;
  -webkit-appearance: none;
  margin-top: -8px;
}
input[type=range]:focus::-webkit-slider-runnable-track {
  background: $Base1;
}
input[type=range]::-moz-range-track {
  width: 100%;
  height: 1px;
  background: $Base1;
}
input[type=range]::-moz-range-thumb {
  height: 16px;
  width: 16px;
  border: 0;
  border-radius: 50%;
  background: $Base1;
}
input[type=range]::-ms-track {
  width: 100%;
  height: 1px;
  background: transparent;
  border-color: transparent;
  border-width: 16px 0;
  color: transparent;
}
input[type=range]::-ms-fill-lower {
  background: $Base1;
}
input[type=range]::-ms-fill-upper {
  background: $Base1;
  border-radius: 2.6px;
}
input[type=range]::-ms-thumb {
  height: 16px;
  width: 16px;
  border: 0;
  border-radius: 50%;
  background: $Base1;
  cursor: pointer;
}
input[type=range]:focus::-ms-fill-lower {
  background: $Base1;
}
input[type=range]:focus::-ms-fill-upper {
  background: $Base1;
}


</style>
