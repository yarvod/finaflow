<template>
  <BaseLayout head>
    <template #head>
      <ion-card-title>Аналитика</ion-card-title>
    </template>
    <template #body>
      <div class="dateFilter">
        <DateFilter
          @update="getAnalytics"
          @date="this.analytics_date = $event"
        />
      </div>
      <SLoader v-if="loading_analytics"/>
      <div v-else-if="analytics.spent || analytics.earned">
        <transition name="fade" mode="out-in" appear>
          <ion-row>
            <ion-col>
              <div class="small-card">
                <div class="label expenditure">Раход</div>
                <div class="expenditure">
                  {{ (analytics.spent).toLocaleString('ru') }} ₽
                </div>
              </div>
            </ion-col>
            <ion-col>
              <div class="small-card">
                <div class="label">Доход</div>
                <div class="revenue">
                  {{ (analytics.earned).toLocaleString('ru') }} ₽
                </div>
              </div>
            </ion-col>
          </ion-row>
        </transition>
        <ComingSoon>
          <template #text>Делаем аналитику!</template>
        </ComingSoon>
      </div>
      <EmptyOperations
        v-else
        :date="analytics_date"
      />
    </template>
  </BaseLayout>
</template>

<script>
import BaseLayout from "@/components/BaseLayout.vue";
import {IonCardTitle, IonCol, IonGrid, IonRow} from "@ionic/vue";
import DateFilter from "@/components/ui/DateFilter.vue";
import EmptyOperations from "@/components/operations/EmptyOperations.vue";
import SLoader from "@/components/ui/SLoader.vue";
import ComingSoon from "@/components/common/ComingSoon.vue";
import moment from "moment";
import {mapGetters} from "vuex";

export default {
  name: "Analytics.vue",
  components: {
    BaseLayout,
    IonCardTitle,
    DateFilter,
    SLoader,
    EmptyOperations,
    IonGrid,
    IonRow,
    IonCol,
    ComingSoon,
  },
  data() {
    return {
      analytics_date: moment().format('MMMM, YYYY'),
    }
  },
  computed: {
    ...mapGetters(['analytics', 'loading_analytics'])
  },
  async ionViewWillEnter() {
    await this.$store.dispatch('getAnalytics');
  },
  methods: {
    async getAnalytics(date_after, date_before) {
      if (date_after && date_before) {
        this.$store.commit('setAnalyticsDatesRange', {date_after: date_after, date_before: date_before});
      }
      await this.$store.dispatch('getAnalytics');
    },
  },
}
</script>

<style lang="scss" scoped>

.dateFilter {
  justify-content: center;
}

</style>