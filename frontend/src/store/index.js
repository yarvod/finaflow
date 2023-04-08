import {createStore} from "vuex";
import user from "./user";
import mobile from "./mobile";
import graph from "./graph";


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
  },
})

export default store;
