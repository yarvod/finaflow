<template>
  <Modal
      @close="$emit('modal_state', false)"
  >
    <template #header>
      <h3>Выберете роль</h3>
    </template>
    <template #body>
      <div class="buttonWrapper">
        <ion-button
            @click="login"
        >
          Войти как редактор ТОС
        </ion-button>
        <ion-button
            @click="login"
        >
          Войти как ЛПР
        </ion-button>
      </div>
    </template>
  </Modal>
</template>

<script>
import YButton from "@/components/ui/YButton";
import Modal from "@/components/common/Modal";
import {IonButton} from "@ionic/vue";

export default {
  name: "LoginModal",
  components: {
    Modal,
    IonButton,
  },
  methods: {
    login() {
      this.$emit('modal_state', false)
      this.$parent.submitLogin();
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