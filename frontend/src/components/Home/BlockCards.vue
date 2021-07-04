<template>
  <div class="content">
    <h1 class="content__title">
      {{ $t('blockCards.title') }}
    </h1>
    <p class="content__chapo">{{ $t('blockCards.chapo') }}</p>
    <carousel-3d
      v-if="visible"
      ref="carousel-3d"
      :perspective="0"
      :space="space"
      :display="display"
      :width="width"
      :height="height"
      :scaling="scaling"
      :border="0"
      :disable3d="disable3d"
      :controls-visible="controlsVisible"
      :controls-width="25"
      :controls-height="22"
      controls-prev-html='<svg width="25" height="22" viewBox="0 0 25 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20.1461 8.95275L1.64612 8.95275M1.64612 8.95275L9.98997 17.1216M1.64612 8.95275L9.98997 0.783922" stroke="#586f7c" stroke-width="2.5"/></svg>'
      controls-next-html='<svg width="25" height="22" viewBox="0 0 25 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0.5 8.95277H19M19 8.95277L10.6561 0.783936M19 8.95277L10.6561 17.1216" stroke="#586f7c" stroke-width="2.5"/></svg>'
      class="content__cards"
    >
      <slide
        class="card"
        v-for="(card, index) in $t('blockCards.cards')"
        v-bind:key="index"
        :index="index"
      >
        <img
          v-if="card.illustration === 'security'"
          class="card__illustration"
          src="@/assets/img/illustration-security.png"
          alt=""
        />
        <img
          v-if="card.illustration === 'availability'"
          class="card__illustration"
          src="@/assets/img/illustration-availability.png"
          alt=""
        />
        <img
          v-if="card.illustration === 'transparency'"
          class="card__illustration"
          src="@/assets/img/illustration-transparency.png"
          alt=""
        />
        <h2 class="card__title">{{ card.title }}</h2>
        <p class="card__chapo">{{ card.chapo }}</p>
      </slide>
    </carousel-3d>
    <div v-else class="content__cards">
      <div
        class="card"
        v-for="(card, index) in $t('blockCards.cards')"
        v-bind:key="index"
        :index="index"
      >
        <img
          v-if="card.illustration === 'security'"
          class="card__illustration"
          src="@/assets/img/illustration-security.png"
          alt=""
        />
        <img
          v-if="card.illustration === 'availability'"
          class="card__illustration"
          src="@/assets/img/illustration-availability.png"
          alt=""
        />
        <img
          v-if="card.illustration === 'transparency'"
          class="card__illustration"
          src="@/assets/img/illustration-transparency.png"
          alt=""
        />
        <h2 class="card__title">{{ card.title }}</h2>
        <p class="card__chapo">{{ card.chapo }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class BlockCards extends Vue {
  // Params 3dCarousel
  public windowWidth;
  public visible = false;
  public width = 300;
  public height = 430;
  public display = 3;
  public space = 400;
  public scaling = 1;
  public disable3d = false;
  public controlsVisible = true;

  initCarouselParams(): void {
    this.windowWidth = window.innerWidth;

    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth;
    });

    if (this.windowWidth <= 767) {
      this.visible = true;
      this.display = 3;
      this.space = 100;
      this.width = 250;
      this.height = 310;
    } else if (this.windowWidth <= 991) {
      this.visible = true;
    } else {
      this.visible = false;
    }
  }

  mounted() {
    this.initCarouselParams();

    window.addEventListener('resize', () => {
      this.initCarouselParams();
    });
  }
}
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

$card-title-font-size: (
  null: 1.875rem /* 30px */,
  $medium-max: 1.5rem /* 24px */,
  $small-max: 1.25rem /* 20px */,
);

$card-chapo-font-size: (
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
  padding: $global-padding;
  padding-top: 115px;
  padding-bottom: 175px;
  background-color: $grey-color;

  @include breakpoint($medium-max) {
    padding: $global-padding--tablet;
    padding-bottom: 55px;
    padding-top: 55px;
  }

  @include breakpoint($small-max) {
    padding: $global-padding--mobile;
    padding-bottom: 35px;
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
    max-width: 585px;
    text-align: center;
    color: $blue-light-color;
  }

  .carousel-3d-container {
    img {
      width: unset;
    }
  }

  &__cards {
    margin-top: 8.125rem; // 130px
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
    overflow: visible;

    @include breakpoint($medium-max) {
      margin-top: 2.5rem; // 40px
    }

    .card {
      display: block;
      width: calc(100% / 3 - 45px) !important;
      height: 430px !important;
      max-height: 430px !important;
      background-color: $white-color;
      padding: 85px 55px 85px 62px;
      border-radius: 20px;
      box-shadow: -5px 8px 55px -15px rgba(0, 0, 0, 0.85);
      -webkit-box-shadow: -5px 8px 55px -15px rgba(0, 0, 0, 0.85);
      -moz-box-shadow: -5px 8px 55px -15px rgba(0, 0, 0, 0.85);
      opacity: 1 !important;
      transition: all 0.2s ease-in;

      @include breakpoint($medium-max) {
        width: 100% !important;
      }

      @include breakpoint($small-max) {
        width: 250px !important;
        padding: 30px 40px;
        height: 310px !important;
      }

      &:not(.current) {
        opacity: 0.4 !important;
      }

      &__illustration {
        margin-bottom: 2.1875rem; // 35px
      }

      &__title {
        @include font-size($card-title-font-size);

        line-height: 1.2;
        font-weight: 400;
        margin-bottom: 0.833em; // 25px
      }

      &__chapo {
        @include font-size($card-chapo-font-size);

        line-height: 1.625;
        color: $blue-light-color;
      }
    }
  }
}
</style>
