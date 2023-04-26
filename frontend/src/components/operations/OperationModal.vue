<template>
  <ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-button color="medium" @click="cancel">Закрыть</ion-button>
      </ion-buttons>
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
      <ion-buttons slot="end">
        <ion-button @click="confirm" :strong="true">Добавить</ion-button>
      </ion-buttons>
    </ion-toolbar>
  </ion-header>
  <ion-content class="ion-padding">
    <div class="groupWrapper" ref="money">
      <ion-label position="stacked">Сумма</ion-label>
      <div class="input-card">
        <ion-input
          type="number"
          inputmode="decimal"
          v-model="form.money"
          placeholder="1000"
        ></ion-input>
      </div>
      <div v-show="!validateMoney" class="note error">Введите сумму!</div>
    </div>
    <div class="groupWrapper">
      <ion-label position="stacked">Категория</ion-label>
      <TreeSelect
        :value="form.category"
        :options="categories"
        @set_value="this.form.category = $event"
      />
      <div v-show="!validateCategory" class="note error">Выберете категорию!</div>
    </div>
    <div class="groupWrapper">
      <ion-label position="stacked">Дата</ion-label>
      <div class="input-card">
        <ion-datetime-button v-model="form.date" datetime="date" mode="ios"></ion-datetime-button>
      </div>
      <ion-modal class="datetime-modal" :keep-contents-mounted="true" mode="ios">
        <ion-datetime
          v-model="form.date"
          id="date"
          presentation="date"
          :prefer-wheel="false"
          mode="ios"
        ></ion-datetime>
      </ion-modal>
    </div>
    <div class="groupWrapper">
      <ion-label position="stacked">Комментарий</ion-label>
      <div class="input-card">
        <ion-input
          type="text"
          v-model="form.comment"
          placeholder="Комментарий"
        ></ion-input>
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
  IonItem,
  IonTitle,
  IonToolbar,
  modalController,
  IonDatetime,
  IonDatetimeButton,
  IonSegment,
  IonSegmentButton,
} from "@ionic/vue";
import {mapGetters} from "vuex";
import TreeSelect from "@/components/ui/TreeSelect.vue";

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
        date: new Date().toJSON().slice(0, 10),
        category: null,
        comment: null,
      },
      is_valid: false,
    }
  },
  computed: {
    ...mapGetters(['categories']),
    validateMoney() {
      return this.form.money;
    },
    validateCategory() {
      return this.form.category;
    }
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
      this.is_valid = this.validateMoney && this.validateCategory
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

.category-label {
  font-size: small;
}

</style>