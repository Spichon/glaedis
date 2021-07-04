<template>
  <div id="faq" class="content">
    <h1 class="content__title">{{ $t('blockFaq.title') }}</h1>
    <p class="content__chapo">{{ $t('blockFaq.chapo') }}</p>
    <ul class="content__questions">
      <li
        class="question"
        v-for="(question, index) in $t('blockFaq.questions')"
        v-bind:key="index"
      >
        <img src="@/assets/img/answer.png" alt="" />
        <div>
          <h3>{{ question.title }}</h3>
          <p>{{ question.answer }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class BlockFaq extends Vue {}
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

$question-title-font-size: (
  null: 1.875rem /* 30px */,
  $medium-max: 1.625rem /* 26px */,
  $small-max: 1.25rem /* 20px */,
);

$question-answer-font-size: (
  null: 1rem /* 16px */,
  $medium-max: 0.875rem /* 14px */,
  $small-max: 0.75rem /* 12px */,
);

.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: $black-color;
  background-color: $white-color;
  padding: $global-faq-padding;
  padding-top: 115px;
  padding-bottom: 100px;

  @include breakpoint($medium-max) {
    padding: $global-padding--tablet;
    padding-bottom: 55px;
    padding-top: 55px;
  }

  @include breakpoint($small-max) {
    padding: $global-padding--mobile;
    padding-bottom: 25px;
    padding-top: 45px;
  }

  &__title {
    @include font-size($title-font-size);

    font-weight: 700;
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

  &__questions {
    margin-top: 9.375rem; // 150px
    display: flex;
    flex-wrap: wrap;

    @include breakpoint($medium-max) {
      margin-top: 2.5rem; // 40px
    }

    li {
      display: flex;
      width: calc(100% / 2 - 28px);
      margin-bottom: 5.625rem; // 90px

      @include breakpoint($medium-max) {
        margin-bottom: 1.875rem; // 30px
        width: calc(100% / 2 - 10px);
      }

      @include breakpoint($small-max) {
        width: 100%;
      }

      &:nth-child(even) {
        margin-left: auto;
      }

      img {
        width: 70px;
        height: 70px;
        margin-right: 1.875rem; // 30px

        @include breakpoint($medium-max) {
          width: 55px;
          height: 55px;
          margin-right: 1.25rem; // 20px
        }

        @include breakpoint($small-max) {
          width: 45px;
          height: 45px;
        }
      }

      h3 {
        @include font-size($question-title-font-size);

        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 0.5em; // 15px
      }

      p {
        @include font-size($question-answer-font-size);

        line-height: 1.5;
        font-weight: 400;
        color: $blue-light-color;
      }
    }
  }
}
</style>
