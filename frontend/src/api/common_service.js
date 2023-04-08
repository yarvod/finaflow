import Api from "@/api/Api";


export default {
  async getSectors(params) {
    return await Api().get('/common/sector/', {params})
  },
  async getSector(slug) {
    return await Api().get(`/common/sector/${slug}/`)
  },
  async getIndicators(params) {
    return await Api().get('/common/indicator/', {params})
  },
  async getIndicator(slug) {
    return await Api().get(`/common/indicator/${slug}/`)
  },
  async getDataFile(params) {
    return await Api().get('/common/datafile/', {params})
  },
}