<template>
  <BaseLayout>
    <template #body>
      <div class="small-card mb5 mt20 hover" @click="$router.push({name: 'account'})">
        <ion-icon :icon="personOutline" size="large"/>
        <div class="ml10">
          {{ user.email }}
          <div class="name">
            {{ user.first_name }} {{ user.last_name }}
          </div>
        </div>
      </div>
      <a href="https://finaflow.ru/admin/">
        <div class="small-card mb5 mt20 hover" v-if="user.is_superuser">
          <ion-icon :icon="hammerOutline" size="large"/>
          <div class="ml10">Админ панель</div>
        </div>
      </a>
      <ComingSoon>
        <template #text>Скоро больше возможностей!</template>
      </ComingSoon>
    </template>
  </BaseLayout>
</template>

<script>
import BaseLayout from "@/components/BaseLayout.vue";
import ComingSoon from "@/components/common/ComingSoon.vue";
import {mapGetters} from "vuex";
import {personOutline, hammerOutline} from "ionicons/icons";
import {IonIcon} from "@ionic/vue";

export default {
  name: "More",
  components: {
    BaseLayout,
    ComingSoon,
    IonIcon,
  },
  data() {
    return {
      personOutline: personOutline,
      hammerOutline: hammerOutline,
    }
  },
  computed: {
    ...mapGetters(['user', 'isAuthenticated']),
  },
  async ionViewWillEnter() {
    await this.$store.dispatch('getMe')
  },
}
</script>

<style lang="scss" scoped>

.small-card {
  flex-direction: row;
  justify-content: start;
  align-items: center;
}

.name {
  font-weight: normal;
  font-size: 12px;
  align-self: end;
}

a {
  text-decoration: none;
  color: initial;
}

</style>