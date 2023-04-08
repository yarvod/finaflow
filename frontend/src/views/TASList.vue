<template>
  <BaseLayout>
    <template #body>
      <div class="head">
        <h4>Распределение финансирования ТОС</h4>
        <!--      <div class="rightSide">-->
        <!--        <ColorBoxes/>-->
        <!--      </div>-->
      </div>
      <SLoader v-if="loadingTASList"/>
      <div v-else class="tableWrapper">
        <table>
          <thead>
          <tr>
            <th>ТОС</th>
            <th>2003-2006</th>
            <th>2007-2030</th>
            <th>Готовность</th>
            <th>Доля импорта (стоимость)</th>
            <th>Доля импорта (продукты)</th>
            <th>УГТ</th>
          </tr>
          </thead>
          <tbody>
          <tr
              v-for="tas in tasList"
              @click="$router.push({name: 'tas_detail', params: {tasId: tas.id}})"
          >
            <td>{{ tas.name }}</td>
            <td>
              <ion-progress-bar :value="base.progress1"></ion-progress-bar>
            </td>
            <td>
              <ion-progress-bar :value="base.progress2"></ion-progress-bar>
            </td>
            <td>{{ base.date }}</td>
            <td>
              <ion-progress-bar :value="base.import_price"></ion-progress-bar>
            </td>
            <td>
              <ion-progress-bar :value="base.import_prod"></ion-progress-bar>
            </td>
            <td>
              {{ tas.trl }}
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </template>
  </BaseLayout>
</template>

<script>
import ColorBoxes from "@/components/common/ColorBoxes.vue";
import SLoader from "@/components/ui/SLoader.vue";
import graph_service from "@/api/graph_service";
import BaseLayout from "@/components/BaseLayout.vue";
import {IonProgressBar} from "@ionic/vue";

export default {
  name: "TASList",
  components: {
    BaseLayout,
    ColorBoxes,
    SLoader,
    IonProgressBar,
  },
  data() {
    return {
      tasList: [],
      loadingTASList: false,
      base: {
        name: "ТОС-1",
        progress1: 0.3,
        progress2: 0.3,
        date: 2034,
        import_price: 0.5,
        price_color: "#C0D24C",
        import_prod: 0.5,
        prod_color: "#309C34",
        trl: 50,
        trl_color: "#4CDA52",
      },
    }
  },
  async mounted() {
    this.loadingTASList = true;
    await graph_service.getTASList()
        .then(resp => {
          if (resp && resp.status === 200 && resp.data) {
            this.tasList = resp.data;
            this.loadingTASList = false;
          }
        })
  },
}
</script>

<style lang="scss" scoped>

.head {
  display: grid;
  grid-auto-flow: dense;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  grid-gap: 1em;

  h3 {
    word-break: normal;
  }
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
  //border-bottom: 1px solid $Gray200;
  max-width: 250px;
  text-overflow: ellipsis;
  overflow: hidden;
}

tbody tr {
  border-bottom: 1px solid $Gray200;

  &:hover {
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    transition: all 0.3s ease;

    @media (prefers-color-scheme: dark) {
      box-shadow: 0 2px 8px rgba(152, 133, 133, 0.33);
      border-bottom: 1px solid var(--ion-background-color);
    }
  }
}


</style>