import axios from 'axios'
import router from "@/router";
import store from "@/store";

export const backendAPIURL = '/api/'
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default (file = false) => {

  const headers = file ? {
    'Content-Type': 'multipart/form-data; boundary=<calculated when request is sent>',
  } : {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }

  const Api = axios.create({
    baseURL: backendAPIURL,
    withCredentials: true,
    headers
  })

  Api.interceptors.request.use((config) => {
    return config;
  });

  Api.interceptors.response.use(
    (response) => {
      return response;
    },
    async (error) => {
      if (error.response.status === 401) {
        const response = await axios.post(`${backendAPIURL}auth/token/refresh/`)
          .catch((err) => {
            localStorage.removeItem('isAuthenticated');
            localStorage.removeItem('user');
            router.push({name: 'operations'});
            store.commit('setUser', {})
          });
        if (response && response.status === 200) {
          return axios(error.config);
        }
      } else {
        return Promise.reject(error);
      }
    }
  );
  return Api;
}
