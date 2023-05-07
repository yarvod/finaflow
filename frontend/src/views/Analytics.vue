<template>
  <BaseLayout head>
    <template #head>
      <div class="inline-flex">
        <div
          class="h1-tab clickable"
          :class="{active: tab === 1}"
          @click="tab = 1"
        >
          Аналитика
        </div>
        <div
          class="h1-tab clickable ml10"
          :class="{active: tab === 2}"
          @click="tab = 2"
        >
          Итоги
        </div>
      </div>
    </template>
    <template #body>
      <div v-if="tab === 1">
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
                  <div class="label expenditure">Расход</div>
                  <div class="expenditure">
                    {{ (analytics.spent).toLocaleString('ru') }} руб
                  </div>
                </div>
              </ion-col>
              <ion-col>
                <div class="small-card">
                  <div class="label">Доход</div>
                  <div class="revenue">
                    {{ (analytics.earned).toLocaleString('ru') }} руб
                  </div>
                </div>
              </ion-col>
            </ion-row>
          </transition>
          <ComingSoon>
            <template #text>Скоро больше аналитики!</template>
          </ComingSoon>
        </div>
        <EmptyOperations
          v-else
          :date="analytics_date"
        />
      </div>
      <div v-if="tab === 2">
        <br>
        <SLoader v-if="loading_results"/>
        <div v-else-if="results.spent">
          <transition name="fade" mode="out-in" appear>
            <ResultsChart/>
          </transition>
        </div>
      </div>
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
import ResultsChart from "@/components/analytics/ResultsChart.vue";
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
    ResultsChart,
  },
  data() {
    return {
      analytics_date: moment().format('MMMM, YYYY'),
      tab: 1,
    }
  },
  computed: {
    ...mapGetters(['analytics', 'loading_analytics', 'results', 'loading_results'])
  },
  async ionViewWillEnter() {
    await this.$store.dispatch('getAnalytics');
    await this.$store.dispatch('getResults');
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