<template>
  <ion-page>
    <ion-header
      :translucent="false"
    >
      <ion-toolbar>
        <slot name="main-header">
          <ion-title>{{ pageTitle }}</ion-title>
        </slot>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <ion-header v-if="head">
        <div class="container ion-margin-top">
          <slot name="head"></slot>
        </div>
      </ion-header>
      <div class="container">
        <slot name="body"></slot>
      </div>
    </ion-content>
  </ion-page>
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
import {defineComponent} from "vue";
import PWAPrompt from "@/components/common/PWAPrompt.vue";

export default defineComponent({
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
    PWAPrompt,
  },
  props: {
    pageTitle: {
      type: String,
      default: 'FinaFlow',
    },
    head: {
      type: Boolean,
      default: false,
    }
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
})
</script>

<style lang="scss" scoped>

ion-title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

ion-menu-button {
  color: $white;
}

</style>