<template>
  <div class="dateFilter">
    <ion-button
      fill="clear"
      @click="sub_month"
    >
      <ion-icon slot="icon-only" :icon="icons.arrowBackCircle"></ion-icon>
    </ion-button>
    <div class="date">
      {{ date_format }}
    </div>
    <ion-button
      fill="clear"
      @click="add_month"
    >
      <ion-icon slot="icon-only" :icon="icons.arrowForwardCircle"></ion-icon>
    </ion-button>
  </div>
</template>

<script>
import {IonButton, IonIcon} from "@ionic/vue";
import {arrowBackCircle, arrowForwardCircle} from "ionicons/icons";
import moment from "moment";

export default {
  name: "DateFilter",
  components: {
    IonButton,
    IonIcon,
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
      return moment(this.date).format('MMMM, YYYY')
    },
    date_after() {
      return moment(this.date).startOf('month').format('YYYY-MM-DD');
    },
    date_before() {
      return moment(this.date).endOf('month').format('YYYY-MM-DD');
    },
  },
  methods: {
    async add_month() {
      this.date = new Date(this.date.setMonth(this.date.getMonth() + 1));
      this.$emit('date', this.date_format);
      await this.$emit('update', this.date_after, this.date_before);
    },
    async sub_month() {
      this.date = new Date(this.date.setMonth(this.date.getMonth() - 1));
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