<template>
  <div style="display: block">
    <div class="head">
      <div class="headLeft">
        <div class="key">
          <div class="boxBtn">
            <div :class="{holding: configs.view.panEnabled}">Shift</div>
          </div>
          <div>Панарамирование</div>
        </div>
        <div class="key">
          <div class="boxBtn">
            <div :class="{holding: configs.view.zoomEnabled}">Ctrl</div>
          </div>
          <div>Масштабирование</div>
        </div>
      </div>
      <div class="headRight">
        <GraphLegend/>
      </div>
    </div>
    <div class="key">
      <ion-button @click="$refs.graph.fitToContents()" fill="clear">
        <ion-icon :icon="scanOutline" slot="icon-only"></ion-icon>
      </ion-button>
      <ion-buttons>
        <ion-button @click="$refs.graph.zoomIn()" fill="clear">
          <ion-icon :icon="addOutline" slot="icon-only"></ion-icon>
        </ion-button>
        <ion-button @click="$refs.graph.zoomOut()" fill="clear">
          <ion-icon :icon="removeOutline" slot="icon-only"></ion-icon>
        </ion-button>
      </ion-buttons>
    </div>
    <SLoader v-if="loading_graph"/>
    <div
        v-else
        class="graph_wrapper"
    >
      <v-network-graph
          ref="graph"
          :nodes="dgraph.nodes"
          :edges="dgraph.links"
          :layouts="dgraph.layouts"
          :configs="configs"
      />
    </div>
  </div>
</template>

<script>
import dagre from "dagre/dist/dagre.min.js"
import {ref} from "vue";
import SLoader from "@/components/ui/SLoader.vue";
import GraphLegend from "@/components/graph/GraphLegend.vue";
import graph_service from "@/api/graph_service";
import {IonButton, IonButtons, IonIcon} from "@ionic/vue";
import {scanOutline, addOutline, removeOutline} from "ionicons/icons";


const graph = ref();
const holdingShift = ref(false)
const holdingCtrl = ref(false)


export default {
  name: "Graph",
  components: {
    SLoader,
    GraphLegend,
    IonButton,
    IonIcon,
    IonButtons,
  },
  props: {
    tasId: String,
  },
  data() {
    return {
      grayColor: "#6f6f6f",
      scanOutline: scanOutline,
      addOutline: addOutline,
      removeOutline: removeOutline,
      dgraph: {},
      loading_graph: false,
      nodeSize: 40,
    }
  },
  computed: {
    configs() {
      return {
        view: {
          scalingObjects: true,
          get panEnabled() {
            return holdingShift.value
          },
          get zoomEnabled() {
            return holdingCtrl.value
          },
        },
        node: {
          draggable: false,
          normal: {
            color: "transparent",
            strokeWidth: 1,
            strokeColor: this.grayColor,
            type: 'rect',
            borderRadius: this.nodeRadius
          },
          label: {
            fontSize: 14,
            color: this.grayColor,
            directionAutoAdjustment: true,
            // direction: 'center',
            // background: {
            //   visible: true,
            //   color: "#9bade4",
            // },
          },
        },
        edge: {
          marker: {
            target: {
              type: "arrow",
              width: 4,
              height: 4,
            },
          },
          margin: 10,
        }
      }
    }
  },
  async mounted() {
    await graph_service.getTASGraph(this.tasId)
        .then(resp => {
          if (resp && resp.status === 200) {
            this.dgraph = resp.data;
            this.layout('BT');
          }
        })
    this.$refs.graph.fitToContents();
    document.addEventListener("keydown", this.onKeyDown)
    document.addEventListener("keyup", this.onKeyUp)
  },
  unmounted() {
    document.removeEventListener("keydown", this.onKeyDown)
    document.removeEventListener("keyup", this.onKeyUp)
  },
  methods: {
    nodeColor(nodeId) {
      const node = this.dgraph.nodes[nodeId]
      if (node.type === 'TAS') {
        return "white"
      } else {
        return node.import_color
      }
    },
    nodeRadius(node) {
      if (node.type === 'TAS' || node.type === 'development') {
        return 20
      } else {
        return 3
      }
    },
    onKeyDown(e) {
      if (e.shiftKey) holdingShift.value = true
      if (e.ctrlKey) holdingCtrl.value = true
    },
    onKeyUp(e) {
      if (!e.shiftKey) holdingShift.value = false
      if (!e.ctrlKey) holdingCtrl.value = false
    },
    layout(direction) {
      if (Object.keys(this.dgraph.nodes).length <= 1 || Object.keys(this.dgraph.links).length === 0) {
        return
      }

      // convert graph
      // ref: https://github.com/dagrejs/dagre/wiki
      const g = new dagre.graphlib.Graph()
      // Set an object for the graph label
      g.setGraph({
        rankdir: direction,
        nodesep: this.nodeSize * 2,
        edgesep: this.nodeSize,
        ranksep: this.nodeSize * 2,
      })
      // Default to assigning a new object as a label for each new edge.
      g.setDefaultEdgeLabel(() => ({}))

      // Add nodes to the graph. The first argument is the node id. The second is
      // metadata about the node. In data case we're going to add labels to each of
      // our nodes.
      Object.entries(this.dgraph.nodes).forEach(([nodeId, node]) => {
        g.setNode(nodeId, {label: node.name, width: node.name.length * 10, height: this.nodeSize})
      })

      // Add edges to the graph.
      Object.values(this.dgraph.links).forEach(edge => {
        g.setEdge(edge.source, edge.target)
      })

      dagre.layout(g)

      const box = {}
      g.nodes().forEach((nodeId) => {
        // update node position
        const x = g.node(nodeId).x
        const y = g.node(nodeId).y
        this.dgraph.layouts.nodes[nodeId] = {x, y}

        // calculate bounding box size
        box.top = box.top ? Math.min(box.top, y) : y
        box.bottom = box.bottom ? Math.max(box.bottom, y) : y
        box.left = box.left ? Math.min(box.left, x) : x
        box.right = box.right ? Math.max(box.right, x) : x
      })

      const graphMargin = this.nodeSize * 2
      const viewBox = {
        top: (box.top ?? 0) - graphMargin,
        bottom: (box.bottom ?? 0) + graphMargin,
        left: (box.left ?? 0) - graphMargin,
        right: (box.right ?? 0) + graphMargin,
      }
      graph.value?.setViewBox(viewBox)
    }
  }
}
</script>

<style lang="scss" scoped>

.head {
  display: grid;
  grid-auto-flow: dense;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  grid-gap: 1em;
  align-items: center;

  .headLeft {
    //display: flex;
    //flex-direction: column;
    //justify-content: start;
    //align-items: center;
    justify-self: start;
  }

  .headRight {
    //display: flex;
    //justify-content: end;
    justify-self: end;
  }
}

.graph_wrapper {
  margin-top: 10px;
  width: 100%;
  height: 700px;
  border: 0.3px solid $Gray200;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.33);
  border-radius: 10px;
}

rect {
  stroke-width: 1;
  stroke: rgb(0, 0, 0);
}

.key {
  margin-top: 3px;
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
  font-size: 12px;
  color: #666;
}

.boxBtn {
  margin-right: 4px;
  text-align: center;
  width: 50px;
  padding: 0;
  border-radius: 4px;
  border: 1px solid #ddd;
  color: #bbb;
  background-color: #eee;
}

.boxBtn div.holding {
  border-color: #888;
  color: #444;
  background-color: #ccc;
}

</style>