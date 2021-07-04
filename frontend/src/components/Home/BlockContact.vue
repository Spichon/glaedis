<template>
  <div id="contact" class="content">
    <h1 class="content__title">{{ $t('blockContact.title') }}</h1>
    <p class="content__chapo">{{ $t('blockContact.chapo') }}</p>
    <form action="" class="content__form">
      <div class="field">
        <label for="name" class="visuallyhidden">{{
          $t('blockContact.formName')
        }}</label>
        <input
          type="text"
          name="name"
          id="name"
          :placeholder="$t('blockContact.formName')"
        />
      </div>
      <div class="field">
        <label for="email" class="visuallyhidden">{{
          $t('blockContact.formEmail')
        }}</label>
        <input
          type="email"
          name="email"
          id="email"
          :placeholder="$t('blockContact.formEmail')"
        />
      </div>
      <div class="field">
        <label for="message" class="visuallyhidden">{{
          $t('blockContact.formMessage')
        }}</label>
        <textarea
          name="message"
          id="message"
          :placeholder="$t('blockContact.formMessage')"
        ></textarea>
      </div>
      <input
        class="submit btn"
        type="submit"
        :value="$t('blockContact.formSubmit')"
      />
    </form>
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
  padding: $global-padding;
  padding-bottom: 60px;
  padding-top: 75px;

  @include breakpoint($medium-max) {
    padding: $global-padding--tablet;
    padding-bottom: 30px;
    padding-top: 45px;
  }

  @include breakpoint($small-max) {
    padding: $global-padding--mobile;
    padding-bottom: 25px;
    padding-top: 25px;
  }

  &__title {
    @include font-size($title-font-size);

    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 0.547em; // 35px
  }

  &__chapo {
    @include font-size($chapo-font-size);

    font-weight: 400;
    line-height: 1.6;
    max-width: 670px;
    color: $blue-light-color;
    text-align: center;
  }

  &__form {
    margin-top: 5rem; // 80px

    @include breakpoint($medium-max) {
      margin-top: 2.5rem; // 40px
    }

    .field {
      width: 705px;

      @include breakpoint($small-max) {
        width: 100%;
        max-width: 100%;
      }

      input,
      textarea {
        width: 100%;
        border: solid 1px $blue-form-color;
        border-radius: 10px;
        padding: 25px 35px;
        color: $blue-light-color;
        background-color: $blue-form-light-color;

        &::placeholder {
          color: $blue-light-color;
        }
      }

      input {
        height: 75px;
        margin-bottom: 1.875rem; // 30px

        @include breakpoint($small-max) {
          height: 55px;
        }
      }

      textarea {
        height: 275px;
        max-height: 275px;
        overflow: auto;
        resize: none;
        margin-bottom: 3.4375rem; // 55px

        @include breakpoint($medium-max) {
          margin-bottom: 1.875rem; // 30px
        }

        @include breakpoint($small-max) {
          height: 210px;
          max-height: 210px;
        }
      }
    }

    .submit {
      margin: 0 auto;
    }
  }
}
</style>
