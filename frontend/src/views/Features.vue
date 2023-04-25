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
              <div class="groupWrapper category">
                <h3>
                  Категории
                </h3>
                <ion-icon :icon="icons.shapesOutline" size="large"/>
              </div>
            </ion-col>
            <ion-col>
              <div class="groupWrapper export">
                <h3>
                  Экспорт
                </h3>
                <ion-icon :icon="icons.shareOutline" size="large"/>
              </div>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col size="8">
              <div class="groupWrapper regular">
                <h3>
                  Регулярные платежи
                </h3>
                <ion-icon :icon="icons.syncCircleOutline" size="large"/>
              </div>
            </ion-col>
            <ion-col>
              <div class="groupWrapper debt">
                <h3>
                  Долги
                </h3>
                <ion-icon :icon="icons.cashOutline" size="large"/>
              </div>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col size="6">
              <div class="groupWrapper friends">
                <h3>
                  Пригласить друзей
                </h3>
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
import {IonCardTitle, IonCol, IonGrid, IonIcon, IonRow} from "@ionic/vue";
import ComingSoon from "@/components/common/ComingSoon.vue";
import {shapesOutline, shareOutline, syncCircleOutline, cashOutline, peopleOutline} from "ionicons/icons";

export default {
  name: "Features",
  components: {
    BaseLayout,
    IonCardTitle,
    ComingSoon,
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
  }
}
</script>

<style lang="scss" scoped>

.groupWrapper {
  color: $white;
  min-height: 50px;

  @include respond-to(desktop) {
    transition: all .3s ease;
  }

  &:hover {
    @include respond-to(desktop) {
      cursor: pointer;
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(31, 34, 42, .05), 0 2px 6px rgba(31, 34, 42, .02), 0 0 1px rgba(31, 34, 42, .02);
    }
  }

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