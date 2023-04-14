<template>
  <div>
    <a :href="getYandexUrl()">
      <ion-button>Войти с Яндекс</ion-button>
    </a>
  </div>
</template>

<script>
import {getYandexUrl} from "@/utils/getYandexUrl.js"
import {IonButton} from "@ionic/vue";

const from_url = 'login/';

export default {
  name: 'YandexLogin',
  components: {
    IonButton,
  },
  methods: {
    getYandexUrl () {
      return getYandexUrl(from_url)
    }
  }
}
</script>

<style scoped>
</style>
