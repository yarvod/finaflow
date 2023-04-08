

const SET_MOBILE = 'SET_MOBILE';

const state = {
  isMobile: false
}

const getters = {
  isMobile: state => state.isMobile
}

const mutations = {
  [SET_MOBILE] (state, payload) {
    state.isMobile = payload
  }
}

const actions = {
  checkMobile (context) {
    const res = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
    context.commit(SET_MOBILE, res)
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
