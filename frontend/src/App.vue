<template>
  <div id="app">
    <v-app>
      <router-view />
      <NotificationsManager></NotificationsManager>
    </v-app>
  </div>
</template>

<script lang="ts">
// import '@/assets/styles/minify/css/main.css';
import { Component, Vue } from 'vue-property-decorator';
import NotificationsManager from '@/components/NotificationsManager.vue';

@Component({
  components: {
    NotificationsManager,
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
/* Import Local Fonts */
@font-face {
  font-family: 'Helvetica';
  src: url('./assets/fonts/Helvetica.woff') format('woff'),
    url('./assets/fonts/Helvetica.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: block;
}

@font-face {
  font-family: 'Helvetica';
  src: url('./assets/fonts/Helvetica-Light.woff') format('woff'),
    url('./assets/fonts/Helvetica-Light.woff2') format('woff2');
  font-weight: 300;
  font-style: normal;
  font-display: block;
}

@font-face {
  font-family: 'Helvetica';
  src: url('./assets/fonts/Helvetica-Oblique.woff') format('woff'),
    url('./assets/fonts/Helvetica-Oblique.woff2') format('woff2');
  font-weight: 400;
  font-style: italic;
  font-display: block;
}

@font-face {
  font-family: 'Helvetica';
  src: url('./assets/fonts/Helvetica-Bold.woff') format('woff'),
    url('./assets/fonts/Helvetica-Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: block;
}

@font-face {
  font-family: 'Helvetica';
  src: url('./assets/fonts/Helvetica-BoldOblique.woff') format('woff'),
    url('./assets/fonts/Helvetica-BoldOblique.woff2') format('woff2');
  font-weight: 700;
  font-style: italic;
  font-display: block;
}

#app {
  font-family: 'Helvetica', sans-serif;
}
</style>
