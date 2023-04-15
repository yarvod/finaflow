<template>
  <ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-button color="medium" @click="cancel">Закрыть</ion-button>
      </ion-buttons>
      <ion-buttons slot="end">
        <ion-button @click="confirm" :strong="true">Добавить</ion-button>
      </ion-buttons>
    </ion-toolbar>
  </ion-header>
  <ion-content class="ion-padding">
    <ion-segment
      @IonChange="changeType($event)"
      v-model="form.type"
    >
      <ion-segment-button :value="1">
        <ion-label>Расход</ion-label>
      </ion-segment-button>
      <ion-segment-button :value="2">
        <ion-label>Доход</ion-label>
      </ion-segment-button>
    </ion-segment>
    <ion-item ref="money">
      <ion-label position="stacked">Сумма</ion-label>
      <ion-input
        type="number"
        v-model="form.money"
        placeholder="500"
      ></ion-input>
      <ion-note slot="error">Введите сумму!</ion-note>
    </ion-item>
    <ion-item>
      <ion-label position="stacked">Дата</ion-label>
      <ion-datetime-button v-model="form.date" datetime="date" mode="ios"></ion-datetime-button>
      <ion-modal :keep-contents-mounted="true" mode="ios">
        <ion-datetime
          v-model="form.date"
          id="date"
          presentation="date-time"
          :prefer-wheel="true"
           mode="ios"
        ></ion-datetime>
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
        :show-count="true"
        :open-on-click="true"
        :close-on-select="true"
        :noResultsText="'Не найдено :('"
        placeholder="Категория"
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
  IonTextarea, IonSegment, IonSegmentButton,
} from "@ionic/vue";
import TreeSelect from 'vue3-treeselect';
import 'vue3-treeselect/dist/vue3-treeselect.css';
import {mapGetters} from "vuex";

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
    IonSegment,
    IonSegmentButton,
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
        date: new Date().toISOString(),
        category: null,
        comment: "",
      },
      is_valid: false,
    }
  },
  computed: {
    ...mapGetters(['categories']),
  },
  async mounted() {
    await this.$store.dispatch('getCategories', {query: {type: this.form.type}});
  },
  methods: {
    async changeType(e) {
      this.form.category = null;
      await this.$store.dispatch('getCategories', {query: {type: this.form.type}});
    },
    cancel() {
      this.form = {};
      return modalController.dismiss(null, 'cancel');
    },
    async confirm() {
      this.is_valid = this.validateMoney()
      if (this.is_valid) {
        await this.$store.dispatch('createOperation', {data: this.form})
          .then(async status => {
            if (status === 201) {
              await this.$store.dispatch('getOperations');
              this.form = {};
              return modalController.dismiss(null, 'confirm');
            }
          })
      }
    },
    validateMoney() {
      this.$refs.money.$el.classList.remove('ion-valid');
      this.$refs.money.$el.classList.remove('ion-invalid');

      if (!this.form.money) {
        this.$refs.money.$el.classList.add('ion-invalid');
        return false
      } else {
        this.$refs.money.$el.classList.add('ion-valid');
        return true
      }
    },
  },
}
</script>

<style lang="scss" scoped>

ion-segment {
  margin-bottom: 5px;
}

ion-datetime-button {
  margin-top: 10px;
  margin-bottom: 5px;
}

.tree-select {
  margin-top: 5px;
  color: var(--ion-item-background);
}

.item-custom {
  padding: 10px 20px;
  background-color: var(--ion-item-background)
}

</style>