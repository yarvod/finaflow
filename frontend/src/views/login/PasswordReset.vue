<template>
  <v-container>
    <v-row>
      <v-col class="d-flex justify-center">
        <v-form ref="form" @submit.prevent="submit" v-model="valid">
          <v-card>
            <v-card-title style="word-break: break-word">
              Востановление пароля
            </v-card-title>
            <v-card-text>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                      v-model="form.password"
                      label="Пароль"
                      :append-icon="show_pwd ? 'mdi-eye' : 'mdi-eye-off'"
                      :type="show_pwd ? 'text' : 'password'"
                      @click:append="show_pwd = !show_pwd"
                      :rules="passwordRules"
                      required
                      filled
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                      v-model="form.confirmPassword"
                      label="Подтверждение пароля"
                      :append-icon="show_pwd2 ? 'mdi-eye' : 'mdi-eye-off'"
                      :type="show_pwd2 ? 'text' : 'password'"
                      @click:append="show_pwd2 = !show_pwd2"
                      :rules="password2Rules"
                      required
                      filled
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="d-flex justify-center">
                  <v-btn color="primary" type="submit">Продолжить</v-btn>
                </v-col>
              </v-row>
              <v-row v-if="error">
                <v-col>
                  <b>{{error}}</b>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import user_service from "@/api/user_service";

export default {
  name: "PasswordReset",
  props: ['uid', 'token'],
  data() {
    return {
      valid: false,
      error: '',
      form: {
        password: '',
        confirmPassword: '',
      },
      show_pwd: false,
      show_pwd2: false,
      passwordRules: [
        v => !!v || 'Пароль необходим!',
        v => v.length >= 8 || 'Минимум 8 символов!',
      ],
      password2Rules: [
        v => !!v || 'Повторите пароль!',
        v => v === this.form.password || 'Пароли должны совпадать!'
      ],
    }
  },
  methods: {
    async submit() {
      if (this.valid) {
        const resp = await user_service.passwordReset({
          uid: this.uid,
          token: this.token,
          password: this.form.password,
          password2: this.form.confirmPassword
        })
        .catch(err => {
          this.error = err.response.data
        })
        if (resp && resp.status === 200) {
          this.$router.replace({name: 'login', params: {tabIndex: '0'}})
        }
      }
    }
  }
}
</script>

<style scoped>

</style>