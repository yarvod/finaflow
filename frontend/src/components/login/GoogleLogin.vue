<template>
  <div>
    <ion-button
      :href="getGoogleUrl()"
      expand="block"
    >
      <ion-icon
        slot="start"
        :src="logo"
        size="large"
      ></ion-icon>
      <div class="google-text">
        Continue with Google
      </div>
    </ion-button>
  </div>
</template>

<script>
import {getGoogleUrl} from "@/utils/getGoogleUrl";
import {IonButton, IonIcon, IonImg} from "@ionic/vue";
import google_logo from "@/assets/img/google_logo.svg";

const from_url = 'login/';

export default {
  name: 'GoogleLogin',
  components: {
    IonButton,
    IonImg,
    IonIcon,
  },
  data() {
    return {
      logo: google_logo,
    }
  },
  methods: {
    getGoogleUrl() {
      return getGoogleUrl(from_url)
    }
  }
}
</script>

<style lang="scss" scoped>
ion-button {
  --border-color: 1px #e3e7ef solid;
  --background-hover: #cbd0de;
  --background: #f6f8fc;
  --background-activated: #cbd0de;
}

.google-text {
  font-weight: bold;
  color: black;
  max-width: 280px;
}
</style>