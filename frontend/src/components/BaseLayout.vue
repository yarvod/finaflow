<template>
  <component>
    <ion-page>
      <ion-header
        :translucent="false"
      >
        <ion-toolbar class="main-head">
          <div class="container flex">
            <ion-title>{{ pageTitle }}</ion-title>
          </div>
        </ion-toolbar>
      </ion-header>

      <ion-content :fullscreen="true">
        <ion-header v-if="head">
          <ion-toolbar>
            <div class="container">
              <slot name="head"></slot>
            </div>
          </ion-toolbar>
        </ion-header>
        <div class="container">
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
  IonFooter,
  IonIcon,
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
    IonFooter,
    IonIcon,
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

ion-menu-button {
  color: $white;
}

</style>