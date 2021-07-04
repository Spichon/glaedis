<template>
  <div id="product" class="content">
    <div
      class="content__row"
      v-for="(row, index) in $t('blockProduct.rows')"
      v-bind:key="index"
    >
      <div class="column column--img">{{ row.img }}</div>
      <div class="column column--content">
        <h2 class="column__title">{{ row.title }}</h2>
        <ul v-if="row.isList" class="column__list">
          <li v-for="(arg, index) in row.args">
            <img src="@/assets/img/check.png" alt="" />
            <p>{{ arg.text }}</p>
          </li>
        </ul>
        <div v-else>
          <p class="column__chapo">{{ row.chapo }}</p>
          <a class="column__cta btn" :href="row.link" :title="row.cta">{{
            row.cta
          }}</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class BlockProduct extends Vue {}
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

$args-font-size: (
  null: 1rem /* 16px */,
  $medium-max: 0.875rem /* 14px */,
  $small-max: 0.75rem /* 12px */,
);

.content {
  color: $black-color;
  padding: $global-custom-padding;
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

  &__row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;

    @include breakpoint($small-max) {
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

    &:first-child {
      margin-bottom: 10.9375rem; // 175px

      @include breakpoint($medium-max) {
        margin-bottom: 2.5rem; // 40px
      }

      .column--content {
        @include breakpoint($medium-max) {
          margin-left: 1.875rem; // 30px
        }

        @include breakpoint($small-max) {
          margin-left: 0;
        }
      }
    }

    &:nth-child(even) {
      flex-direction: row-reverse;

      @include breakpoint($small-max) {
        flex-direction: column;
        justify-content: center;
        align-items: center;
      }

      .column--content {
        @include breakpoint($medium-max) {
          margin-right: 1.875rem; // 30px
        }

        @include breakpoint($small-max) {
          margin-right: 0;
        }
      }
    }

    .column {
      width: 100%;

      &--img {
        width: calc(100% / 2);
        height: 583px;
        border-radius: 30px;
        background-color: $white-color;
        box-shadow: -5px 8px 55px -15px rgba(0, 0, 0, 0.85);
        -webkit-box-shadow: -5px 8px 55px -15px rgba(0, 0, 0, 0.85);
        -moz-box-shadow: -5px 8px 55px -15px rgba(0, 0, 0, 0.85);

        @include breakpoint($medium-max) {
          height: 530px;
        }

        @include breakpoint($small-max) {
          width: 100%;
          height: 350px;
          margin-bottom: 2.5rem; // 40px
        }
      }

      &--content {
        max-width: 590px;
        margin: auto;

        @include breakpoint($medium-max) {
          width: calc(100% / 2);
          max-width: 50%;
        }

        @include breakpoint($small-max) {
          width: 100%;
          max-width: 100%;
        }
      }

      &__title {
        @include font-size($title-font-size);

        line-height: 1.2;
        font-weight: 400;
        margin-bottom: 0.703em; // 45px

        @include breakpoint($medium-max) {
          margin-bottom: 1.875rem; // 30px
        }

        @include breakpoint($small-max) {
          text-align: center;
        }
      }

      &__chapo {
        @include font-size($chapo-font-size);

        line-height: 1.6;
        color: $blue-light-color;
        margin-bottom: 2.5em; // 50px

        @include breakpoint($medium-max) {
          margin-bottom: 1.875rem; // 30px
        }

        @include breakpoint($small-max) {
          text-align: center;
        }
      }

      &__cta {
        @include breakpoint($small-max) {
          margin: 0 auto;
        }
      }

      &__list {
        li {
          display: flex;

          &:not(:last-child) {
            margin-bottom: 1.875rem; // 30px
          }

          img {
            margin-right: 1.5625rem; // 25px

            @include breakpoint($medium-max) {
              width: 45px;
              height: 45px;
            }

            @include breakpoint($small-max) {
              margin-right: 1.25rem; // 20px
              width: 40px;
              height: 40px;
            }
          }

          p {
            @include font-size($args-font-size);

            line-height: 1.4;
            color: $blue-light-color;
            max-width: 400px;
          }
        }
      }
    }
  }
}
</style>
