<template>
  <Radar
      :data="chartData"
      :options="chartOptions"
  />
</template>

<script>
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
} from 'chart.js'
import { Radar } from 'vue-chartjs'

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
)

export default {
  name: 'RadarChart',
  components: {
    Radar
  },
  props: {
    chartData: {
      type: Object,
      default: {
        labels: ['Т1', 'Т2', 'Т3', 'Т4', 'Т5',],
        datasets: [
          {
            label: 'Оценка',
            backgroundColor: 'rgba(179,181,198,0.2)',
            borderColor: 'rgba(179,181,198,1)',
            pointBackgroundColor: 'rgba(179,181,198,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(179,181,198,1)',
            data: [
              106.76395801915824,
              95.13479406960697,
              86.95439284603894,
              90.52869546929831,
              92.51154885261361
            ]
          },
          {
            label: 'Базовый сценарий',
            backgroundColor: 'rgba(255,99,132,0.2)',
            borderColor: 'rgba(255,99,132,1)',
            pointBackgroundColor: 'rgba(255,99,132,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(255,99,132,1)',
            data: [
              90.52869546929833,
              95.13479406960697,
              95.134794069607,
              90.52869546929831,
              92.38454260265142
            ]
          }
        ]
      },
    },
    chartOptions: {
      type: Object,
      default: () => {
        return {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            title: {
              display: true,
              text: 'Достижение целей года 10'
            },
          },
        }
      }
    },
  },
  data() {
    return {}
  }
}
</script>
