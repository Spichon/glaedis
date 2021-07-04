import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

import en from './en.json';
import fr from './fr.json';

export const defaultLocale = 'en';

export const languages = {
  en: en,
  fr: fr,
};
