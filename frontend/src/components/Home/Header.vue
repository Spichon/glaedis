<template>
  <div class="header">
    <div class="header__logo">
      <router-link tag="a" to="/" title="Glaedis - Accueil">
        <img src="@/assets/img/header-logo.png" alt="Glaedis" />
      </router-link>
    </div>
    <nav class="header__nav">
      <ul>
        <li v-for="(menu, index) in $t('menus')" v-bind:key="index">
          <a
            :href="menu.link"
            v-scroll-to="{
              el: menu.link,
              duration: 500,
              lazy: false,
              easing: 'linear',
              offset: -130,
              force: true,
              cancelable: true,
            }"
            >{{ menu.title }}</a
          >
        </li>
      </ul>
    </nav>
    <div class="header__users">
      <v-btn to="/main/dashboard" large text>
        Account
        <v-icon class="ml-2">mdi-account-key</v-icon>
      </v-btn>
    </div>
    <BurgerMenu></BurgerMenu>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

import BurgerMenu from '@/components/Home/BurgerMenu.vue';

@Component({
  components: {
    BurgerMenu,
  },
})
export default class Header extends Vue {}
</script>

<style lang="scss" scoped>
$menu-title-font-size: (
  null: 1.25rem /* 20px */,
  $medium-max: 1.125rem /* 18px */,
  $small-max: 1rem /* 16px */,
);

.header {
  background-color: $blue-color;
  padding: $header-padding;
  display: flex;
  flex-direction: row;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 2;

  @include breakpoint($medium-max) {
    padding: $header-padding--tablet;
  }

  @include breakpoint($small-max) {
    padding: $header-padding--mobile;
    padding-bottom: 5px;
  }

  &__logo {
    width: 233px;
    height: 58px;
    margin-right: 45px;
  }

  &__nav,
  &__users {
    @include breakpoint($medium-max) {
      display: none;
    }
  }

  &__nav ul {
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 58px;
    padding: 0;

    li {
      height: 100%;
    }

    li:not(:last-child) {
      margin-right: 50px;
    }

    a {
      @include font-size($menu-title-font-size);

      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100%;
      color: $white-color;
      line-height: 1.2;
    }
  }

  &__users {
    margin-left: auto;
  }
}
</style>
