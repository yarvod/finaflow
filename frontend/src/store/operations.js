import finance_service from "@/api/finance_service";
import moment from "moment";
import {groupBy} from "@/utils/functions";


const state = {
  operations: [],
  loading_operations: true,
  date_after: moment().startOf('month').format('YYYY-MM-DD'),
  date_before: moment().endOf('month').format('YYYY-MM-DD'),
}

const getters = {
  operations : state => state.operations,
  loading_operations: state => state.loading_operations,
  date_after: state => state.date_after,
  date_before: state => state.date_before,
}

const mutations = {
  setOperations(state, payload) {
    state.operations = payload.operations;
  },
  setLoadingOperations(state, payload) {
    state.loading_operations = payload.loading_operations;
  },
  setDatesRange(state, payload) {
    state.date_after = payload.date_after;
    state.date_before = payload.date_before;
  },
  ResetOperations(state, payload) {
    state.operations = [];
    state.loading_operations = false;
  },
}


const actions = {
  async getOperations(context, payload) {
    context.commit('setLoadingOperations', {loading_operations: true});
    const params = {
      date_after: context.getters.date_after,
      date_before: context.getters.date_before,
    }
    const response = await finance_service.getOperationsList(params);
    if (response && response.status === 200 && response.data) {
      const operations = groupBy(response.data, 'date')
      context.commit('setOperations', {operations: operations})
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
    return response?.status
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}