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
      <ion-title>{{ type_display }}</ion-title>
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
    <div class="groupWrapper" ref="money">
      <ion-label position="stacked">Сумма</ion-label>
      <div class="input-card">
        <ion-input
          type="number"
          v-model="form.money"
          placeholder="0"
        ></ion-input>
      </div>
      <div v-show="!validateMoney" class="note error">Введите сумму!</div>
    </div>
    <div class="groupWrapper">
      <ion-label position="stacked">Категория</ion-label>
      <TreeSelect
        v-if="this.form.id"
        :value="form.category"
        :options="categories"
        @set_value="this.form.category = $event"
      />
      <div v-show="!validateCategory" class="note error">Выберете категорию!</div>
    </div>
    <div class="groupWrapper">
      <ion-label position="stacked">Дата</ion-label>
      <div class="input-card">
        <ion-datetime-button v-model="form.date" datetime="date"></ion-datetime-button>
      </div>
      <ion-modal class="datetime-modal" :keep-contents-mounted="true">
        <ion-datetime
          v-model="form.date"
          id="date"
          presentation="date"
          :prefer-wheel="false"
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
  IonSelect,
  IonSelectOption,
  actionSheetController,
} from "@ionic/vue";
import TreeSelect from "@/components/ui/TreeSelect.vue";
import {mapGetters} from "vuex";
import {TYPE_CHOICES} from "@/utils/constants";

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
    validateMoney() {
      return this.form.money;
    },
    validateCategory() {
      return this.form.category;
    },
    type_display() {
      return TYPE_CHOICES[this.operation.type]
    }
  },
  async mounted() {
    this.form = {
      id: this.operation.id,
      type: this.operation.type,
      category: this.operation?.category?.id,
      money: this.operation.money,
      comment: this.operation.comment,
      date: this.operation.date,
    }
    await this.$store.dispatch('getCategories', {query: {type: this.form.type}});
  },
  methods: {
    cancel() {
      return modalController.dismiss(null, 'cancel');
    },
    async removeOperation() {
      const actionSheet = await actionSheetController.create({
        header: 'Вы уверены, удаляем?',
        buttons: [
          {
            text: 'Удалить',
            role: 'destructive',
          },
          {
            text: 'Отменить',
            role: 'cancel',
          },
        ],
      });
      await actionSheet.present();
      const {role} = await actionSheet.onWillDismiss();
      if (role === 'destructive') {
        this.$store.dispatch('deleteOperation', {data: this.operation})
          .then(async status => {
            if (status === 204) {
              await this.$store.dispatch('getOperations');
              return modalController.dismiss(null, 'cancel');
            }
          })
      }
    },
    async saveOperation() {
      this.is_valid = this.validateMoney && this.validateCategory
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