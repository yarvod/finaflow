import finance_service from "@/api/finance_service";
import moment from "moment";


const state = {
  analytics: {},
  loading_analytics: false,
  analytics_date_after: moment().startOf('month').format('YYYY-MM-DD'),
  analytics_date_before: moment().endOf('month').format('YYYY-MM-DD'),
}

const getters = {
  analytics: state => state.analytics,
  loading_analytics: state => state.loading_analytics,
  analytics_date_after: state => state.analytics_date_after,
  analytics_date_before: state => state.analytics_date_before,
}

const mutations = {
  setAnalytics(state, payload) {
    state.analytics = payload.analytics;
  },
  setLoadingAnalytics(state, payload) {
    state.loading_analytics = payload.loading_analytics;
  },
  setAnalyticsDatesRange(state, payload) {
    state.analytics_date_after = payload.date_after;
    state.analytics_date_before = payload.date_before;
  },
  ResetAnalytics(state, payload) {
    state.analytics = [];
    state.loading_analytics = false;
  },
}

const actions = {
  async getAnalytics(context, payload) {
    context.commit('setLoadingAnalytics', {loading_analytics: true});
    const params = {
      date_after: context.getters.analytics_date_after,
      date_before: context.getters.analytics_date_before,
    }
    console.log(params)
    const response = await finance_service.getAnalytics(params);
    if (response && response.status === 200 && response.data) {
      context.commit('setAnalytics', {analytics: response.data})
    }
    context.commit('setLoadingAnalytics', {loading_analytics: false})
    return response?.status
  },
}

export default {
  state,
  getters,
  mutations,
  actions
}