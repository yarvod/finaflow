import Api from './Api';

export default {
  async LogOut () {
    return await Api().post(`/auth/logout/`)
  },
  async LogIn (data) {
    return await Api().post(`/auth/login/`, data)
  },
  async LogInGoogle (data) {
    return await Api().post(`/auth/login/social/google`, data)
  },
  async LogInYandex (data) {
    return await Api().post(`/auth/login/social/yandex`, data)
  },
  async getMe () {
    return await Api().get(`/users/`)
  },
  async updateMe (data) {
    return await Api().put(`/users/`, data)
  },
  async activate (data) {
    return await Api().post(`/auth/activate/`, data)
  },
  async activateResend (data) {
    return await Api().post(`/auth/activate/resend/`, data)
  },
  async createUser (data) {
    return await Api().post(`/auth/register/`, data)
  },
  async passwordResetConfirm (data) {
    return await Api().post(`/auth/password/reset/confirm/`, data)
  },
  async passwordReset (data) {
    return await Api().post(`/auth/password/reset/`, data)
  },
  async checkEmail (data) {
    return await Api().post(`/auth/check_email/`, data)
  },
}