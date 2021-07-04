<template>
  <div id="highlighted" class="content">
    <h1 class="content__title">{{ $t('blockHighlighted.title') }}</h1>
    <p class="content__chapo">{{ $t('blockHighlighted.chapo') }}</p>
    <a
      class="content__cta btn"
      :href="$t('blockHighlighted.link')"
      :title="$t('blockHighlighted.cta')"
      >{{ $t('blockHighlighted.cta') }}</a
    >
    <div class="content__mockup">
      <img src="@/assets/img/mockup-macbook.png" />
    </div>
    <div class="content__brands">
      <a href="https://www.coinbase.com" title="Coinbase">
        <img src="@/assets/img/coinbase.png" alt="Coinbase" />
      </a>
      <a href="https://global.bittrex.com/" title="Bittrex">
        <img src="@/assets/img/bittrex.png" alt="Bittrex" />
      </a>
      <a href="https://www.binance.com" title="Binance">
        <img src="@/assets/img/binance.png" alt="Binance" />
      </a>
      <a href="https://www.kraken.com" title="Kraken">
        <img src="@/assets/img/kraken.png" alt="Kraken" />
      </a>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class BlockHighlighted extends Vue {}
</script>

<style lang="scss" scoped>
$title-font-size: (
  null: 4rem /* 64px */,
  $medium-max: 2.75rem /* 44px */,
  $small-max: 1.5rem /* 24px */,
);

$chapo-font-size: (
  null: 1.25rem /* 20px */,
  $medium-max: 1.125rem /* 18px */,
  $small-max: 1rem /* 16px */,
);

.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: $global-padding;
  padding-top: calc(95px + 140px); // Calc height of fixed header
  padding-bottom: 175px;
  color: $white-color;
  background: url('../../assets/svg/background-highlighted.svg') no-repeat top
    center / cover;

  @include breakpoint($medium-max) {
    padding: $global-padding--tablet;
    padding-bottom: 55px;
    padding-top: calc(55px + 140px); // Calc height of fixed header
  }

  @include breakpoint($small-max) {
    padding: $global-padding--mobile;
    padding-bottom: 45px;
    padding-top: calc(55px + 40px); // Calc height of fixed header
  }

  &__title {
    @include font-size($title-font-size);

    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 0.391em; // 25px
    text-align: center;
  }

  &__chapo {
    @include font-size($chapo-font-size);

    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 2.25em; // 45px
    text-align: center;
  }

  &__cta {
    margin-bottom: 4.6875rem; // 75px

    @include breakpoint($medium-max) {
      margin-bottom: 3.4375rem; // 55px
    }

    @include breakpoint($small-max) {
      margin-bottom: 2.25rem; // 45px
    }
  }

  &__mockup {
    margin-bottom: 10.3125rem; // 165px

    @include breakpoint($medium-max) {
      margin-bottom: 3.75rem; // 60px
    }

    @include breakpoint($small-max) {
      margin-bottom: 2.25rem; // 45px
    }
  }

  &__brands {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
    z-index: 1;

    a {
      @include breakpoint($medium-max) {
        transform: scale(0.9);
      }

      &:first-child {
        @include breakpoint($medium-max) {
          margin-top: -5px;
        }

        @include breakpoint($small-max) {
          margin-top: -3px;
        }
      }
    }
  }
}
</style>
