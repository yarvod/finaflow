<template>
  <ion-app>
    <ion-loading :is-open="loading_user" message="Загрузка..."/>
<!--    <router-view v-slot="{ Component }">-->
<!--    <transition name="fade" mode="out-in" appear>-->
<!--      <component :is="Component" />-->
<!--    </transition>-->
<!--  </router-view>-->
    <router-view/>
  </ion-app>
</template>

<script>
import {IonApp, IonLoading, IonRouterOutlet} from "@ionic/vue";
import {mapGetters} from "vuex";

export default {
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
  },
}
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
