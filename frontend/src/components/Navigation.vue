<template>
  <ion-page ref="page">
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="operations" href="/operations">
          <ion-icon :icon="listOutline"/>
          <ion-label>Список</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="analytics" href="/analytics">
          <ion-icon :icon="analyticsOutline"/>
          <ion-label>Аналитика</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="add-operation" @click="openModal">
          <ion-icon :icon="addCircleOutline"/>
          <ion-label>Добавить</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="features" href="/features">
          <ion-icon :icon="sparklesOutline"/>
          <ion-label>Фичи</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="more" href="/more">
          <ion-icon :icon="ellipsisHorizontalOutline"/>
          <ion-label>Еще</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script>
import {
  IonIcon,
  IonLabel,
  IonPage,
  IonRouterOutlet,
  IonTabBar,
  IonTabButton,
  IonTabs,
  modalController
} from "@ionic/vue";
import {addCircleOutline, analyticsOutline, listOutline, ellipsisHorizontalOutline, sparklesOutline} from "ionicons/icons";
import OperationModal from "@/components/operations/OperationModal";

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
      sparklesOutline: sparklesOutline,
      ellipsisHorizontalOutline: ellipsisHorizontalOutline,
    }
  },
  ionViewWillEnter() {
    this.presentingElement = this.$refs.page.$el;
  },
  methods: {
    async openModal() {
      const modal = await modalController.create({
        component: OperationModal,
        presentingElement: this.presentingElement,
        canDismiss: true,
      });
      modal.present();
      const {data, role} = await modal.onWillDismiss();
    },
  },
}
</script>

<style scoped>

</style>