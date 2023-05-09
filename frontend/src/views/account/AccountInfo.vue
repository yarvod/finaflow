<template>
  <base-layout>
    <template #main-header>
      <div class="container">
        <ion-title>FinaFlow</ion-title>
        <ion-buttons slot="start">
          <ion-back-button></ion-back-button>
        </ion-buttons>
      </div>
    </template>
    <template #body>
      <ion-card>
        <ion-card-header class="head">
          <ion-card-title>Профиль</ion-card-title>
          <div>
            <ion-button
              router-link="/account_edit"
              router-direction="forward"
            >
              Изменить
            </ion-button>
          </div>
        </ion-card-header>

        <ion-card-content>
          <ion-list>
            <ion-item>
              <div class="col">
                <b>Имя: </b> <span>{{ user.first_name }}</span>
              </div>
              <ion-button
                v-if="!user.first_name"
                @click="$router.push({name: 'account_edit'})"
              >
                Добавить
              </ion-button>
            </ion-item>
            <ion-item>
              <div class="col">
                <b>Фамилия: </b> <span>{{ user.last_name }}</span>
              </div>
              <ion-button
                class="col"
                v-if="!user.last_name"
                @click="$router.push({name: 'account_edit'})"
              >
                Добавить
              </ion-button>
            </ion-item>
            <ion-item>
              <div class="col">
                <b>Почта: </b> <span>{{ user.email }}</span>
              </div>
            </ion-item>
            <ion-item>
              <div class="col">
                <b>Телефон: </b> <span>{{ user.phone_number }}</span>
              </div>
              <ion-button
                class="col"
                v-if="!user.phone_number"
                @click="$router.push({name: 'account_edit'})"
              >
                Добавить
              </ion-button>
            </ion-item>
          </ion-list>
        </ion-card-content>
        <ion-button
          class="ion-margin-horizontal"
          @click="LogOut"
          color="danger"
        >
          Выйти
        </ion-button>
      </ion-card>
    </template>
  </base-layout>
</template>


<script>
import {mapGetters} from "vuex";
import BaseLayout from "@/components/BaseLayout.vue";
import {
  IonBackButton,
  IonButton,
  IonButtons,
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardTitle,
  IonItem,
  IonList,
  IonTitle
} from "@ionic/vue";

export default {
  name: "AccountInfo",
  components: {
    IonButton,
    BaseLayout,
    IonList,
    IonCard,
    IonCardHeader,
    IonCardTitle,
    IonCardContent,
    IonItem,
    IonTitle,
    IonButtons,
    IonBackButton,
  },
  data() {
    return {}
  },
  computed: {
    ...mapGetters(['user', 'isMobile'])
  },
  methods: {
    async LogOut() {
      this.$store.commit('setLoadingUser', true);
      await this.$store.dispatch('LogOut')
        .then(() => {
          this.$store.dispatch('ResetStore')
          this.$router.push({name: 'login'})
        })
    }
  },
  async ionViewWillEnter() {
    await this.$store.dispatch('getMe')
  }
}
</script>

<style lang="scss" scoped>

.head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

span {
  word-break: break-word;
}

</style>