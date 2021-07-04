<template>
  <div class="burger-menu">
    <button
      :class="['hamburger hamburger--collapse', { 'is-active': active }]"
      type="button"
      @click="handleBurgerMenu"
    >
      <span class="hamburger-box">
        <span class="hamburger-inner"></span>
      </span>
    </button>
    <div :class="['burger-menu__container', { 'is-active': active }]">
      <nav class="burger-menu__nav">
        <ul>
          <li v-for="(menu, index) in $t('menus')" v-bind:key="index">
            <a
              @click="handleBurgerMenu"
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
      <div class="burger__users">
        <v-btn to="/main/dashboard" large text>
          Account
          <v-icon class="ml-2">mdi-account-key</v-icon>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class BurgerMenu extends Vue {
  public active = false;
  public html = document.querySelector('html');

  public handleBurgerMenu() {
    if (this.active) {
      this.active = false;
      this.html.style.overflow = 'auto';
    } else {
      this.active = true;
      this.html.style.overflow = 'hidden';
    }
  }
}
</script>

<style lang="scss" scoped>
$menu-title-font-size: (
  null: 1.25rem /* 20px */,
  $medium-max: 2.125rem /* 34px */,
  $small-max: 1.5rem /* 24px */,
);

.burger-menu {
  margin-left: auto;

  .hamburger {
    @include breakpoint($small-max) {
      margin-top: 0;
    }
  }

  &__container {
    position: fixed;
    top: -140px;
    left: 0;
    width: 100%;
    height: calc(100% + 140px);
    transform: translate3d(0, -100%, 0);
    background-color: $blue-color;
    z-index: -1;
    transition: all 0.2s ease-in;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: $white-color;

    @include breakpoint($small-max) {
      top: -70px;
    }

    &.is-active {
      transform: translate3d(0, 0, 0);
    }
  }

  &__nav ul {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0;

    li:not(:last-child) {
      margin-bottom: 30px;
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
}
</style>
