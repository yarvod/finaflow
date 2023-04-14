import Api from "@/api/Api";


export default {
  async getOperationsList() {
    return await Api().get(`/finances/operation/`)
  },
  async getOperation(operationId) {
    return await Api().get(`/finances/operation/${operationId}/`)
  },
  async createOperation(data) {
    return await Api().post(`/finances/operation/`, data)
  },
  async updateOperation(operation) {
    return await Api().put(`/finances/operation/${operation.id}/`, operation)
  },
  async deleteOperation(operation) {
    return await Api().delete(`/finances/operation/${operation.id}/`)
  },
  async getCategoriesList(params) {
    return await Api().get(`/finances/category/`, {params: params})
  },
  async getCategory(categoryId) {
    return await Api().get(`/finances/category/${categoryId}/`)
  },
  async createCategory(data) {
    return await Api().post(`/finances/category/`, data)
  },
  async updateCategory(category) {
    return await Api().put(`/finances/operation/${category.id}/`, category)
  },
  async deleteCategory(category) {
    return await Api().delete(`/finances/operation/${category.id}/`)
  },
}