<template>
  <div class="dateFilter">
    <ion-button
      fill="clear"
      @click="sub"
    >
      <ion-icon slot="icon-only" :icon="icons.arrowBackCircle"></ion-icon>
    </ion-button>
    <div class="date">
      {{ date_format }}
    </div>
    <ion-button
      fill="clear"
      @click="add"
    >
      <ion-icon slot="icon-only" :icon="icons.arrowForwardCircle"></ion-icon>
    </ion-button>
  </div>
</template>

<script>
import {IonButton, IonIcon} from "@ionic/vue";
import {arrowBackCircle, arrowForwardCircle} from "ionicons/icons";
import moment from "moment";

moment.locale('ru')
export default {
  name: "DateFilter",
  components: {
    IonButton,
    IonIcon,
  },
  props: {
    change_period: {
      type: String,
      default: 'month',
    }
  },
  data() {
    return {
      icons: {
        arrowBackCircle: arrowBackCircle,
        arrowForwardCircle: arrowForwardCircle,
      },
      date: new Date(),
    }
  },
  computed: {
    date_format() {
      if (this.change_period === 'month') {
        return moment(this.date).format('MMMM, YYYY')
      }
      return moment(this.date).format('YYYY')
    },
    date_after() {
      return moment(this.date).startOf(this.change_period).format('YYYY-MM-DD');
    },
    date_before() {
      return moment(this.date).endOf(this.change_period).format('YYYY-MM-DD');
    },
  },
  methods: {
    async add() {
      if (this.change_period === 'month') {
        this.date = new Date(this.date.setMonth(this.date.getMonth() + 1));
      } else {
        this.date = new Date(this.date.setFullYear(this.date.getFullYear() + 1));
      }
      this.$emit('date', this.date_format);
      await this.$emit('update', this.date_after, this.date_before);
    },
    async sub() {
      if (this.change_period === 'month') {
        this.date = new Date(this.date.setMonth(this.date.getMonth() - 1));
      } else {
        this.date = new Date(this.date.setFullYear(this.date.getFullYear() - 1));
      }
      this.$emit('date', this.date_format);
      await this.$emit('update', this.date_after, this.date_before);
    }
  },
}
</script>

<style lang="scss" scoped>

.dateFilter {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.date {
  margin-left: 5px;
  margin-right: 5px;
  font-weight: bolder;
  color: $Base1;
}

</style>