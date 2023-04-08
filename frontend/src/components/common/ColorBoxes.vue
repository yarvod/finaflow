<template>
  <div>
    <div class="color-box-title">
      {{ title }}
    </div>
    <div style="display: flex;">
      <div
          v-for="color_box of color_boxes"
          :key="color_box.id"
      >
        <div class="color-box-label">
          {{ color_box.value }}
        </div>
        <Box
            :color="color_box.color"
            height="19px"
            width="19px"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Box from "@/components/ui/Box.vue";

export default {
  name: "ColorBoxes",
  components: {
    Box,
  },
  props: {
    title: {
      type: String,
      default: "Доля импорта",
    },
    color_boxes: {
      type: Array,
      default: [
        {id: 1, value: 0, color: "#309C34"},
        {id: 2, value: 0.1, color: "#4CDA52"},
        {id: 3, value: 0.2, color: "#C0D24C"},
        {id: 4, value: 0.3, color: "#D6EA57"},
        {id: 5, value: 0.4, color: "#DDF445"},
        {id: 6, value: 0.5, color: "#E1FF1E"},
        {id: 7, value: 0.6, color: "#FFCD1E"},
        {id: 8, value: 0.7, color: "#FFA51E"},
        {id: 9, value: 0.8, color: "#FF8A1E"},
        {id: 10, value: 0.9, color: "#FF611E"},
        {id: 11, value: 1, color: "#FF1E1E"},
      ],
    }
  },
}
</script>

<style lang="scss" scoped>

.color-box-title {
  font-style: normal;
  font-weight: 600;
  font-size: 10px;
  line-height: 10px;
  text-align: left;
}

.color-box-label {
  font-style: normal;
  font-weight: 600;
  font-size: 10px;
  line-height: 10px;
  text-align: center;
}

</style>