import Api from "@/api/Api";


export default {
  async getOperationsList() {
    return await Api().get(`/finances/operation/`)
  },
  async getOperation(operationId) {
    return await Api().get(`/finances/operation/${tasId}/`)
  },
  async updateOperation(operation) {
    return await Api().put(`/finances/operation/${operation.id}/`, operation)
  },
  async deleteOperation(operation) {
    return await Api().delete(`/finances/operation/${operation.id}/`)
  },
  async getCategoriesList() {
    return await Api().get(`/finances/category/`)
  },
}