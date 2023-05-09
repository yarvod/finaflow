<template>
  <ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-button color="medium" @click="cancel">Закрыть</ion-button>
      </ion-buttons>
      <ion-segment
        @IonChange="changeType($event)"
        v-model="type"
      >
        <ion-segment-button :value="1">
          <ion-label>Расход</ion-label>
        </ion-segment-button>
        <ion-segment-button :value="2">
          <ion-label>Доход</ion-label>
        </ion-segment-button>
      </ion-segment>
      <ion-buttons slot="end">
        <ion-button @click="openCategoryModal" :strong="true">Добавить</ion-button>
      </ion-buttons>
    </ion-toolbar>
  </ion-header>
  <ion-content>
    <div class="h2 title">Категории</div>
    <div
      class="small-card hover mb5"
      v-for="category in categories"
      :key="category.id"
    >
      <div>
        {{ category.label }} <span v-if="category?.children?.length">({{category.children.length}})</span>
      </div>
    </div>
  </ion-content>
</template>

<script>
import {
  IonButton,
  IonButtons,
  IonContent,
  IonHeader,
  IonItem,
  IonLabel,
  IonList,
  IonSegment,
  IonSegmentButton,
  IonToolbar,
  modalController
} from "@ionic/vue";
import {mapGetters} from "vuex";
import CategoryModal from "@/components/categories/CategoryModal.vue";

export default {
  name: "CategoriesModal",
  components: {
    IonHeader,
    IonToolbar,
    IonButtons,
    IonButton,
    IonSegment,
    IonSegmentButton,
    IonLabel,
    IonContent,
    IonList,
    IonItem,
  },
  data() {
    return {
      type: "1",
    }
  },
  computed: {
    ...mapGetters(['categories']),
  },
  async mounted() {
    await this.$store.dispatch('getCategories', {query: {type: this.type}});
  },
  methods: {
    async changeType(e) {
      await this.$store.dispatch('getCategories', {query: {type: this.type}});
    },
    cancel() {
      return modalController.dismiss(null, 'cancel');
    },
    async openCategoryModal() {
      const modal = await modalController.create({
        component: CategoryModal,
        componentProps: {type: this.type},
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

.title {
  margin-top: 15px;
  margin-bottom: 15px;
  margin-left: 15px;
}

.small-card {
  margin-left: 15px;
  margin-right: 15px;
}

</style>