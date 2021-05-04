<template>
  <div id="app">
    <v-app>
      <v-app-bar app color="primary" dark>
        <v-btn to="/" text class="d-flex align-center display-1">
          <v-icon>mdi-hand</v-icon>
          API
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn to="/main" large text>
          Account
          <v-icon class="ml-2">mdi-account-key</v-icon>
        </v-btn>
      </v-app-bar>
      <router-view/>
      <NotificationsManager></NotificationsManager>
    </v-app>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import NotificationsManager from '@/components/NotificationsManager.vue';

@Component({
  components: {
    NotificationsManager,
  },
})
export default class App extends Vue {
}
</script>
