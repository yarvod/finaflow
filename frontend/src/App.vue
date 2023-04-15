<template>
  <ion-app>
    <ion-loading :is-open="loading_user" message="Загрузка..."/>
    <ion-router-outlet></ion-router-outlet>
  </ion-app>
</template>

<script>
import {IonApp, IonLoading, IonRouterOutlet} from "@ionic/vue";
import {mapGetters} from "vuex";
import {defineComponent} from "vue";

export default defineComponent({
  name: 'App',
  components: {
    IonApp,
    IonRouterOutlet,
    IonLoading,
  },
  computed: {
    ...mapGetters(['loading_user'])
  },
  async beforeMount() {
    this.$store.dispatch('checkMobile');
    this.$store.commit('setLoadingUser', true);
    await this.$store.dispatch('getMe');
    await this.$store.dispatch('getOperations');
  },
})
</script>

<style lang="scss">

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

</style>
