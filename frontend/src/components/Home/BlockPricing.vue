<template>
  <div id="pricing" class="content">
    <h1 class="content__title">{{ $t('blockPricing.title') }}</h1>
    <p class="content__chapo">{{ $t('blockPricing.chapo') }}</p>
    <div class="content__cards">
      <div
        class="card"
        v-for="(card, index) in $t('blockPricing.cards')"
        v-bind:key="index"
      >
        <div class="card__infos">
          <p class="card__price">{{ card.price }}</p>
          <p class="card__chapo">{{ card.chapo }}</p>
          <a class="card__cta btn" :href="card.link" :title="card.cta">{{
            card.cta
          }}</a>
        </div>
        <ul class="card__list">
          <li v-for="(arg, index) in card.args">
            <img v-if="arg.active" src="@/assets/img/true.png" alt="" />
            <img v-else src="@/assets/img/false.png" alt="" />
            <p>{{ arg.text }}</p>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class BlockPricing extends Vue {}
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

$card-price-font-size: (
  null: 5.25rem /* 84px */,
  $medium-max: 3.375rem /* 54px */,
  $small-max: 3rem /* 48px */,
);

$card-chapo-font-size: (
  null: 1.25rem /* 20px */,
  $medium-max: 1.125rem /* 18px */,
  $small-max: 1rem /* 16px */,
);

$card-args-font-size: (
  null: 1.25rem /* 20px */,
  $medium-max: 1.125rem /* 18px */,
  $small-max: 1rem /* 16px */,
);

.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: $white-color;
  background-color: $blue-color;
  padding: $global-padding;
  padding-top: 115px;
  padding-bottom: 175px;

  @include breakpoint($medium-max) {
    padding: $global-padding--tablet;
    padding-bottom: 55px;
    padding-top: 55px;
  }

  @include breakpoint($small-max) {
    padding: $global-padding--mobile;
    padding-bottom: 45px;
    padding-top: 45px;
  }

  &__title {
    @include font-size($title-font-size);

    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 0.547em; // 35px
    text-align: center;
  }

  &__chapo {
    @include font-size($chapo-font-size);

    font-weight: 400;
    line-height: 1.6;
    max-width: 765px;
    text-align: center;
  }

  &__cards {
    margin-top: 7.5rem; // 120px
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 100%;

    @include breakpoint($medium-max) {
      margin-top: 2.5rem; // 40px
    }

    @include breakpoint($small-max) {
      flex-direction: column;
      align-items: center;
    }

    .card {
      display: block;
      width: 390px;
      height: 580px;
      max-height: 580px;
      background-color: $white-color;
      color: $black-color;
      padding: 45px 55px 45px 55px;
      border-radius: 20px;
      box-shadow: -5px 8px 55px -15px rgba(0, 0, 0, 0.85);
      -webkit-box-shadow: -5px 8px 55px -15px rgba(0, 0, 0, 0.85);
      -moz-box-shadow: -5px 8px 55px -15px rgba(0, 0, 0, 0.85);

      @include breakpoint($small-max) {
        width: 100%;
        height: 520px;
        max-height: 520px;
      }

      &:not(:last-child) {
        margin-right: 2.5rem; // 40px

        @include breakpoint($small-max) {
          margin-right: 0; // 40px
          margin-bottom: 2.5rem; // 40px
          padding: 30px 40px 30px 40px;
        }
      }

      &__infos {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        height: 240px;
        max-height: 240px;
        margin-bottom: 2.8125rem; // 45px

        @include breakpoint($small-max) {
          height: 180px;
          max-height: 180px;
        }
      }

      &__price {
        @include font-size($card-price-font-size);

        text-align: center;
        line-height: 1.2;
        font-weight: 400;
      }

      &__chapo {
        @include font-size($card-chapo-font-size);

        line-height: 1.2;
        text-align: center;
      }

      &__cta {
        margin: 0 auto;
      }

      &__list {
        li {
          display: flex;
          flex-direction: row;
          align-items: center;

          &:not(:last-child) {
            margin-bottom: 0.9375rem; // 15px
          }

          img {
            width: 14px;
            height: 14px;
            margin-right: 0.9375rem; // 15px
          }

          p {
            @include font-size($card-args-font-size);

            line-height: 1.2;
            color: $blue-light-color;
            max-width: 400px;
          }
        }
      }
    }
  }
}
</style>
