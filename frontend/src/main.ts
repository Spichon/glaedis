import '@babel/polyfill';
import './component-hooks';
import vuetify from './plugins/vuetify';
import './plugins/vee-validate';
import './plugins/vue-filter';
import './registerServiceWorker';
import 'vuetify/dist/vuetify.min.css';
import Vue from 'vue';
import App from './App.vue';
import '@aws-amplify/ui-vue';
import Amplify from 'aws-amplify';
import {Auth} from 'aws-amplify';
import store from './store';
import router from './router';
import VueClipboard from 'vue-clipboard2';
import VueScrollTo from 'vue-scrollto';
import Hamburgers from 'hamburgers';
import Carousel3d from 'vue-carousel-3d';

import fullscreen from 'vue-fullscreen';
import { redirectUrl, cognitoUserPoolClientId, cognitoUserPoolId, awsRegion, userUrl, testUrl } from './env';

// Multi languages
import VueI18n from 'vue-i18n'
import { languages } from './i18n/index.js'
import { defaultLocale } from './i18n/index.js'

const messages = Object.assign(languages);

Vue.config.productionTip = false;


const i18n = new VueI18n({
  locale: defaultLocale,
  fallbackLocale: 'fr',
  messages
})

Vue.use(fullscreen);
Vue.use(VueScrollTo);
Vue.use(Hamburgers);
Vue.use(Carousel3d);
Vue.use(VueClipboard);
Vue.use(VueI18n);

Amplify.configure({
    Auth: {
        region: awsRegion,
        userPoolId: cognitoUserPoolId,
        userPoolWebClientId: cognitoUserPoolClientId,
        mandatorySignIn: false,
        oauth: {
            scope: ['email', 'openid'],
            redirectSignIn: redirectUrl,
            redirectSignOut: redirectUrl,
            responseType: 'code',
        },
    },
    API: {
        endpoints: [
            {
                name: 'UserAPI',
                endpoint: userUrl,
                custom_header: async () => {
                    return {Authorization: `Bearer ${(await Auth.currentSession()).getIdToken().getJwtToken()}`};
                },
            },
            {
                name: 'TestAPIKey',
                endpoint: testUrl,
            },
        ],
    },
});


Vue.prototype.$Amplify = Amplify;

Vue.config.productionTip = false;

new Vue({
    store,
    router,
    // @ts-ignore
    vuetify,
    i18n,
    render: (h) => h(App),
}).$mount('#app');
