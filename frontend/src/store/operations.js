import finance_service from "@/api/finance_service";


const state = {
  operations: [],
  loading_operations: true,
}

const getters = {
  operations : state => state.operations,
  loading_operations: state => state.loading_operations,
}

const mutations = {
  setOperations(state, payload) {
    state.operations = payload.operations;
  },
  setLoadingOperations(state, payload) {
    state.loading_operations = payload.loading_operations;
  },
  ResetOperations(state, payload) {
    state.operations = [];
  },
}


const actions = {
  async getOperations(context, payload) {
    context.commit('setLoadingOperations', {loading_operations: true})
    const response = await finance_service.getOperationsList(payload?.params);
    if (response && response.status === 200 && response.data) {
      context.commit('setOperations', {operations: response.data})
    }
    context.commit('setLoadingOperations', {loading_operations: false})
    return response?.status
  },
  async createOperation(context, payload) {
    const response = await finance_service.createOperation(payload.data);
    return response?.status
  },
  async updateOperation(context, payload) {
    const response = await finance_service.updateOperation(payload.data);
    return response?.status
  },
  async deleteOperation(context, payload) {
    const response = await finance_service.deleteOperation(payload.data);
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}