<template>
  <base-layout>
    <template #body>
      <div class="center">
        <form @submit.prevent ref="form">
          <h3>Вход в систему</h3>
          <ion-item ref="email">
            <ion-label position="floating">Почта</ion-label>
            <ion-input
              type="email"
              v-model="login_email"
              @ionInput="validateEmail"
              placeholder="Введите почту"
            ></ion-input>
            <ion-note slot="error">Некорректная почта</ion-note>
          </ion-item>
          <ion-item class="ion-margin-top">
            <ion-label position="floating">Пароль</ion-label>
            <ion-input
              v-model="login_password"
              placeholder="Введите пароль"
              type="password"
            ></ion-input>
          </ion-item>
          <ion-button
            class="ion-margin-top"
            color="primary"
            expand="block"
            @click="submitLogin()"
          >
            Войти
          </ion-button>
        </form>
        <div class="oauth">
          <GoogleLogin class="google"/>
          <YandexLogin class="yandex"/>
        </div>
      </div>
    </template>
  </base-layout>
</template>

<script>
import {mapGetters} from "vuex";
import {IonButton, IonInput, IonItem, IonLabel, IonNote} from "@ionic/vue";
import BaseLayout from "@/components/BaseLayout";
import {checkEmail} from "@/utils/functions";
import GoogleLogin from "@/components/login/GoogleLogin";
import YandexLogin from "@/components/login/YandexLogin";

export default {
  name: "Login",
  components: {
    BaseLayout,
    IonInput,
    IonLabel,
    IonItem,
    IonButton,
    IonNote,
    GoogleLogin,
    YandexLogin,
  },
  data() {
    return {
      login_email: '',
      login_password: '',
      show_modal_recovery: false,
      show_modal_login: false,
    }
  },
  computed: {
    ...mapGetters(['user']),
  },
  methods: {
    validateEmail(ev) {
      const value = ev.target.value;

      this.$refs.email.$el.classList.remove('ion-valid');
      this.$refs.email.$el.classList.remove('ion-invalid');

      if (value === '') return;

      checkEmail(value)
        ? this.$refs.email.$el.classList.add('ion-valid')
        : this.$refs.email.$el.classList.add('ion-invalid');
    },
    async submitLogin() {
      const formData = {
        email: this.login_email.replace(/\s/g, '').toLowerCase(),
        password: this.login_password.replace(/\s/g, '')
      }
      await this.$store.dispatch('LogIn', formData)
        .then(response => {
          if (response && response.status === 200) {
            this.$router.push({name: 'operations'})  //FIXME: переход на желаему страницу
          } else {
            this.$router.replace({name: 'login'})
          }
          this.onReset()
        })
        .catch(error => {
          if (error.response && error.response.data['non_field_errors']) {
            alert(error.response.data['non_field_errors'][0])
          } else {
            alert('Что-то пошло не так, проверьте правильность пароля')
          }
        })
    },
    onReset() {
      this.login_email = '';
      this.login_password = '';
    },
  }
}
</script>

<style lang="scss" scoped>

.center {
  max-width: 500px;
  margin: auto;
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}

.oauth {
  margin-top: 20px;
}

.yandex {
  margin-top: 10px;
}

.google {
  margin-top: 10px;
}

</style>