import {createStore} from "vuex";
import user from "./user";
import mobile from "./mobile";
import operations from "./operations";
import categories from "./categories";


const store = createStore({
  state: {},
  getters: {},
  mutations: {},
  actions: {
    ResetStore (context, payload) {
      context.commit('ResetUserStore');
      context.commit('ResetOperations');
      context.commit('ResetCategories');
    }
  },
  modules: {
    user,
    mobile,
    operations,
    categories,
  },
})

export default store;
