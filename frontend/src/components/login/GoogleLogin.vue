<template>
  <div>
    <a :href="getGoogleUrl()">
      <ion-button>Login with Google</ion-button>
    </a>
  </div>
</template>

<script>
import {getGoogleUrl} from "@/utils/getGoogleUrl";
import {IonButton} from "@ionic/vue";

const from_url = 'login/';

export default {
  name: 'GoogleLogin',
  components: {
    IonButton,
  },
  methods: {
    getGoogleUrl () {
      return getGoogleUrl(from_url)
    }
  }
}
</script>

<style scoped>
</style>