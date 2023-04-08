<template>
  <base-layout head>
    <template #head>
      <ion-segment @SegmentChangeEventDetail="changeTab($event)" v-model="currentTab">
        <ion-segment-button value="tech_map">
          <ion-label>Тех. карта</ion-label>
        </ion-segment-button>
        <ion-segment-button value="info">
          <ion-label>Информация</ion-label>
        </ion-segment-button>
        <ion-segment-button value="effect">
          <ion-label>Эффекты</ion-label>
        </ion-segment-button>
      </ion-segment>
    </template>
    <template #body>
      <div :class="$style.tabContent">
        <TASGraph
            v-if="currentTab === 'tech_map'"
            :tas-id="tasId"
        />
        <TASInfo
            v-if="currentTab === 'info'"
            :tas-id="tasId"
        />
        <TASCharts
            v-if="currentTab === 'effect'"
            :tas-id="tasId"
        />
      </div>
    </template>
  </base-layout>
</template>

<script>
import TASGraph from "@/views/TASDetail/TASGraph";
import TASInfo from "@/views/TASDetail/TASInfo";
import TASCharts from "@/views/TASDetail/TASCharts";
import BaseLayout from "@/components/BaseLayout";
import {IonLabel, IonSegment, IonSegmentButton} from "@ionic/vue";

export default {
  name: "TASDetail",
  components: {
    BaseLayout,
    IonLabel,
    IonSegmentButton,
    IonSegment,
    TASGraph,
    TASInfo,
    TASCharts,
  },
  data() {
    return {
      currentTab: 'tech_map'
    }
  },
  computed: {
    tasId() {
      return this.$route.params.tasId
    },
  },
  methods: {
    changeTab(e) {
      console.log(e.detail.value)
      this.currentTab = e.detail.value;
    },
  }
}
</script>

<style lang="scss" module>

.tabs:global(.tab-list._new) {

  :global(.tab-list__container) {
    background-color: $white;
    padding: 1px;
    overflow-x: auto;
    overflow-y: hidden;
    white-space: nowrap;
  }

  @include respond-to(mobile) {
    :global(.tab-list__container) {
      border: none;
    }

    :global(.tab-list__tab) {
      margin: 0;
      padding: 7px 12px;

      &:first-child,
      &:last-child {
        margin-right: 0;
        margin-left: 0;
      }
    }
  }

  @include respond-to(mobile-sm) {
    :global(.tab-list__tab) {
      padding: 5px 7px;
    }
  }
}

.tabContent {
  margin-top: 20px;
  min-height: 100%;
}

.items {
  overflow-x: scroll;
  width: 100%;
  height: 100%;
  white-space: nowrap;
}

.item {
  display: inline-block;
  vertical-align: top;
  width: 100%;
  min-height: 100%;
  padding-right: 50px;
}

</style>