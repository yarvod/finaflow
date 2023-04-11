<template>
  <base-layout>
    <template #body>
      <ion-card>
        <ion-card-header>
          <ion-card-title>Редактирование профиля</ion-card-title>
        </ion-card-header>
        <ion-card-content>
          <form ref="form" @submit.prevent="submit">
            <ion-item ref="first_name">
              <ion-label position="stacked">Имя</ion-label>
              <ion-input
                  v-model="form.first_name"
                  type="text"
              />
            </ion-item>
            <ion-item ref="last_name">
              <ion-label position="stacked">Фамилия</ion-label>
              <ion-input
                  v-model="form.last_name"
                  type="text"
              />
            </ion-item>
            <ion-item ref="email">
              <ion-label position="stacked">Почта</ion-label>
              <ion-input
                  v-model="form.email"
                  type="email"
                  disabled
              />
            </ion-item>
            <ion-item ref="input_phone">
              <ion-label position="stacked">Телефон</ion-label>
              <ion-input
                  v-model="form.phone_number"
                  type="tel"
                  :max-length="11"
              />
            </ion-item>

            <div>
              <ion-button
                  type="submit"
              >
                Сохранить
              </ion-button>
            </div>
          </form>
        </ion-card-content>
      </ion-card>
    </template>
  </base-layout>
</template>

<script>
import {mapGetters} from 'vuex';
import BaseLayout from "@/components/BaseLayout.vue";
import {IonButton, IonCard, IonCardContent, IonCardHeader, IonCardTitle, IonInput, IonItem, IonLabel} from "@ionic/vue";

export default {
  name: "AccountEdit",
  components: {
    BaseLayout,
    IonCard,
    IonCardHeader,
    IonCardTitle,
    IonCardContent,
    IonButton,
    IonInput,
    IonItem,
    IonLabel,
  },
  data() {
    return {
      form: {
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
      }
    }
  },
  computed: {
    ...mapGetters(['user']),
  },
  async mounted() {
    await this.$store.dispatch('getMe')
    this.form = {...this.user};
  },
  methods: {
    async submit() {
      this.$store.commit('setLoadingUser', true)
      await this.$store.dispatch('updateMe', this.form)
        .then(() => {
          this.$router.back();
        })
    }
  }
}
</script>

<style lang="scss" scoped>


</style>