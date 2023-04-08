<template>
  <div>
    <div :class="$style.head">
      <h3>Эффекты {{ tasDetail.name }}</h3>
    </div>
    <div :class="$style.chartsWrapper">
      <div :class="$style.chart">
        <BarChart
            :title="'Доля импорта'"
            :index-axis="'y'"
            :x-grid="false"
            :y-grid="false"
            :x-ticks="false"
        />
      </div>
      <div :class="$style.chart">
        <LineChart
            :title="'Динамика импорта в секторе А'"
            :yGrid="false"
            :xGrid="false"
            :yTicks="false"
        />
      </div>
    </div>
  </div>
</template>

<script>
import graph_service from "@/api/graph_service";
import BarChart from "@/components/graph/BarChart";
import LineChart from "@/components/graph/LineChart";

export default {
  name: "TASCharts",
  components: {
    LineChart,
    BarChart,
  },
  props: {
    tasId: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      tasDetail: {},
      loading_tas: true,
    }
  },
  async mounted() {
    this.loading_tas = true;
    await graph_service.getTAS(this.tasId)
        .then(resp => {
          if (resp && resp.status === 200 && resp.data) {
            this.tasDetail = resp.data
            this.loading_tas = false;
          }
        })
  },
}
</script>

<style lang="scss" module>

.head {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.chartsWrapper {
  display: grid;
  grid-auto-flow: dense;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  grid-gap: 1em;
}

.chart {
  display: flex;
  flex: 1 1 auto;
  min-height: 350px;
}

</style>