// @ts-ignore
import moment from 'moment';
import Vue from 'vue';

Vue.filter('formatDate', (value: Date) => {
    if (value) {
        return moment(String(value)).calendar();
    }
});
