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
              Список операций
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
            ></ion-menu-button>
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
      <ion-footer>
        <ion-toolbar>
<!--          <ion-tabs>-->
<!--            <ion-tab-bar slot="bottom" selected-tab="list">-->
              <ion-tab-button tab="analytics">
                <ion-icon :icon="analyticsOutline"/>
                <ion-label>Аналитика</ion-label>
              </ion-tab-button>

              <ion-tab-button tab="list">
                <ion-icon :icon="listOutline"/>
                <ion-label>Список</ion-label>
              </ion-tab-button>

              <ion-tab-button tab="add">
                <ion-icon :icon="addCircleOutline"/>
                <ion-label>Добавить</ion-label>
              </ion-tab-button>

              <ion-tab-button tab="categories">
                <ion-icon :icon="shapesOutline"/>
                <ion-label>Категории</ion-label>
              </ion-tab-button>

              <ion-tab-button tab="profile">
                <ion-icon :icon="personOutline"/>
                <ion-label>Профиль</ion-label>
              </ion-tab-button>
<!--            </ion-tab-bar>-->
<!--          </ion-tabs>-->
        </ion-toolbar>
      </ion-footer>
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
  IonIcon, IonTabButton, IonTabs, IonTabBar,
} from '@ionic/vue';
import {mapGetters} from "vuex";
import {addCircleOutline, analyticsOutline, listOutline, personOutline, shapesOutline} from "ionicons/icons";

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
    IonTabButton,
    IonTabs,
    IonTabBar,
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
  data() {
    return {
      analyticsOutline: analyticsOutline,
      listOutline: listOutline,
      addCircleOutline: addCircleOutline,
      shapesOutline: shapesOutline,
      personOutline: personOutline,
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