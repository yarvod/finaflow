<template>
  <div>
    <div class="head">
      <h4>Информация о {{ tasDetail.name }}</h4>
      <ColorBoxes class="rightBox"/>
    </div>
    <SLoader v-if="loading_tas"/>
    <div
        v-else
        class="tableWrapper"
    >
      <table ref="table">
        <thead>
        <tr>
          <th>
            КТЭ ТОС
          </th>
          <th v-for="year in tasDetail.kte_set.years" :key="year">
            {{ year }}
          </th>
        </tr>
        </thead>
        <tbody>
        <tr
            v-for="kte in tasDetail.kte_set.ktes"
            :key="kte.id"
        >
          <td class="kteName">
            {{ kte.name }}
          </td>
          <td
              v-for="year in tasDetail.kte_set.years"
              :key="year"
          >
            <Box
                :id="`${kte.id}_${year}`"
                v-if="findFinance(kte, year)"
                :color="findFinance(kte, year).import_color"
                radius="3px"
            >
              {{ findFinance(kte, year)?.money }}
            </Box>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import graph_service from "@/api/graph_service";
import ColorBoxes from "@/components/common/ColorBoxes";
import SLoader from "@/components/ui/SLoader";
import Box from "@/components/ui/Box";
import LeaderLine from 'leader-line-vue';
import AnimEvent from "anim-event";
import {ref} from "vue";

const table = ref();

export default {
  name: "TASInfo",
  components: {
    ColorBoxes,
    SLoader,
    Box,
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
      tasGraph: {},
      loading_tas: true,
      leaderLines: [],
      scrollListener: AnimEvent.add(() => {
          this.leaderLines.forEach(line => line.position())
        }),
    }
  },
  async mounted() {
    this.loading_tas = true;
    await Promise.all([
      await graph_service.getTAS(this.tasId),
      await graph_service.getTASGraph(this.tasId),
    ]).then(([respDetail, respGraph]) => {
      if (respDetail.status === 200 && respDetail.status === 200) {
        this.tasDetail = respDetail?.data;
        this.tasGraph = respGraph?.data;
        this.loading_tas = false;
      }
    }).catch((err) => {
      console.log(err)
    })
    this.drawArrows();
    await document.querySelector('ion-content').getScrollElement()
      .then(el => {
        el.addEventListener('scroll', this.scrollListener, false);
        el.addEventListener('resize', this.scrollListener, false);
      });
    this.$refs.table.addEventListener('scroll', this.scrollListener, false);
    this.$refs.table.addEventListener('resize', this.scrollListener, false);
    window.addEventListener('scroll', this.scrollListener, false);
    window.addEventListener('resize', this.scrollListener, false);
  },
  unmounted() {
    this.leaderLines.forEach(line => line.remove())
    AnimEvent.remove(this.scrollListener)
    document.querySelector('ion-content').getScrollElement()
        .then(el => {
          el.removeEventListener('scroll', this.scrollListener)
          el.removeEventListener('resize', this.scrollListener)
        });
    window.removeEventListener('scroll', this.scrollListener)
    window.removeEventListener('resize', this.scrollListener)
  },
  methods: {
    findFinance(kte, year) {
      return kte.ktefinancing_set.find(item => item.year === year)
    },
    drawArrows() {
      const lines = this.tasGraph.links_info
      for (let ind in lines) {
        let line = LeaderLine.setLine(
            document.getElementById(lines[ind].kte_from),
            document.getElementById(lines[ind].kte_to),
            {
              color: '#0069b4',
              size: 2,
              path: 'arc',
              startPlug: 'square',
              dash: {animation: true}
            }
        )
        this.leaderLines.push(line);
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.head {
  display: grid;
  grid-auto-flow: dense;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 1em;
  align-items: center;
  justify-items: auto;
}

.rightBox {
  justify-self: end;
}

.tableWrapper {
  margin-top: 20px;
  display: flex;
  width: 100%;
  justify-content: center;
}

table {
  display: block;
  overflow: auto;
  white-space: nowrap;
  padding: 6px;
}

th {
  padding: 30px 10px;
  font-style: normal;
  color: $Gray500;
  font-weight: 550;
  font-size: 16px;
  line-height: 15px;
  text-align: left;
  border-bottom: 1px solid $Gray200;
}

td {
  padding: 20px 10px;
  text-align: left;
  align-items: center;
  border-bottom: 1px solid $Gray200;
  max-width: 250px;
  text-overflow: ellipsis;
  overflow: hidden;
}

tbody tr {
  &:hover {
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    transition: all 0.3s ease;
  }
}

</style>