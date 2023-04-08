<template>
  <div class="modal-container">
    <div class="modalHeader">
      <div>
        <slot name="header">
          default header
        </slot>
      </div>
      <ion-button
          @click="$emit('close')"
          fill="clear"
          color="medium"
      >
        <ion-icon
            :icon="closeCircleOutline"
            slot="icon-only"
        ></ion-icon>
      </ion-button>
    </div>

    <div class="modalBody">
      <slot name="body">
        default body
      </slot>
    </div>
  </div>
</template>

<script>
import YButton from "@/components/ui/YButton";
import {closeCircleOutline} from 'ionicons/icons'
import {IonButton, IonIcon} from "@ionic/vue";

export default {
  name: 'Modal',
  components: {
    YButton,
    IonButton,
    IonIcon,
  },
  data() {
    return {
      closeCircleOutline: closeCircleOutline
    }
  }
}
</script>

<style lang="scss" scoped>

.modal-container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 9998;
  width: 100%;
  max-width: 700px;
  height: fit-content;
  max-height: 500px;
  margin: 0 auto;
  padding: 20px 30px;
  background-color: white;
  color: $black;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modalHeader {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.modalBody {
  margin: 20px 0;
}

</style>