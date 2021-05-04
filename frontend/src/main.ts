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

import fullscreen from 'vue-fullscreen';
import {redirectUrl, cognitoUserPoolClientId, cognitoUserPoolId, awsRegion, userUrl, testUrl} from './env';

Vue.use(fullscreen);
Vue.use(VueScrollTo);
Vue.use(VueClipboard);

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
    render: (h) => h(App),
}).$mount('#app');
