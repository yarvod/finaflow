<template>
  <BaseLayout head>
    <template #head>
      <ion-card-title>Фичи</ion-card-title>
    </template>
    <template #body>
      <transition name="fade" mode="out-in" appear>
        <ion-grid>
          <ion-row>
            <ion-col>
              <div
                class="groupWrapper hover category"
                @click="openCategoriesModal"
              >
                <div class="h3">
                  Категории
                </div>
                <ion-icon :icon="icons.shapesOutline" size="large"/>
              </div>
            </ion-col>
            <ion-col>
              <div class="groupWrapper hover export">
                <div class="h3">
                  Экспорт
                </div>
                <ion-icon :icon="icons.shareOutline" size="large"/>
              </div>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col size="8">
              <div class="groupWrapper hover regular">
                <div class="h3">
                  Регулярные платежи
                </div>
                <ion-icon :icon="icons.syncCircleOutline" size="large"/>
              </div>
            </ion-col>
            <ion-col>
              <div class="groupWrapper hover debt">
                <div class="h3">
                  Долги
                </div>
                <ion-icon :icon="icons.cashOutline" size="large"/>
              </div>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col size="6">
              <div class="groupWrapper hover friends">
                <div class="h3">
                  Пригласить друзей
                </div>
                <ion-icon :icon="icons.peopleOutline" size="large"/>
              </div>
            </ion-col>
          </ion-row>
        </ion-grid>
      </transition>
    </template>
  </BaseLayout>
</template>

<script>
import BaseLayout from "@/components/BaseLayout.vue";
import {IonCardTitle, IonCol, IonGrid, IonIcon, IonRow, modalController} from "@ionic/vue";
import ComingSoon from "@/components/common/ComingSoon.vue";
import {shapesOutline, shareOutline, syncCircleOutline, cashOutline, peopleOutline} from "ionicons/icons";
import CategoriesModal from "@/components/categories/CategoriesModal.vue";

export default {
  name: "Features",
  components: {
    BaseLayout,
    IonCardTitle,
    ComingSoon,
    CategoriesModal,
    IonIcon,
    IonCol,
    IonRow,
    IonGrid,
  },
  data() {
    return {
      icons: {
        shapesOutline: shapesOutline,
        shareOutline: shareOutline,
        syncCircleOutline: syncCircleOutline,
        cashOutline: cashOutline,
        peopleOutline: peopleOutline,
      },
    }
  },
  methods: {
    async openCategoriesModal() {
      const modal = await modalController.create({
        component: CategoriesModal,
        presentingElement: this.presentingElement,
        canDismiss: true,
      });
      await modal.present();
      const {data, role} = await modal.onWillDismiss();
    },
  },
}
</script>

<style lang="scss" scoped>

.groupWrapper {
  color: $white;
  min-height: 50px;

  &:active {
    transition: all .1s ease;
    background: $Secondary0;
  }

  &.category {
    background: $Base600;
  }

  &.export {
    background: $Emerald400;
  }

  &.regular {
    background: $Yellow;
  }

  &.debt {
    background: $Blue;
  }

  &.friends {
    background: $Pink;
  }
}

</style>