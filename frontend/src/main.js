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

const VUE_APP_COGNITO_USER_POOL_CLIENT_ID = process.env.VUE_APP_COGNITO_USER_POOL_CLIENT_ID;
const VUE_APP_COGNITO_USER_POOL_ID = process.env.VUE_APP_COGNITO_USER_POOL_ID;
const VUE_APP_REDIRECT_URL = process.env.VUE_APP_REDIRECT_URL;
const VUE_APP_AWS_REGIONS = process.env.VUE_APP_AWS_REGION;
const VUE_APP_USER_API = process.env.VUE_APP_USER_API;
const VUE_APP_TEST_API = process.env.VUE_APP_TEST_API;

Amplify.configure({
    Auth: {
        region: VUE_APP_AWS_REGIONS,
        userPoolId: VUE_APP_COGNITO_USER_POOL_ID,
        userPoolWebClientId: VUE_APP_COGNITO_USER_POOL_CLIENT_ID,
        mandatorySignIn: false,
        oauth: {
            scope: ['email', 'openid'],
            redirectSignIn: VUE_APP_REDIRECT_URL,
            redirectSignOut: VUE_APP_REDIRECT_URL,
            responseType: 'code'
        }
    },
    API: {
        endpoints: [
            {
                name: "UserAPI",
                endpoint: VUE_APP_USER_API,
                custom_header: async () => {
                    return {Authorization: `Bearer ${(await Auth.currentSession()).getIdToken().getJwtToken()}`}
                }
            },
            {
                name: "TestAPIKey",
                endpoint: VUE_APP_TEST_API,
            }
        ]
    }
});


Vue.prototype.$Amplify = Amplify;

Vue.config.productionTip = false;

new Vue({
    store,
    router,
    vuetify,
    render: h => h(App)
}).$mount('#app')
