<template>
  <BaseLayout head>
    <template #head>
      <div class="inline-flex">
        <div
          class="h1-tab"
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
      >
        <SwiperSlide>
          <div class="fullSize">
            <div class="dateFilter">
              <DateFilter
                @update="getAnalytics"
                @date="this.analytics_date = $event"
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
              <ComingSoon>
                <template #text>Скоро больше аналитики!</template>
              </ComingSoon>
            </div>
            <EmptyOperations
              v-else
              :date="analytics_date"
            />
          </div>
        </SwiperSlide>
        <SwiperSlide>
          <div class="fullSize">
            <br>
            <SLoader v-if="loading_results"/>
            <div v-else-if="results.spent">
              <div class="h3">За 2023 год</div>
              <transition name="fade" mode="out-in" appear>
                <ResultsChart/>
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
      tab: 0,
      segment: 1,
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
    onSwiper(swiper) {
      this.swiper = swiper;
    },
    slideChange() {
      this.tab = this.swiper.activeIndex;
    },
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

</style>