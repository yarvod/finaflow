<template>
  <ion-button
    :href="getYandexUrl()"
  >
    <ion-img :src="logo"></ion-img>
    <div class="yandex-text">
      Войти с Яндекс ID
    </div>
  </ion-button>
</template>

<script>
import {getYandexUrl} from "@/utils/getYandexUrl.js"
import {IonButton, IonImg} from "@ionic/vue";
import yandex_logo from "@/assets/img/yandex_logo.svg";

const from_url = 'login/';

export default {
  name: 'YandexLogin',
  data() {
    return {
      logo: yandex_logo,
    }
  },
  components: {
    IonButton,
    IonImg,
  },
  methods: {
    getYandexUrl() {
      return getYandexUrl(from_url)
    }
  }
}
</script>

<style lang="scss" scoped>

ion-button {
  --background: #1a1a1a;
  --background-hover: #464545FF;
}

.yandex-text {
  margin-left: 13px;
  font-weight: bold;
  color: white;
  max-width: 280px;
}

</style>
