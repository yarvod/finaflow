<template>
  <ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-button color="medium" @click="cancel">Закрыть</ion-button>
      </ion-buttons>
      <ion-title>Запись</ion-title>
      <ion-buttons slot="end">
        <ion-button @click="confirm" :strong="true">Добавить</ion-button>
      </ion-buttons>
    </ion-toolbar>
  </ion-header>
  <ion-content class="ion-padding">
    <ion-item>
      <ion-label position="stacked">Сумма</ion-label>
      <ion-input
        type="number"
        v-model="form.money"
        placeholder="500"
      ></ion-input>
    </ion-item>
    <ion-item>
      <ion-label position="stacked">Дата</ion-label>
      <ion-datetime-button v-model="form.date" datetime="date"></ion-datetime-button>
      <ion-modal :keep-contents-mounted="true">
        <ion-datetime v-model="form.date" id="date" presentation="date-time" :prefer-wheel="true"></ion-datetime>
      </ion-modal>
    </ion-item>
    <ion-item>
      <ion-label position="stacked">Комментарий</ion-label>
      <ion-textarea
        v-model="form.comment"
        placeholder="Комментарий"
      ></ion-textarea>
    </ion-item>
    <div class="item-custom">
      <ion-label position="stacked">Категория</ion-label>
      <tree-select
        v-model="form.category"
        :options="categories"
        :multiple="false"
        :open-on-click="true"
        :close-on-select="true"
        placeholder="Категория"
        class="tree-select"
      />
    </div>
  </ion-content>
</template>

<script>
import {
  IonButton,
  IonButtons,
  IonContent,
  IonHeader,
  IonInput,
  IonItem,
  IonTitle,
  IonToolbar,
  modalController,
  IonDatetime,
  IonDatetimeButton,
  IonTextarea,
} from "@ionic/vue";
import TreeSelect from 'vue3-treeselect';
import 'vue3-treeselect/dist/vue3-treeselect.css';
import finance_service from "@/api/finance_service";

export default {
  name: "OperationModal",
  components: {
    IonHeader,
    IonToolbar,
    IonButtons,
    IonButton,
    IonTitle,
    IonContent,
    IonItem,
    IonInput,
    IonDatetime,
    IonDatetimeButton,
    IonTextarea,
    TreeSelect,
  },
  props: {
    operation: {
      type: Object,
      required: false,
    }
  },
  data() {
    return {
      form: {
        type: 1,
        money: null,
        date: null,
        category: null,
        comment: "",
      },
      categories: [],
    }
  },
  async mounted() {
    await finance_service.getCategoriesList({params: {type: this.form.type}})
      .then(resp => {
        if (resp && resp.status === 200) {
          this.categories = resp?.data
        }
      })
  },
  methods: {
    cancel() {
      return modalController.dismiss(null, 'cancel');
    },
    async confirm() {
      await finance_service.createOperation(this.form)
        .then(resp => {
          if (resp && resp.status === 201) {
            return modalController.dismiss(null, 'confirm');
          }
        })
    },
  },
}
</script>

<style lang="scss" scoped>

ion-datetime-button {
  margin-top: 10px;
  margin-bottom: 5px;
}

.tree-select {
  margin-top: 5px;
}

.item-custom {
  padding: 10px 20px;
  background-color: var(--ion-item-background)
}

</style>