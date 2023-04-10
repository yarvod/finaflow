<template>
  <div :class="$style.header">
    <div :class="$style.leftSide">
      <router-link :to="{name: 'operations'}">
        <img
            :src="path"
            alt=""
        />
      </router-link>
      <p v-if="!isMobile">
        Система научно-технического прогнозирования
      </p>
      <p v-else>НТР</p>
    </div>

    <div :class="$style.rightSide">
      <YButton
          :class="$style.button"
          @click="$router.push({name: 'account'})"
          color="#1E7FC5"
          text_color="white"
      >
        <Icon color="white" icon="mdi-account"/>
      </YButton>

      <YButton
          :class="$style.button"
          @click="$router.back()"
          color="#1E7FC5"
          text_color="white"
      >
        <Icon color="white" icon="mdi-login-variant"/>
      </YButton>
    </div>

  </div>
</template>

<script>

import {mapGetters} from "vuex";
import path_logo from "@/assets/img/mipt_rus_text_inv.png"
import YButton from "@/components/ui/YButton";
import { Icon } from '@iconify/vue';

export default {
  name: "YHeader",
  components: {
    YButton,
    Icon,
  },
  data() {
    return {
      username: '',
      password: '',
      errors: [],
      path: path_logo,
    }
  },
  computed: {
    ...mapGetters(['user', 'loading_user', 'isAuthenticated', 'isMobile'])
  },
  methods: {
    async LogOut() {
      await this.$store.dispatch('LogOut')
          .then(() => this.$store.dispatch('ResetStore'))
      await this.$router.push({name: 'login'})
    }
  }
}
</script>

<style lang="scss" module>
.v-btn {
  margin-right: 5px;
}

img {
  max-width: 100px;
}

.header {
  position: sticky;
  top: 0;
  left: 0;
  z-index: 12;
  transition: all .3s ease;
  padding-right: $containerPadding;
  padding-left: $containerPadding;
  height: $headerHeight;
  background-color: $Base1;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.title {
  color: $white;
  float: left;
  padding-left: 25px;
  display: flex;
  flex-direction: row;
}

.leftSide {
  display: flex;
  align-items: center;
  justify-items: start;
  position: relative;

  p {
    color: $white;
  }
}

.rightSide {
  display: flex;
}

.button:first-child {
  margin-right: 10px;
}

</style>
