<template>
  <div class="head">
    <h3>Результаты прогнозирования</h3>
  </div>
  <SLoader v-if="loadingCharts"/>
  <div v-else class="items">
    <div class="item chart">
      <LineChart
          :chartData="charts"
          :title="'График финансирования'"
          :y-border-color="'#A7A7A7'"
          :x-border-color="'#A7A7A7'"
      />
    </div>
    <div class="item chart">
      <LineChart
          :chartData="releaseDeadLineData"
          :title="'Срок реализации'"
          :y-border-color="'#A7A7A7'"
          :x-border-color="'#A7A7A7'"
      />
    </div>
    <div class="item chart">
      <BarChart
          :chartData="importData"
          :title="'Доля импорта'"
          :index-axis="'x'"
          :x-grid="false"
          :y-grid="true"
          y-grid-color="#00000"
          :x-ticks="false"
          :y-ticks="true"
      />
    </div>
    <div class="item chart">
      <LineChart
          :chartData="VVPData"
          :title="'Динамика ВВП'"
          :index-axis="'x'"
          :x-grid="false"
          :y-grid="false"
          :y-ticks="false"
      />
    </div>
    <div class="item">
      <TASText/>
    </div>
  </div>

</template>

<script>
import SLoader from "@/components/ui/SLoader";
import graph_service from "@/api/graph_service";
import LineChart from "@/components/graph/LineChart";
import BarChart from "@/components/graph/BarChart";
import TASText from "@/views/PredictResults/TASText";


export default {
  name: "PredictResults",
  components: {
    LineChart,
    BarChart,
    SLoader,
    TASText,
  },
  data() {
    return {
      charts: {},
      loadingCharts: true,
      releaseDeadLineData: {
        labels: [2020, 2021, 2022, 20223, 2024, 2025, 2026, 2027],
        datasets: [
          {
            label: 'ТОС-1',
            data: [100, 90, 70, 65, 50, 45, 43, 20, 0].reverse(),
            backgroundColor: '#309c34'
          },
          {
            label: 'ТОС-2',
            data: [100, 80, 65, 60, 55, 40, 40, 20, 0].reverse(),
            backgroundColor: '#ff8a1e'
          }
        ]
      },
      importData: {
        labels: [1, 2, 3],
        datasets: [
          {
            label: 'По стоимости',
            data: [40, 80, 60],
            backgroundColor: '#0069B4'
          },
          {
            label: 'По объектам',
            data: [80, 30, 40],
            backgroundColor: '#FF8A1E'
          }
        ]
      },
      VVPData: {
        labels: [2020, 2021, 2022, 20223, 2024, 2025, 2026, 2027],
        datasets: [
          {
            label: 'Базовый сценарий',
            data: [100, 90, 70, 65, 50, 45, 43, 20, 0].reverse(),
            backgroundColor: '#ff8a1e'
          },
          {
            label: 'Текущий сценарий',
            data: [100, 80, 65, 60, 55, 40, 40, 20, 0].reverse(),
            backgroundColor: '#0069B4'
          }
        ]
      },
    }
  },
  async mounted() {
    this.loadingCharts = true;
    await graph_service.getTASChart()
        .then(resp => {
          if (resp && resp.status === 200 && resp.data) {
            this.charts = resp.data;
            this.loadingCharts = false;
          }
        })
  },
}
</script>

<style lang="scss" scoped>

html, body {
  overflow-y: auto;
  height: 100%;
  display: table-row;
}

.head {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.items {
  overflow-x: scroll;
  width: 100%;
  min-height: 100%;
  white-space: nowrap;
}

.item {
  display: inline-block;
  vertical-align: middle;
  width: 850px;
  padding-right: 50px;
  min-height: 100%;
}

.chart {
  min-height: 300px;
  width: 500px;
}

</style>