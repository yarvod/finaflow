<template>
  <BaseLayout head>
    <template #head>
      <div class="inline-flex">
        <div
          class="h1-tab ml5"
          :class="{active: tab === 0}"
          @click="swiper.slideTo(0)"
        >
          Аналитика
        </div>
        <div
          class="h1-tab ml15"
          :class="{active: tab === 1}"
          @click="swiper.slideTo(1)"
        >
          Итоги
        </div>
      </div>
    </template>
    <template #body>
      <Swiper
        @slideChange="slideChange"
        @swiper="onSwiper"
        :space-between="10"
      >
        <SwiperSlide>
          <div class="fullSize">
            <div class="dateFilter">
              <DateFilter
                @update="getAnalytics"
                @date="analytics_date = $event"
                change_period="month"
              />
            </div>
            <SLoader v-if="loading_analytics"/>
            <div v-else-if="analytics.spent || analytics.earned">
              <transition name="fade" mode="out-in" appear>
                <ion-segment v-model="segment">
                  <ion-segment-button :value="1">
                    <div class="operation-segment">
                      <div class="label expenditure">Расход</div>
                      <div class="expenditure">
                        {{ (analytics.spent).toLocaleString('ru') }} руб
                      </div>
                    </div>
                  </ion-segment-button>
                  <ion-segment-button :value="2">
                    <div class="operation-segment">
                      <div class="label">Доход</div>
                      <div class="revenue">
                        {{ (analytics.earned).toLocaleString('ru') }} руб
                      </div>
                    </div>
                  </ion-segment-button>
                </ion-segment>
              </transition>
              <transition name="fade" mode="out-in" appear>
                <div>
                  <div v-if="segment === '1'" class="groupWrapper mt15">
                    <EmptyOperations v-if="!analytics?.spent_by_category?.length"/>
                    <div v-else>
                      <div
                        class="card hover"
                      >
                        <div class="h4">В среднем в день</div>
                        <div class="expenditure">{{ mean_day_spent().toLocaleString('ru') }} руб</div>
                      </div>
                      <div
                        class="card hover"
                        v-for="expenditure in analytics.spent_by_category"
                        :key="expenditure.category_id"
                      >
                        <div class="h3">{{ expenditure.category }}</div>
                        <div class="expenditure">{{ (expenditure.total).toLocaleString('ru') }} руб</div>
                      </div>
                    </div>
                  </div>
                  <div v-if="segment === '2'" class="groupWrapper mt15">
                    <EmptyOperations v-if="!analytics?.earned_by_category?.length"/>
                    <div v-else>
                      <div
                        class="card hover"
                      >
                        <div class="h4">В среднем в день</div>
                        <div class="revenue">{{ mean_day_earned().toLocaleString('ru') }} руб</div>
                      </div>
                      <div
                        class="card hover"
                        v-for="revenue in analytics.earned_by_category"
                        :key="revenue.category_id"
                      >
                        <div class="h3">{{ revenue.category }}</div>
                        <div class="revenue">{{ (revenue.total).toLocaleString('ru') }} руб</div>
                      </div>
                    </div>
                  </div>
                </div>
              </transition>
            </div>
            <EmptyOperations
              v-else
              :date="analytics_date"
            />
          </div>
        </SwiperSlide>
        <SwiperSlide>
          <div class="fullSize">
            <div class="dateFilter">
              <DateFilter
                @update="getResults"
                @date="results_date = $event"
                change_period="year"
              />
            </div>
            <SLoader v-if="loading_results"/>
            <div v-else-if="results.spent">
              <transition name="fade" mode="out-in" appear>
                <div>
                  <ion-row class="ion-justify-content-between">
                    <ion-col>
                      <div class="small-card">
                        <div class="label expenditure">Расходы</div>
                        <div class="expenditure">
                          {{ (results.total_spent).toLocaleString('ru') }} руб
                        </div>
                      </div>
                    </ion-col>
                    <ion-col>
                      <div class="small-card">
                        <div class="label">Доходы</div>
                        <div class="revenue">
                          {{ (results.total_earned).toLocaleString('ru') }} руб
                        </div>
                      </div>
                    </ion-col>
                  </ion-row>
                  <ResultsChart/>
                </div>
              </transition>
            </div>
          </div>
        </SwiperSlide>
      </Swiper>
    </template>
  </BaseLayout>
</template>

<script>
import BaseLayout from "@/components/BaseLayout.vue";
import {IonCardTitle, IonCol, IonGrid, IonRow, IonSegment, IonSegmentButton} from "@ionic/vue";
import DateFilter from "@/components/ui/DateFilter.vue";
import EmptyOperations from "@/components/operations/EmptyOperations.vue";
import SLoader from "@/components/ui/SLoader.vue";
import ComingSoon from "@/components/common/ComingSoon.vue";
import ResultsChart from "@/components/analytics/ResultsChart.vue";
import moment from "moment";
import {mapGetters} from "vuex";
import {Swiper, SwiperSlide} from 'swiper/vue';

import 'swiper/css';
import '@ionic/vue/css/ionic-swiper.css';

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
    Swiper,
    SwiperSlide,
    IonSegment,
    IonSegmentButton,
  },
  data() {
    return {
      analytics_date: moment().format('MMMM, YYYY'),
      results_date: moment().format('YYYY'),
      tab: 0,
      segment: '1',
      swiper: null,
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
    async getResults(date_after, date_before) {
      console.log(date_after, date_before)
      if (date_after && date_before) {
        this.$store.commit('setResultsDatesRange', {date_after: date_after, date_before: date_before});
      }
      await this.$store.dispatch('getResults');
    },
    onSwiper(swiper) {
      this.swiper = swiper;
    },
    slideChange() {
      this.tab = this.swiper.activeIndex;
    },
    mean_day_spent() {
      return this.analytics.spent / moment().day()
    },
    mean_day_earned() {
      return this.analytics.earned / moment().day()
    }
  },
}
</script>

<style lang="scss" scoped>

.dateFilter {
  justify-content: center;
}

.swiper .swiper-slide {
  text-align: start;
  height: auto;
}

ion-col {
  &:first-of-type {
    padding-left: 0;
  }

  &:last-of-type {
    padding-right: 0;
  }
}

.card {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

</style>