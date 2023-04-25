<template>
  <Bar :data="bar_data" :options="options"/>
</template>

<script>
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js';
import {Bar} from 'vue-chartjs';
import {mapGetters} from "vuex";
import {getMonthName} from "@/utils/functions";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default {
  name: "ResultsChart",
  components: {
    Bar,
  },
  data() {
    return {
      options: {
        responsive: true,
        maintainAspectRatio: true
      },
    }
  },
  computed: {
    ...mapGetters(['results']),
    bar_data() {
      let labels = this.results.labels.map(x => getMonthName(x))
      return {
        labels: labels,
        datasets:
          [
            {
              label: 'Расходы',
              backgroundColor: '#ed5e64',
              data: this.results.spent
            },
            {
              label: 'Доходы',
              backgroundColor: '#5ccc8b',
              data: this.results.earned,
            }
          ]
      }
    },
  }
}
</script>

<style scoped>

</style>