import finance_service from "@/api/finance_service";


const state = {
  categories: [],
  loading_categories: true,
}

const getters = {
  categories : state => state.categories,
  loading_categories: state => state.loading_categories,
}

const mutations = {
  setCategories(state, payload) {
    state.categories = payload.categories;
  },
  setLoadingCategories(state, payload) {
    state.loading_categories = payload.loading_categories;
  },
  ResetCategories(state, payload) {
    state.categories = [];
  },
}


const actions = {
  async getCategories(context, payload) {
    context.commit('setLoadingCategories', {loading_categories: true})
    const response = await finance_service.getCategoriesList(payload.query);
    if (response && response.status === 200 && response.data) {
      context.commit('setCategories', {categories: response.data})
    }
    context.commit('setLoadingCategories', {loading_categories: false})
    return response?.status
  },
  async createCategory(context, payload) {
    const response = await finance_service.createCategory(payload.data);
    return response?.status
  },
  async updateCategory(context, payload) {
    const response = await finance_service.updateCategory(payload.data);
    return response?.status
  },
  async deleteCategory(context, payload) {
    const response = await finance_service.deleteCategory(payload.data);
    return response?.status
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}