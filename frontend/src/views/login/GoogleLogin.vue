<template>
  <div>
    <SLoader/>
  </div>
</template>

<script>
import SLoader from '@/components/ui/SLoader.vue';
import {mapGetters} from "vuex";

export default {
  name: "GoogleLogin",
  components: {
    SLoader,
  },
  computed: {
    ...mapGetters(['user'])
  },
  async mounted() {
    await this.$store.dispatch('LogInGoogle', {code: this.$route.query.code})
      .then((status) => {
          if (status === 200) {
            this.$router.replace({name: 'operations'})
          } else {
            this.$router.replace({name: 'login'})
          }
        }
      )
  }
}
</script>

<style scoped>

</style>