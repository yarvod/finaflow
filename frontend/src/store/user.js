import user_service from '@/api/user_service';


const state = {
  user: {},
  isAuthenticated: false,
  loading_user: false,
}

const getters = {
  isAuthenticated: state => state.isAuthenticated,
  user: state => state.user,
  loading_user: state => state.loading_user,
}

const mutations = {
  setUser(state, payload) {
    state.user = payload.user;
    state.isAuthenticated = payload.isAuthenticated;
    state.loading_user = false;
  },
  setLoadingUser(state, payload) {
    state.loading_user = payload;
  },
  ResetUserStore(state, payload) {
    state.user = {}
    state.isAuthenticated = false
    state.loading_user = false
  }
}


const actions = {
  async LogOut (context) {
    const response = await user_service.LogOut();
    if (response && response.status === 205) {
      context.commit('ResetUserStore', {});
      localStorage.removeItem('isAuthenticated');
      localStorage.removeItem('user');
    }
  },
  async getMe (context) {
    const response = await user_service.getMe();
    if (response && response.data) {
      context.commit('setUser', {user: response.data, isAuthenticated: true})
      localStorage.setItem('user', JSON.stringify(response.data))
    }
    return response
  },
  async updateMe (context, data) {
    const response = await user_service.updateMe(data);
    if (response && response.data) {
      await context.dispatch('getMe')
    }
    return response
  },
  async LogIn (context, data) {
    const login_resp = await user_service.LogIn(data)
    if (login_resp && login_resp.status === 200) {
      await this.dispatch('getMe');
      localStorage.isAuthenticated = true;
    }
    return login_resp
  },
  async LogInGoogle (context, data) {
    const login_resp = await user_service.LogInGoogle(data)
    if (login_resp && login_resp.status === 200) {
      await this.dispatch('getMe');
      localStorage.isAuthenticated = true;
    }
    return login_resp.status
  },
  async LogInYandex (context, data) {
    const login_resp = await user_service.LogInYandex(data)
    if (login_resp && login_resp.status === 200) {
      await this.dispatch('getMe');
      localStorage.isAuthenticated = true;
    }
    return login_resp.status
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}