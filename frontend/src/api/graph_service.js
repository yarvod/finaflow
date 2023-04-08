import Api from "@/api/Api";


export default {
  async getTASList() {
    return await Api().get(`/graph/tas/`)
  },
  async getTASChart() {
    return await Api().get(`/graph/tas/charts`)
  },
  async getTAS(tasId) {
    return await Api().get(`/graph/tas/${tasId}/`)
  },
  async getTASGraph(tasId) {
    return await Api().get(`/graph/tas/${tasId}/graph`)
  },
}