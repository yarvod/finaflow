<template>
  <ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-button color="medium" @click="cancel">Закрыть</ion-button>
      </ion-buttons>
      <ion-buttons slot="end">
        <ion-button @click="add" :strong="true">Добавить</ion-button>
      </ion-buttons>
    </ion-toolbar>
  </ion-header>
  <ion-content>
    <div class="wrapper">
      <div class="groupWrapper">
        <ion-label position="stacked">Название</ion-label>
        <div class="input-card">
          <ion-input
            type="text"
            v-model="form.title"
            placeholder="Название"
          ></ion-input>
        </div>
        <div v-show="!validateTitle" class="note error">Введите название!</div>
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
  IonInput,
  IonLabel,
  IonToolbar,
  modalController,
} from "@ionic/vue";

export default {
  name: "CategoryModal",
  components: {
    IonHeader,
    IonToolbar,
    IonButtons,
    IonButton,
    IonContent,
    IonLabel,
    IonInput,
  },
  props: {
    type: {
      type: String,
      default: "1",
    }
  },
  data() {
    return {
      form: {
        title: null,
        type: Number(this.type),
        parent: null,
      },
      is_valid: false,
    }
  },
  computed: {
    validateTitle() {
      return this.form.title
    },
  },
  methods: {
    cancel() {
      return modalController.dismiss(null, 'cancel');
    },
    async add() {
      this.is_valid = this.validateTitle;
      if (this.is_valid) {
        await this.$store.dispatch('createCategory', {data: this.form})
          .then(async status => {
            if (status === 201) {
              await this.$store.dispatch('getCategories', {query: {type: this.type}});
              this.form = {};
              return modalController.dismiss(null, 'confirm');
            }
          })
      }
    },
  },
}
</script>

<style lang="scss" scoped>

.wrapper {
  margin: 15px;
}

</style>