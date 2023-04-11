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
        <ion-datetime v-model="form.date" id="date"></ion-datetime>
      </ion-modal>
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
    <ion-item>
      <ion-label position="stacked">Комментарий</ion-label>
      <ion-textarea
        v-model="form.comment"
        placeholder="Комментарий"
      ></ion-textarea>
    </ion-item>
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
        money: 100,
        date: '2023-04-10T00:00',
        category: null,
        comment: "",
      },
      categories: [
        {
          id: 'a',
          label: 'a',
          children: [
            {
              id: 'aa',
              label: 'aa',
            },
            {
              id: 'ab',
              label: 'ab',
            }
          ],
        },
        {
          id: 'b',
          label: 'b',
        },
        {
          id: 'c',
          label: 'c',
        }
      ],
    }
  },
  methods: {
    cancel() {
      return modalController.dismiss(null, 'cancel');
    },
    confirm() {
      return modalController.dismiss(this.name, 'confirm');
    },
  },
}
</script>

<style lang="scss" scoped>

ion-datetime-button {
  margin-bottom: 5px;
}

.tree-select {
  margin-top: 5px;
}

.item-custom {
  margin-top: 10px;
  padding-left: 20px;
  padding-right: 20px;
}

</style>