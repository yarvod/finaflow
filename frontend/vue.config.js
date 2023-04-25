const {defineConfig} = require('@vue/cli-service')
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
          @import "@/assets/style/scss/defaults.scss";
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
  },
  pwa: {
    name: 'FinaFlow',
    themeColor: '#f7f7f7',
    msTileColor: '#ffffff',
    iconPaths: {
      faviconSVG: 'img/icons/safari-pinned-tab.svg',
      favicon32: 'img/icons/favicon-32x32.png',
      favicon16: 'img/icons/favicon-16x16.png',
      appleTouchIcon: 'img/icons/apple-touch-icon-152x152.png',
      maskIcon: 'img/icons/safari-pinned-tab.svg',
      msTileImage: 'img/icons/msapplication-icon-144x144.png'
    }
  }
})