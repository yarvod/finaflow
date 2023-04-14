<template>
  <ion-button
    :href="getYandexUrl()"
    expand="block"
  >
    <ion-icon
      slot="start"
      :src="logo"
    ></ion-icon>
    <div class="yandex-text">
      Войти с Яндекс ID
    </div>
  </ion-button>
</template>

<script>
import {getYandexUrl} from "@/utils/getYandexUrl.js"
import {IonButton, IonIcon} from "@ionic/vue";
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
    IonIcon,
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
  --background: #1e1e1e;
  --background-hover: #464545FF;
}

.yandex-text {
  margin-left: 13px;
  font-weight: bold;
  color: white;
  max-width: 280px;
}

</style>
