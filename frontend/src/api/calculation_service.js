import Api from "@/api/Api";


export default {
  async getCalculations(params) {
    return await Api().get('/calculation/', {params})
  },
  async getCalculation(id) {
    return await Api().get(`/calculation/${id}/`)
  },
  async createCalculation(data, onUploadProgress) {
    return await Api(true).post(`/calculation/`, data, {onUploadProgress})
  },
  async testCalculation(data, onUploadProgress) {
    return await Api().post(`/calculation/test/`, data)
  },
}