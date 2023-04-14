import {createStore} from "vuex";
import user from "./user";
import mobile from "./mobile";
import graph from "./graph";
import operations from "./operations";
import categories from "./categories";


const store = createStore({
  state: {},
  getters: {},
  mutations: {},
  actions: {
    ResetStore (context, payload) {
    }
  },
  modules: {
    user,
    mobile,
    graph,
    operations,
    categories,
  },
})

export default store;
