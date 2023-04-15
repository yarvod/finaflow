<template>
  <ion-header>
    <ion-toolbar>
      <ion-buttons slot="start">
        <ion-button
          color="medium"
          @click="cancel"
        >
          Закрыть
        </ion-button>
      </ion-buttons>
      <ion-buttons slot="end">
        <ion-button
          :strong="true"
          color="danger"
          @click="removeOperation"
        >
          Удалить
        </ion-button>
      </ion-buttons>
    </ion-toolbar>
  </ion-header>
  <ion-content class="ion-padding">
    <ion-item ref="type">
      <ion-label position="stacked">Тип</ion-label>
      <ion-select
        :value="form.type"
        @ionChange="form.type = $event.detail.value"
        interface="popover"
        placeholder="Выберете тип"
      >
        <IonSelectOption :value="1">Расход</IonSelectOption>
        <IonSelectOption :value="2">Доход</IonSelectOption>
      </ion-select>
    </ion-item>
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
        v-if="this.form.category"
        v-model="form.category"
        :options="categories"
        :multiple="false"
        :default-expand-level="1"
        :show-count="true"
        :open-on-click="true"
        :close-on-select="true"
        :noResultsText="'Не найдено :('"
        placeholder="Категория"
      />
    </div>
    <ion-button
      color="primary"
      expand="block"
      @click="saveOperation"
    >
      Сохранить
    </ion-button>
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
  IonSelect, IonSelectOption,
} from "@ionic/vue";
import TreeSelect from 'vue3-treeselect';
import 'vue3-treeselect/dist/vue3-treeselect.css';
import {mapGetters} from "vuex";

export default {
  name: "OperationEditModal",
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
    IonSelect,
    IonSelectOption,
  },
  props: {
    operation: {
      type: Object,
      required: false,
    }
  },
  data() {
    return {
      form: {},
      is_valid: false,
    }
  },
  computed: {
    ...mapGetters(['categories']),
  },
  async mounted() {
    this.form = {
      id: this.operation.id,
      type: this.operation.type,
      category: this.operation.category.id,
      money: this.operation.money,
      comment: this.operation.comment,
      date: this.operation.date,
    }
    await this.$store.dispatch('getCategories', {query: {type: this.form.type}});
  },
  methods: {
    async changeType(e) {
      this.form.category = null;
      await this.$store.dispatch('getCategories', {query: {type: this.form.type}});
    },
    cancel() {
      return modalController.dismiss(null, 'cancel');
    },
    removeOperation() {
      this.$store.dispatch('deleteOperation', {data: this.operation})
        .then(async status => {
          if (status === 204) {
            await this.$store.dispatch('getOperations');
            return modalController.dismiss(null, 'cancel');
          }
        })
    },
    async saveOperation() {
      this.is_valid = this.validateMoney()
      if (this.is_valid) {
        await this.$store.dispatch('updateOperation', {data: this.form})
          .then(async status => {
            if (status === 200) {
              await this.$store.dispatch('getOperations');
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