<template>
  <Line
      :data="chartDataPrepared"
      :options="chartOptionsPrepared"
  />
</template>

<script>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import {Line} from 'vue-chartjs'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)

export default {
  name: 'LineChart',
  components: {
    Line
  },
  props: {
    chartData: {
      type: Object,
      default: {
        labels: ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033'],
        datasets: [
          {
            label: 'Базовый сценарий',
            data: [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            backgroundColor: '#FF8A1E',
            borderColor: '#FF8A1E',
            pointStyle: 'circle',
            pointRadius: 5,
            borderWidth: 1,
          },
          {
            label: 'ТОС-1',
            backgroundColor: '#3684AF',
            data: [9, 7, 6, 5, 6, 4, 3, 5, 2, 3, 4],
            borderColor: '#3684AF',
            pointStyle: 'circle',
            pointRadius: 5,
            borderWidth: 1,
          }
        ]
      },
    },
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
    }
  },
  computed: {
    chartDataPrepared() {
      let datasets = []
      for (let i in this.chartData.datasets) {
        let dataset = {
          label: this.chartData.datasets[i].label,
          data: this.chartData.datasets[i].data,
          borderColor: this.chartData.datasets[i].backgroundColor,
          backgroundColor: this.chartData.datasets[i].backgroundColor,
          pointStyle: 'circle',
          pointRadius: 5,
          borderWidth: 1,
        }
        datasets.push(dataset)
      }
      return {
        labels: this.chartData.labels,
        datasets: datasets,
      }
    },
    chartOptionsPrepared() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: {
            // color: "#000000",
            display: true,
            text: this.title,
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
              display: this.yBorder,
              color: this.yBorderColor,
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
              display: this.xBorder,
              color: this.xBorderColor,
            },
          },
        }
      }
    }
  },
}
</script>
