import Vue from 'vue'
import App from './App.vue'
import '@aws-amplify/ui-vue';
import Amplify from 'aws-amplify';
import {Auth} from 'aws-amplify';

import store from './store'
import router from './router'
import vuetify from './plugins/vuetify';

import VueClipboard from 'vue-clipboard2';

const VueScrollTo = require('vue-scrollto');
import fullscreen from 'vue-fullscreen'

Vue.use(fullscreen);
Vue.use(VueScrollTo);
Vue.use(VueClipboard);

const ROOT_DOMAIN = 'glaedis.com';


Amplify.configure({
    Auth: {
        region: 'eu-west-1',
        userPoolId: 'eu-west-1_IEI0AT7pa',
        userPoolWebClientId: 'v43j263bt8a17qacme6obvvro',
        mandatorySignIn: false,
        oauth: {
            scope: ['email', 'openid'],
            redirectSignIn: `https://glaedis-app.${ROOT_DOMAIN}/`,
            redirectSignOut: `https://glaedis-app.${ROOT_DOMAIN}/`,
            responseType: 'code'
        }
    },
    API: {
        endpoints: [
            {
                name: "UserAPI",
                endpoint: `https://glaedis-user.${ROOT_DOMAIN}`,
                custom_header: async () => {
                    return {Authorization: `Bearer ${(await Auth.currentSession()).getIdToken().getJwtToken()}`}
                }
            },
            {
                name: "TestAPIKey",
                endpoint: `https://test.${ROOT_DOMAIN}`,
            }
        ]
    }
});

const currentConfig = Auth.configure();
console.log(currentConfig);

Vue.prototype.$Amplify = Amplify;

Vue.config.productionTip = false;

new Vue({
    store,
    router,
    vuetify,
    render: h => h(App)
}).$mount('#app')
