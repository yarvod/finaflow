<template>
  <Modal
      @close="$emit('modal_state', false)"
  >
    <template #header>
      <h3>Востановление доступа</h3>
    </template>
    <template #body>
      <div v-if="timerCount > 0">
        <p>Мы отправили Вам письмо с почты <a>...</a> чтобы восстановить аккаунт</p>
        <p>Проверьте вашу почту <a>{{ formRecovery.email }}</a>.</p>
        <b>Чтобы отправить снова подождите {{ timerCount }} с.</b>
      </div>
      <form ref="formRecovery" @submit.prevent="submit">
        <div>
          <ion-item ref="email">
            <ion-label position="floating">Почта</ion-label>
            <ion-input
                type="email"
                v-model="formRecovery.email"
                @ionInput="validateEmail"
                placeholder="Введите почту"
            ></ion-input>
            <ion-note slot="error">Некорректная почта</ion-note>
          </ion-item>
        </div>
        <div class="buttonWrapper">
          <ion-button
              :disabled="(timerCount > 0)"
              type="submit"
          >
            Восстановить
          </ion-button>
        </div>
      </form>
    </template>
  </Modal>
</template>

<script>
import Modal from "@/components/common/Modal";
import user_service from "@/api/user_service";
import {checkEmail} from "@/utils/functions";
import {IonButton, IonInput, IonItem, IonLabel, IonNote} from "@ionic/vue";

export default {
  name: "RecoveryModal",
  components: {
    Modal,
    IonItem,
    IonNote,
    IonLabel,
    IonInput,
    IonButton,
  },
  props: {
    show_modal: {
      type: Boolean,
      default: false,
    }
  },
  data() {
    return {
      timerCount: 0,
      formRecovery: {
        email: ''
      },
      email_exists: false,
    }
  },
  watch: {
    timerCount: {
      handler(value) {
        if (value > 0) {
          setTimeout(() => {
            this.timerCount--;
          }, 1000);
        }

      },
      immediate: true
    }
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
    existsEmail() {
      if (checkEmail(this.formRecovery.email)) {
        user_service.checkEmail({email: this.formRecovery.email})
            .then(resp => {
              this.email_exists = resp.data.exists
            })
        return this.email_exists
      }
      return true
    },
    async submit() {
      if (this.existsEmail()) {
        const resp = await user_service.passwordResetConfirm({email: this.formRecovery.email})
        if (resp && resp.status === 200) {
          this.timerCount = 30
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>

.buttonWrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  * {
    margin-top: 10px;
  }
}

</style>