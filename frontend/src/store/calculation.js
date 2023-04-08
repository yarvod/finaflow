import calculation_service from "@/api/calculation_service";


const state = {
  chart_data: {},
  radar_data: {},
}

const getters = {
  chart_data: state => state.chart_data,
  radar_data: state => state.radar_data,
}

const mutations = {
  setChartData(state, payload) {
    state.chart_data = payload.chart_data;
  },
  ResetChartDataStore(state, payload) {
    state.chart_data = {}
  },
  setRadarData(state, payload) {
    state.radar_data = payload.chart_data;
  },
  ResetRadarDataStore(state, payload) {
    state.radar_data = {}
  }
}


const actions = {
  async getCalculation (context, id) {
    const response = await calculation_service.getCalculation(id);
    if (response && response.data) {
      context.commit('setChartData', {chart_data: response.data.values_data})
      context.commit('setRadarData', {chart_data: response.data.radar_values_data})
    }
    return response
  },
}


export default {
  state,
  getters,
  mutations,
  actions
}