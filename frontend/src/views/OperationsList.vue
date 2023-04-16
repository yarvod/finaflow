<template>
  <BaseLayout head>
    <template #head>
      <ion-card-title>Все операции</ion-card-title>
    </template>
    <template #body>
      <div class="dateFilter">
        <DateFilter
          @update="getOperations"
          @date="this.operations_date = $event"
        />
      </div>
      <SLoader v-if="loading_operations"/>
      <div v-else-if="operations.length">
        <transition name="fade" mode="out-in" appear>
          <div>
            <OperationItem
              v-for="operation in operations"
              :key="operation.id"
              :operation="operation"
            />
          </div>
        </transition>
      </div>
      <EmptyOperations
        v-else
        :date="operations_date"
      >
        <template #action>
          <ion-button
            @click="openModal"
            color="success"
          >
            Добавить!
          </ion-button>
        </template>
      </EmptyOperations>
    </template>
  </BaseLayout>
</template>

<script>
import SLoader from "@/components/ui/SLoader.vue";
import BaseLayout from "@/components/BaseLayout.vue";
import {IonButton, IonCardTitle, IonProgressBar, IonSpinner, modalController} from "@ionic/vue";
import OperationItem from "../components/operations/OperationItem.vue";
import {mapGetters} from "vuex";
import EmptyOperations from "@/components/operations/EmptyOperations.vue";
import OperationModal from "@/components/operations/OperationModal.vue";
import DateFilter from "@/components/ui/DateFilter.vue"
import moment from "moment";

export default {
  name: "OperationsList",
  components: {
    BaseLayout,
    SLoader,
    IonProgressBar,
    OperationItem,
    IonSpinner,
    IonCardTitle,
    EmptyOperations,
    IonButton,
    DateFilter,
  },
  data() {
    return {
      operations_date: moment().format('MMMM, YYYY'),
    }
  },
  computed: {
    ...mapGetters(['operations', 'loading_operations'])
  },
  async ionViewWillEnter() {
    const date_after = moment().startOf('month').format('YYYY-MM-DD');
    const date_before = moment().endOf('month').format('YYYY-MM-DD');
    await this.getOperations(date_after, date_before)
  },
  methods: {
    async getOperations(date_after, date_before) {
      await this.$store.dispatch('getOperations', {params: {date_after: date_after, date_before: date_before}});
    },
    async openModal() {
      const modal = await modalController.create({
        component: OperationModal,
        presentingElement: this.presentingElement,
        canDismiss: true,
      });
      modal.present();
      const {data, role} = await modal.onWillDismiss();
    },
  },
}
</script>

<style lang="scss" scoped>

.dateFilter {
  justify-content: center;
}

.head {
  display: grid;
  grid-auto-flow: dense;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  grid-gap: 1em;

  h3 {
    word-break: normal;
  }
}

.rightSide {
  display: flex;
  align-items: center;
  justify-content: end;
  position: relative;
  font-size: 12px;
  font-weight: 400;
  line-height: 12px;
}
</style>