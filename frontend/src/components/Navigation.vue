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
import {addCircleOutline, analyticsOutline, listOutline, personOutline, shapesOutline} from "ionicons/icons";
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
      shapesOutline: shapesOutline,
      personOutline: personOutline,
    }
  },
  mounted() {
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