import Vue from 'vue';
import VeeValidate from 'vee-validate';
import {Validator} from 'vee-validate';

Vue.use(VeeValidate);

// Prevent from the error : Invalid base64-encoded string: number of data characters (9)
// cannot be 1 more than a multiple of 4
Validator.extend('modulo4', {
    getMessage: (field) => 'The ' + field + 'cannot be 1 more than a multiple of 4',
    validate: (value) => value.length % 4 !== 1,
});



