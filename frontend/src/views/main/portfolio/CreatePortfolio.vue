<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create Portfolio</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Name" type="string" v-model="name" v-validate="'required|alpha_dash'"
                          data-vv-name="name" :error-messages="errors.collect('name')" required></v-text-field>
            <v-select
                label="AccountId"
                data-vv-name="AccountId"
                data-vv-delay="100"
                v-model="accountId"
                v-on:change="setAccountInformation"
                :items="accounts"
                item-text="name"
                item-value="id"
                v-validate="'required'"
                :error-messages="errors.first('accountId')"
            ></v-select>
            <v-select
                label="Ticker"
                data-vv-name="Ticker"
                data-vv-delay="100"
                v-model="ticker"
                v-if="accountId"
                :items="Object.keys(timeframes.timeframes)"
                v-validate="'required'"
                :error-messages="errors.first('ticker')"
            ></v-select>
          </v-form>
        </template>
      </v-card-text>
      <v-card elevation="10" v-if="accountId">
        <v-card-title class="display-1 text--primary">
          Select your assets
          <v-select
              class="ml-5"
              width="20"
              data-vv-name="quoteAssetId"
              data-vv-delay="100"
              v-model="quoteAssetId"
              v-on:change="getTradableAssetPairs"
              :items="quoteAssets"
              item-value="id"
              v-validate="'required'"
              :error-messages="errors.first('quoteAssetId')"
          >
            <template v-slot:selection="{ item, index }">
              <img :class="['mr-2', 'em']"
                   :width="32"
                   :height="32"
                   :src="'https://s2.coinmarketcap.com/static/img/coins/64x64/'+ item.asset.cmc_id + '.png'">
              {{ item.asset.symbol }}
            </template>
            <template v-slot:item="{ item }">
              <img :class="['mr-2', 'em']"
                   :width="32"
                   :height="32"
                   :src="'https://s2.coinmarketcap.com/static/img/coins/64x64/'+ item.asset.cmc_id + '.png'">
              {{ item.asset.symbol }}
            </template>
          </v-select>
          <v-spacer></v-spacer>
          <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
          ></v-text-field>
        </v-card-title>
        <v-layout class="my-3" column style="height: 40vh">
          <v-flex style="overflow: auto">
            <v-data-table
                v-model="selected"
                :headers="headers"
                :items="tradableAssetPairs"
                :search="search"
                item-key="base.asset.name"
                show-select
                class="elevation-1"
                hide-default-footer
                disable-pagination
            >
              <template v-slot:item.logo="{ item }">
                <v-img
                    width="32px"
                    height="32px"
                    :src="'https://s2.coinmarketcap.com/static/img/coins/64x64/'+ item.base.asset.cmc_id  + '.png'"
                ></v-img>
              </template>
            </v-data-table>
          </v-flex>
        </v-layout>
      </v-card>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn @click="submit" :disabled="!valid">
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {IAssetBroker, IAssetBrokerPair, IPortfolioCreate, ITimeframes} from '@/interfaces';
import {dispatchGetAccounts} from '@/store/account/actions';
import {dispatchGetPortfolios} from '@/store/portfolio/actions';
import {dispatchCreatePortfolio} from '@/store/portfolio/actions';
import {readAccounts, readOneAccount} from '@/store/account/getters';
import {dispatchGetQuoteAssets, dispatchGetTimeframes, dispatchGetTradableAssetPairs} from '@/store/broker/actions';

@Component
export default class CreatePortfolio extends Vue {
  public valid = false;
  public name: string = '';
  public accountId: number = null as any;
  public quoteAssetId: number = null as any;
  public tradableAssetPairs: IAssetBrokerPair[] = [];
  public quoteAssets: IAssetBroker[] = [];
  public selected: IAssetBrokerPair[] = [];
  public search = '';
  public timeframes: ITimeframes = {'timeframes': {}};
  public ticker: string = null as any;
  public headers = [
    {text: 'Logo', sortable: false, value: 'logo', align: 'left'},
    {text: 'Name', sortable: true, value: 'base.asset.name', align: 'left'},
    {text: 'Symbol', sortable: true, value: 'base.asset.symbol', align: 'left'},
    {text: 'Type', sortable: true, value: 'base.asset.type', align: 'left'},
  ];

  public async mounted() {
    await dispatchGetAccounts(this.$store);
    await dispatchGetPortfolios(this.$store);
    this.reset();
  }

  public reset() {
    this.name = '';
    this.accountId = null as any;
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async setAccountInformation() {
    this.quoteAssets = await dispatchGetQuoteAssets(this.$store, {id: this.account!.broker.id});
    this.timeframes = await dispatchGetTimeframes(this.$store, {id: this.account!.broker.id});
  }

  public async getTradableAssetPairs() {
    this.tradableAssetPairs = await dispatchGetTradableAssetPairs(this.$store, {id: this.quoteAssetId});
  }

  get accounts() {
    return readAccounts(this.$store);
  }

  get account() {
    return readOneAccount(this.$store)(+this.accountId);
  }


  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedPortfolio: IPortfolioCreate = {
        name: this.name,
        account_id: this.accountId,
        asset_broker_pairs: this.selected,
        quote_asset_id: this.quoteAssetId,
        ticker: this.ticker,
      };
      await dispatchCreatePortfolio(this.$store, updatedPortfolio);
      this.$router.push('/main/portfolios');
    }
  }
}
</script>
