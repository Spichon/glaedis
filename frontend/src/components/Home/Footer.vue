<template>
  <div class="content">
    <div class="content__column">
      <h2>{{ $t('footer.about.title') }}</h2>
      <p v-html="$t('footer.about.text')"></p>
    </div>
    <div class="content__column">
      <h2>{{ $t('footer.menus.title') }}</h2>
      <ul>
        <li
          v-for="(link, index) in $t('footer.menus.links')"
          v-bind:key="index"
        >
          <a :href="link.link">{{ link.title }}</a>
        </li>
      </ul>
    </div>
    <div class="content__column">
      <h2>{{ $t('footer.newsletter.title') }}</h2>
      <form action="">
        <label for="email" class="visuallyhidden">{{
          $t('footer.newsletter.label')
        }}</label>
        <input
          class="email"
          type="email"
          name="email"
          id="email"
          :placeholder="$t('footer.newsletter.label')"
        />
        <input
          class="submit btn"
          type="submit"
          :value="$t('footer.newsletter.submit')"
        />
      </form>
      <ul class="socials">
        <li v-for="(social, index) in $t('footer.socials')" v-bind:key="index">
          <a :href="social.link"
            ><img
              v-if="social.picto === 'facebook'"
              src="@/assets/svg/facebook.svg"
              alt=""/>
            <img
              v-if="social.picto === 'twitter'"
              src="@/assets/svg/twitter.svg"
              alt=""/><img
              v-if="social.picto === 'linkedin'"
              src="@/assets/svg/linkedin.svg"
              alt=""
          /></a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class BlockStarted extends Vue {}
</script>

<style lang="scss" scoped>
$column-h2-font-size: (
  null: 1.875rem /* 30px */,
  $medium-max: 1.625rem /* 26px */,
  $small-max: 1.25rem /* 20px */,
);

$column-text-font-size: (
  null: 1.25rem /* 20px */,
  $medium-max: 1.125rem /* 18px */,
  $small-max: 1rem /* 16px */,
);

.content {
  display: flex;
  padding: $global-padding;
  padding-top: 125px;
  padding-bottom: 100px;
  color: $black-color;

  @include breakpoint($medium-max) {
    padding: $global-padding--tablet;
    padding-bottom: 55px;
    padding-top: 55px;
  }

  @include breakpoint($small-max) {
    padding: $global-padding--mobile;
    padding-bottom: 25px;
    padding-top: 25px;
    flex-wrap: wrap;
  }

  &__column:not(:last-child) {
    width: 310px;

    @include breakpoint($medium-max) {
      width: calc(100% / 3);
    }

    @include breakpoint($small-max) {
      width: 100%;
      margin-bottom: 2.1875rem; // 35px
    }
  }

  &__column:first-child {
    margin-right: 8.4375rem; // 135px

    @include breakpoint($medium-max) {
      margin-right: 60px; // 135px
    }

    @include breakpoint($small-max) {
      margin-right: 0;
    }
  }

  &__column:last-child {
    margin-left: auto;

    @include breakpoint($small-max) {
      margin-left: 0;
      width: 100%;
    }
  }

  &__column {
    h2 {
      @include font-size($column-h2-font-size);

      font-weight: 400;
      line-height: 1.2;
      margin-bottom: 1.5em; // 45px
    }

    p {
      @include font-size($column-text-font-size);

      line-height: 1.6;
      color: $blue-light-color;
    }

    ul {
      @include font-size($column-text-font-size);

      line-height: 1.2;
      color: $blue-light-color;

      @include breakpoint($small-max) {
        display: flex;
        flex-wrap: wrap;
      }

      li:not(:last-child) {
        margin-bottom: 1em; // 20px

        &::after {
          @include breakpoint($small-max) {
            content: '-';
            margin: 0 7px;
          }
        }
      }
    }

    form {
      display: flex;
      justify-content: space-between;
      margin-bottom: 3.125rem; // 50px
      border: solid 1px $blue-color;
      border-radius: 10px;
      width: 562px;
      height: 68px;
      position: relative;

      @include breakpoint($medium-max) {
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 200px;
        height: 116px;
      }

      @include breakpoint($small-max) {
        width: 100%;
      }

      .email {
        padding-left: 30px;

        @include breakpoint($medium-max) {
          padding-left: 15px;
          width: 200px;
          height: 58px;
        }

        @include breakpoint($small-max) {
          width: 100%;
        }

        &::placeholder {
          @include font-size($column-text-font-size);

          color: $blue-color;
          opacity: 1;
        }
      }

      .submit {
        position: absolute;
        top: -1px;
        right: -2px;
        padding: 0 35px 0 15px;
        background: $orange-color url('../../assets/svg/send.svg') no-repeat
          center right 20px;

        @include breakpoint($medium-max) {
          position: initial;
          margin-top: auto;
          margin-bottom: -1px;
        }

        @include breakpoint($small-max) {
          width: 100%;
        }
      }
    }

    .socials {
      display: flex;

      @include breakpoint($small-max) {
        justify-content: center;
      }

      li:not(:last-child) {
        margin-right: 1.25rem; // 20px

        &::after {
          @include breakpoint($small-max) {
            content: none;
          }
        }
      }
    }
  }
}
</style>
