import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify, {
    iconfont: 'md',
});

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: '#586F7C',
                secondary: '#DD985C',
                accent: '#8c9eff',
                error: '#b71c1c',
            },
        },
    },
});
