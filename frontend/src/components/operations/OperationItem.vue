<template>
  <div class="operation-card hover" @click="openModal">
    <div class="contentWrapper">
      <div class="leftSide">
        <ion-card-title class="title" mode="ios">
          {{ get_categories_titles() }}
        </ion-card-title>
        <div
          class="comment"
          v-if="operation.comment"
        >
          {{ operation.comment }}
        </div>
      </div>
      <div class="rightSide">
        <span class="money" :style="get_type_color()">{{ (operation.money).toLocaleString('ru') }}</span>
        <span class="money" :style="get_type_color()">{{ currency_choices[operation.currency] }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import {CURRENCY_CHOICES, TYPE_CHOICES} from "@/utils/constants";
import {IonCardSubtitle, IonCardTitle, IonChip, modalController} from "@ionic/vue";
import {dateFilter} from "@/utils/functions";
import OperationModal from "@/components/operations/OperationModal";
import OperationEditModal from "@/components/operations/OperationEditModal";

export default {
  name: "OperationItem",
  components: {
    IonChip,
    IonCardSubtitle,
    IonCardTitle,
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
        return {'--color': '#ed5e64'}
      }
      return {'--color': '#5ccc8b'}
    },
    async openModal() {
      const modal = await modalController.create({
        component: OperationEditModal,
        presentingElement: this.presentingElement,
        canDismiss: true,
        componentProps: {operation: this.operation}
      });
      modal.present();
      const {data, role} = await modal.onWillDismiss();
    },
  },
}
</script>

<style lang="scss" scoped>
.operation-card {
  background-color: $white;
  border-radius: $BorderRadius;
  padding: 10px;
  width: 100%;
  margin-bottom: 10px;

  &:active {
    transition: all .1s ease;
    background-color: $Secondary0;
  }

  &:last-of-type {
    margin-bottom: 0;
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
  font-size: 16px;
}

.comment {
  margin: 5px;
  font-family: $base-font;
  font-size: 12px;
  color: $Gray400;
  word-break: break-all;
}

.money {
  margin-right: 5px;
  color: var(--color);
}
</style>