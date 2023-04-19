<template>
  <div>
    <ion-button
      v-if="deferredPrompt"
      ref="addBtn"
      class="add-button"
      @click="clickCallback"
    >
      Add
    </ion-button>
  </div>
</template>

<script>
import {IonButton} from "@ionic/vue";
import {defineComponent} from "vue";

export default defineComponent({
  name: 'PWAPrompt.vue',
  components: {
    IonButton,
  },
  data: () => ({
    deferredPrompt: null,
  }),
  IonViewDidEnter() {
    this.captureEvent()
  },
  methods: {
    captureEvent() {
      window.addEventListener('beforeinstallprompt', (e) => {
        // ! Prevent Chrome 67 and earlier from automatically showing the prompt
        e.preventDefault()
        // Stash the event so it can be triggered later.
        this.deferredPrompt = e
      })
    },
    clickCallback() {
      this.captureEvent()
      // Show the prompt
      this.deferredPrompt.prompt()
      // Wait for the user to respond to the prompt
      this.deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          // Call another function?
        }
        this.deferredPrompt = null
      })
    },
  },
})
</script>