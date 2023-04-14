<template>
  <BaseLayout head>
    <template #head>
        <h4>Все операции</h4>
    </template>
    <template #body>
      <SLoader v-if="loading_operations"/>
      <div v-else-if="operations.length">
        <OperationItem
            v-for="operation in operations"
            :key="operation.id"
            :operation="operation"
        />
      </div>
    </template>
  </BaseLayout>
</template>

<script>
import SLoader from "@/components/ui/SLoader.vue";
import BaseLayout from "@/components/BaseLayout.vue";
import {IonProgressBar, IonSpinner} from "@ionic/vue";
import OperationItem from "../components/operations/OperationItem";
import {mapGetters} from "vuex";

export default {
  name: "OperationsList",
  components: {
    BaseLayout,
    SLoader,
    IonProgressBar,
    OperationItem,
    IonSpinner,
  },
  computed: {
    ...mapGetters(['operations', 'loading_operations'])
  },
  async mounted() {
    await this.$store.dispatch('getOperations');
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