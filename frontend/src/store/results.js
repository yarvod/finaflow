import finance_service from "@/api/finance_service";
import moment from "moment";


const state = {
  results: {},
  loading_results: false,
  results_date_after: moment().startOf('year').format('YYYY-MM-DD'),
  results_date_before: moment().endOf('year').format('YYYY-MM-DD'),
}

const getters = {
  results: state => state.results,
  loading_results: state => state.loading_results,
  results_date_after: state => state.results_date_after,
  results_date_before: state => state.results_date_before,
}

const mutations = {
  setResults(state, payload) {
    state.results = payload.results;
  },
  setLoadingResults(state, payload) {
    state.loading_results = payload.loading_results;
  },
  setResultsDatesRange(state, payload) {
    state.results_date_after = payload.date_after;
    state.results_date_before = payload.date_before;
  },
  ResetResults(state, payload) {
    state.results = [];
    state.loading_results = false;
  },
}

const actions = {
  async getResults(context, payload) {
    context.commit('setLoadingResults', {loading_results: true});
    const params = {
      date_after: context.getters.results_date_after,
      date_before: context.getters.results_date_before,
    }
    const response = await finance_service.getResults(params);
    if (response && response.status === 200 && response.data) {
      context.commit('setResults', {results: response.data})
    }
    context.commit('setLoadingResults', {loading_results: false})
    return response?.status
  },
}

export default {
  state,
  getters,
  mutations,
  actions
}