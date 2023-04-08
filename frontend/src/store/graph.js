import graph_service from "@/api/graph_service";


const state = {
  dgraph: {
    links: {},
    nodes: {},
    layouts: {
      nodes: {},
    }
  },
  loading_graph: true,
}

const getters = {
  dgraph : state => state.dgraph,
  loading_graph: state => state.loading_graph,
}

const mutations = {
  setGraph(state, payload) {
    state.dgraph = payload.dgraph;
  },
  setLoadingGraph(state, payload) {
    state.loading_graph = payload.loading_graph;
  },
  ResetGraph(state, payload) {
    state.dgraph = []
  },
}


const actions = {
  async getGraph (context, payload) {
    context.commit('setLoadingGraph', {loading_graph: true})
    const response = await graph_service.getTASGraph(payload.tasId);
    if (response && response.data) {
      context.commit('setGraph', {dgraph: response.data})
      context.commit('setLoadingGraph', {loading_graph: false})
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