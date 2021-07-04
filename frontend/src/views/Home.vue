<template>
  <v-main class="wrapper">
    <Header></Header>
    <BlockHighlighted></BlockHighlighted>
    <BlockCards></BlockCards>
    <BlockProduct></BlockProduct>
    <BlockPricing></BlockPricing>
    <BlockFaq></BlockFaq>
    <BlockContact></BlockContact>
    <BlockStarted></BlockStarted>
    <Footer></Footer>
  </v-main>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { appName } from '@/env';

import Header from '@/components/Home/Header.vue';
import BlockHighlighted from '@/components/Home/BlockHighlighted.vue';
import BlockCards from '@/components/Home/BlockCards.vue';
import BlockProduct from '@/components/Home/BlockProduct.vue';
import BlockPricing from '@/components/Home/BlockPricing.vue';
import BlockFaq from '@/components/Home/BlockFaq.vue';
import BlockContact from '@/components/Home/BlockContact.vue';
import BlockStarted from '@/components/Home/BlockStarted.vue';
import Footer from '@/components/Home/Footer.vue';

@Component({
  components: {
    Header,
    BlockHighlighted,
    BlockCards,
    BlockProduct,
    BlockPricing,
    BlockFaq,
    BlockContact,
    BlockStarted,
    Footer,
  },
})
export default class Login extends Vue {
  public appName = appName;
}
</script>

<style lang="scss"></style>
