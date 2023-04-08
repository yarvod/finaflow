<template>
  <component>
    <ion-menu
        content-id="main-content"
        side="end"
        v-if="isAuthenticated"
    >
      <ion-header>
        <ion-toolbar>
          <ion-title>Меню</ion-title>
        </ion-toolbar>
      </ion-header>
      <ion-content class="ion-padding">
        <ion-list>
          <ion-item button @click="$router.push({name: 'home'})">
            <ion-label>
              Главная
            </ion-label>
          </ion-item>
          <ion-item button @click="$router.push({name: 'account'})">
            <ion-label>
              Профиль
            </ion-label>
          </ion-item>
        </ion-list>
      </ion-content>
    </ion-menu>
    <ion-page id="main-content">
      <ion-header
          :translucent="false"
      >
        <ion-toolbar class="main-head">
          <div class="container flex">
            <ion-title>{{ pageTitle }}</ion-title>
            <ion-menu-button
                v-if="isAuthenticated"
                color="dark"
            ></ion-menu-button>
          </div>
        </ion-toolbar>
      </ion-header>

      <ion-content :fullscreen="true">
        <ion-header v-if="head">
          <ion-toolbar>
            <slot name="head"></slot>
          </ion-toolbar>
        </ion-header>
        <div class="container" id="container">
          <slot name="body"></slot>
        </div>
      </ion-content>
    </ion-page>
  </component>
</template>

<script>
import {
  IonButtons,
  IonContent,
  IonHeader,
  IonList,
  IonMenu,
  IonMenuButton,
  IonPage,
  IonTitle,
  IonToolbar,
  IonItem,
  IonLabel,
} from '@ionic/vue';
import {mapGetters} from "vuex";

export default {
  name: "BaseLayout",
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonButtons,
    IonMenu,
    IonMenuButton,
    IonList,
    IonItem,
    IonLabel,
  },
  props: {
    pageTitle: {
      type: String,
      default: 'finaflow',
    },
    head: {
      type: Boolean,
      default: false,
    }
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
}
</script>

<style lang="scss" scoped>

.main-head {
  --color: white;
  --background: var(--base1);
}

.flex {
  display: flex;
  justify-content: space-between;
}

ion-title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

</style>