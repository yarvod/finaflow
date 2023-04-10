<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom" selected-tab="operations">
        <ion-tab-button tab="operations" href="/operations">
          <ion-icon :icon="listOutline"/>
          <ion-label>Список</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="analytics" href="/analytics">
          <ion-icon :icon="analyticsOutline"/>
          <ion-label>Аналитика</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="add-operation">
          <ion-icon :icon="addCircleOutline"/>
          <ion-label>Добавить</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="categories" href="/categories">
          <ion-icon :icon="shapesOutline"/>
          <ion-label>Категории</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="account" href="/account">
          <ion-icon :icon="personOutline"/>
          <ion-label>Профиль</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script>
import {IonIcon, IonLabel, IonPage, IonRouterOutlet, IonTabBar, IonTabButton, IonTabs} from "@ionic/vue";
import {addCircleOutline, analyticsOutline, listOutline, personOutline, shapesOutline} from "ionicons/icons";

export default {
  name: "Navigation",
  components: {
    IonPage,
    IonRouterOutlet,
    IonTabs,
    IonTabBar,
    IonTabButton,
    IonIcon,
    IonLabel,
  },
  data() {
    return {
      analyticsOutline: analyticsOutline,
      listOutline: listOutline,
      addCircleOutline: addCircleOutline,
      shapesOutline: shapesOutline,
      personOutline: personOutline,
    }
  },
}
</script>

<style scoped>

</style>