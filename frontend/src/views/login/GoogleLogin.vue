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
      .then(async status => {
          if (status === 200) {
            await this.$store.dispatch('getMe')
              .then(resp => {
                if (resp && resp.status === 200) {
                  localStorage.isAuthenticated = true;
                  this.$router.push({name: 'operations'})
                }
              })
          }
          this.$router.push({name: 'login'})
        }
      )
  }
}
</script>

<style scoped>

</style>