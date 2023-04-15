<template>
  <div class="operation-card">
    <div class="contentWrapper">
      <div class="leftSide">
        <ion-card-subtitle>{{formatDate()}}</ion-card-subtitle>
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
        <ion-chip :color="get_type_color()">
          {{ (operation.money).toLocaleString('ru') }}
          {{ currency_choices[operation.currency] }}
        </ion-chip>
      </div>
    </div>
  </div>
</template>

<script>
import {CURRENCY_CHOICES, TYPE_CHOICES} from "@/utils/constants";
import {IonCardSubtitle, IonChip} from "@ionic/vue";
import {dateFilter} from "@/utils/functions";

export default {
  name: "OperationItem",
  components: {
    IonChip,
    IonCardSubtitle,
  },
  props: {
    operation: {
      required: true,
      type: Object,
    }
  },
  data() {
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
    get_type_color() {
      if (this.operation.type === 1) {
        return "danger"
      }
      return "success"
    },
    formatDate() {
      return dateFilter(this.operation.date)
    }
  },
}
</script>

<style lang="scss" scoped>
.operation-card {
  border: $Gray300 1px solid;
  border-radius: 5px;
  padding: 10px;
  width: 100%;
  margin-top: 10px;
  @include respond-to(desktop) {
    transition: all .3s ease;
  }

  &:hover {
    @include respond-to(desktop) {
      cursor: pointer;
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(31, 34, 42, .05), 0 2px 6px rgba(31, 34, 42, .02), 0 0 1px rgba(31, 34, 42, .02);
      @media (prefers-color-scheme: dark) {
      }
    }
  }
}

.contentWrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.leftSide {
  display: flex;
  flex-direction: column;
}

.rightSide {

}

.title {
  font-family: $base-font;
  font-size: 17px;
}

.comment {
  margin: 5px;
  font-family: $base-font;
  font-size: 12px;
  color: $Gray400;
  word-break: break-all;
}

ion-chip {
  cursor: default;
}

.money {
  margin-right: 5px;
  color: var(--color);
}
</style>