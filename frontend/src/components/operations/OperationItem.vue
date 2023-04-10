<template>
  <div class="card">
    <div class="contentWrapper">
      <div class="leftSide">
        <div class="title">
          {{ get_categories_titles() }}
        </div>
        <div
          class="comment"
          v-if="operation.comment"
        >
          {{ operation.comment }}
        </div>
      </div>
      <div class="rightSide">
        <span class="money" :style="get_money_color()">{{ (operation.money).toLocaleString('ru') }}</span>
        <span class="money" :style="get_money_color()">{{ currency_choices[operation.currency] }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import {CURRENCY_CHOICES} from "@/utils/constants";

export default {
  name: "OperationItem",
  props: {
    operation: {
      required: true,
      type: Object,
    }
  },
  data () {
    return {
      currency_choices: CURRENCY_CHOICES,
    }
  },
  methods: {
    get_categories_titles() {
      if (this.operation.categories_titles) {
        return this.operation.categories_titles.join(": ")
      }
      return "None"
    },
    get_money_color() {
      if (this.operation.type === 1) {
        return {'--color': '#ed5e64'}
      }
      return {'--color': '#5ccc8b'}
    }
  },
}
</script>

<style lang="scss" scoped>
.card {
  border: $Gray300 1px solid;
  border-radius: 5px;
  padding: 10px;
  width: 100%;
  margin-top: 10px;
}

.contentWrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.leftSide {

}

.rightSide {

}

.title {
  font-family: $base-font;
  font-size: 15px;
}

.comment {
  margin: 5px;
  font-family: $base-font;
  font-size: 12px;
  color: $Gray400;
}

.money {
  margin-right: 5px;
  color: var(--color);
}
</style>