<template>
  <Treeselect
    v-model="new_value"
    :options="options"
    :multiple="false"
    :show-count="true"
    :open-on-click="true"
    :close-on-select="true"
    :noResultsText="'Не найдено :('"
    placeholder="Категория"
  >
    <template #value-label="{ node }">
      <div>
        {{ node.raw.label }}
      </div>
    </template>
    <template
      #option-label="{ node, shouldShowCount, count, labelClassName, countClassName }"
    >
      <div class="listItem">
        {{ node.label }}
        <span
          v-if="shouldShowCount"
          :class="countClassName"
        >
          ({{ count }})
        </span>
      </div>
    </template>
  </Treeselect>
</template>

<script>
import Treeselect from 'vue3-treeselect';
import '@/assets/style/scss/treeselect.scss';

export default {
  name: "TreeSelect",
  components: {
    Treeselect,
  },
  props: {
    value: {
      type: String,
      default: null,
    },
    options: {
      type: Array,
      default: [],
    }
  },
  computed: {
    new_value: {
      set(v) {
        this.$emit('set_value', v);
      },
      get() {
        return this.value;
      }
    }
  }
}
</script>

<style lang="scss" scoped>

.listItem {
  margin-top: 5px;
  margin-bottom: 5px;
}

</style>