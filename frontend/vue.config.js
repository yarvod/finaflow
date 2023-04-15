const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    publicPath: '/',
    devServer: {
        allowedHosts: "all"
    },
    transpileDependencies: true,
    css: {
        loaderOptions: {
            sass: {
                additionalData: `
          @import "@/assets/style/scss/variables.scss";
          @import "@/assets/style/scss/mixins.scss";
          @import "@/assets/style/scss/transitions.scss";
        `
            }
        }
    },
    pages: {
        index: {
            entry: 'src/main.ts'
        }
    }
})