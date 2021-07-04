<template>
  <div class="content">
    <h1 class="content__title">{{ $t('blockStarted.title') }}</h1>
    <p class="content__chapo">{{ $t('blockStarted.chapo') }}</p>
    <a
      class="content__cta btn"
      :href="$t('blockStarted.link')"
      :title="$t('blockStarted.cta')"
      >{{ $t('blockStarted.cta') }}</a
    >
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class BlockStarted extends Vue {}
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
  justify-content: flex-end;
  align-items: center;
  height: 642px;
  padding: $global-padding;
  padding-bottom: 70px;
  color: $white-color;
  background-image: url('../../assets/svg/background-started.svg');
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;

  @include breakpoint($medium-max) {
    padding: $global-padding--tablet;
    padding-bottom: 55px;
    padding-top: 55px;
    height: 470px;
  }

  @include breakpoint($small-max) {
    padding: $global-padding--mobile;
    padding-bottom: 25px;
    padding-top: 25px;
    height: 400px;
  }

  &__title {
    @include font-size($title-font-size);

    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 1.016em; // 65px
    text-align: center;
  }

  &__chapo {
    @include font-size($chapo-font-size);

    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 3em; // 60px
    max-width: 735px;
    text-align: center;
  }
}
</style>
