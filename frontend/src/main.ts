import {createApp} from 'vue'
import App from './App.vue'
import router from './router';
// @ts-ignore
import store from './store';

import '@ionic/vue/css/core.css';
import '@ionic/vue/css/normalize.css';
import '@ionic/vue/css/structure.css';
import '@ionic/vue/css/typography.css';
import '@ionic/vue/css/padding.css';
import '@ionic/vue/css/float-elements.css';
import '@ionic/vue/css/text-alignment.css';
import '@ionic/vue/css/text-transformation.css';
import '@ionic/vue/css/flex-utils.css';
import '@ionic/vue/css/display.css';

/* Theme variables */
import './theme/variables.css';
import './theme/default.css';

import BaseLayout from "@/components/BaseLayout.vue";
import {Icon} from '@iconify/vue';
import {IonicVue} from '@ionic/vue';

const app = createApp(App)
    .use(IonicVue)
    .use(router)
    .use(store)

app.component('BaseLayout', BaseLayout);
app.component('Icon', Icon);

router.isReady().then(() => {
    app.mount('#app');
});