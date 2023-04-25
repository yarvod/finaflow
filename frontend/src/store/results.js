import finance_service from "@/api/finance_service";


const state = {
  results: {},
  loading_results: false,
}

const getters = {
  results: state => state.results,
  loading_results: state => state.loading_results,
}

const mutations = {
  setResults(state, payload) {
    state.results = payload.results;
  },
  setLoadingResults(state, payload) {
    state.loading_results = payload.loading_results;
  },
  ResetResults(state, payload) {
    state.results = [];
    state.loading_results = false;
  },
}

const actions = {
  async getResults(context, payload) {
    context.commit('setLoadingResults', {loading_results: true});
    const response = await finance_service.getResults();
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