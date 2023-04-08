<template>
  <Bar
      :options="chartOptionsPrepared"
      :data="chartDataPrepared"
  />
</template>

<script>
import {Bar} from 'vue-chartjs'
import {Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: {Bar},
  props: {
    title: {
      type: String,
      default: 'Заголовок'
    },
    indexAxis: {
      type: String,
      default: 'y'
    },
    xGrid: {
      type: Boolean,
      default: true,
    },
    xGridColor: {
      type: String,
      default: "#A7A7A7"
    },
    xTicks: {
      type: Boolean,
      default: true,
    },
    xBorder: {
      type: Boolean,
      default: true,
    },
    xBorderColor: {
      type: String,
      default: "#666666"
    },
    yGrid: {
      type: Boolean,
      default: true,
    },
    yGridColor: {
      type: String,
      default: "#A7A7A7"
    },
    yTicks: {
      type: Boolean,
      default: true,
    },
    yBorder: {
      type: Boolean,
      default: true,
    },
    yBorderColor: {
      type: String,
      default: "#666666"
    },
    gridLineWidth: {
      default: 0.3
    },
    chartData: {
      type: Object,
      default: {
        labels: [2023, 2027, 2026, 2025, 2024, 2023, 2022, 2021, 2020],
        datasets: [
          {
            label: 'Базовый сценарий',
            backgroundColor: '#FF8A1E',
            data: [1, 2, 3, 4, 5, 6, 7, 8, 9]
          },
          {
            label: 'ТОС-1',
            backgroundColor: '#3684AF',
            data: [2, 3, 4, 5, 6, 7, 8, 9, 10]
          }
        ]
      }
    }
  },
  computed: {
    chartDataPrepared() {
      return this.chartData
    },
    chartOptionsPrepared() {
      return {
        indexAxis: this.indexAxis,
        maintainAspectRatio: false,
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: this.title,
            // color: "#000000",
            font: {
              size: 12,
              family: "'Inter', sans-serif",
              style: 'normal',
              weight: 600,
            },
          },
          legend: {
            labels: {
              // color: "#000000",
              font: {
                size: 12,
                family: "'Inter', sans-serif",
                style: 'normal',
                weight: 600,
                lineHeight: '15px',
              }
            }
          },
        },
        scales: {
          y: {
            grid: {
              display: this.yGrid,
              color: this.yGridColor,
              lineWidth: this.gridLineWidth
            },
            ticks: {
              display: this.yTicks,
              // color: '#000000',
              font: {
                size: 12,
                family: "'Inter', sans-serif",
                style: 'normal',
                weight: 600,
                lineHeight: '15px',
              }
            },
            border: {
              display: false,
            },
          },
          x: {
            grid: {
              display: this.xGrid,
              color: this.xGridColor,
              lineWidth: this.gridLineWidth
            },
            ticks: {
              display: this.xTicks,
              // color: '#000000',
              font: {
                size: 12,
                family: "'Inter', sans-serif",
                style: 'normal',
                weight: 600,
                lineHeight: '15px',
              }
            },
            border: {
              display: false,
            },
          }
        }
      }
    }
  }
}
</script>