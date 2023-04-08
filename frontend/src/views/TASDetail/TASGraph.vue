<template>
  <div class="main">
    <div class="head">
      <h4>Технологическая карта {{ tasDetail.name }}</h4>
    </div>
    <div class="graph_box">
      <Graph
          class="graph"
          :tas-id="tasId"
      />
    </div>
  </div>
</template>

<script>

import Graph from "@/components/graph/Graph";
import ColorBoxes from "@/components/common/ColorBoxes";
import graph_service from "@/api/graph_service";
import GraphLegend from "@/components/graph/GraphLegend";

export default {
  name: "TASGraph",
  components: {
    Graph,
    ColorBoxes,
    GraphLegend,
  },
  props: {
    tasId: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      tasDetail: {
        name: '',
      }
    }
  },
  async mounted() {
    await graph_service.getTAS(this.tasId)
        .then(resp => {
          if (resp && resp.status === 200 && resp.data) {
            this.tasDetail = resp.data
          }
        })
  }
}
</script>

<style lang="scss" scoped>

.head {
  display: grid;
  grid-auto-flow: dense;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  grid-gap: 1em;
}

.rightSide {
  display: flex;
  align-items: center;
  justify-content: end;
  position: relative;
  font-size: 12px;
  font-weight: 400;
  line-height: 12px;
}

.graph_box {
  display: flex;
  flex: 1 1 auto;
  justify-content: space-between;
}

.graph {
  display: flex;
  flex: 1 1 auto;
  align-items: stretch;
}

.main {
  min-height: 100%;
}

</style>