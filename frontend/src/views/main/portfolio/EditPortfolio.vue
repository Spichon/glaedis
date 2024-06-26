<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit Portfolio</div>
      </v-card-title>
      <v-card-text>
        <template>
          <div class="my-3">
            <div class="subheading secondary--text text--lighten-2">Name</div>
            <div
                class="title primary--text text--darken-2"
                v-if="portfolio"
            >{{ portfolio.name }}
            </div>
            <div
                class="title primary--text text--darken-2"
                v-else
            >-----
            </div>
          </div>
          <div class="my-3">
            <div class="subheading secondary--text text--lighten-2">Account</div>
            <div
                class="title primary--text text--darken-2"
                v-if="portfolio"
            >{{ portfolio.account.name }}
            </div>
            <div
                class="title primary--text text--darken-2"
                v-else
            >-----
            </div>
          </div>
          <v-select
              label="Optimizer"
              data-vv-name="optimizerId"
              data-vv-delay="100"
              v-model="optimizerId"
              :items="optimizers"
              item-value="id"
              item-text="name"
              v-validate="'required'"
              :error-messages="errors.first('optimizerId')"
          ></v-select>
          <v-slider
              v-if="optimizer && optimizer.name==='Max_profit'"
              v-model="riskFree.val"
              :label="'Risk Free'"
              :thumb-color="riskFree.color"
              thumb-label="always"
          >
            <template v-slot:thumb-label="{ value }">
              {{ value + '%' }}
            </template>
          </v-slider>
          <v-form
              v-model="valid"
              ref="form"
              lazy-validation
          >
            <v-text-field
                label="Name"
                v-model="name"
                required
            ></v-text-field>
            <v-select
                label="Ticker"
                data-vv-name="Ticker"
                data-vv-delay="100"
                v-model="ticker"
                :items="Object.keys(timeframes.timeframes)"
                v-validate="'required'"
                :error-messages="errors.first('ticker')"
            ></v-select>
            <v-card elevation="10">
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
                      :key="refresh"
                      v-model="selected"
                      :headers="headers"
                      :items="tradableAssetPairs"
                      :search="search"
                      item-key="id"
                      show-select
                      hide-default-footer
                      disable-pagination
                      class="elevation-1"
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
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn @click.stop="dialog=true">Delete</v-btn>
        <v-btn
            @click="submit"
            :disabled="!valid"
        >
          Save
        </v-btn>
      </v-card-actions>
      <v-dialog v-model="dialog" max-width="290">
        <v-card>
          <v-card-title class="headline">
            Delete Portfolio ?
          </v-card-title>
          <v-card-text>
            Are you sure you want to delete the portfolio ? This action is final
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="red" text @click="dialog = false">
              Disagree
            </v-btn>
            <v-btn color="green" text @click="deletePortfolio">
              Agree
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {IAssetBroker, IAssetBrokerPair, IPortfolioAssetBroker, IPortfolioUpdate, ITimeframes} from '@/interfaces';
import {dispatchGetQuoteAssets, dispatchGetTimeframes, dispatchGetTradableAssetPairs} from '@/store/broker/actions';
import {dispatchGetOptimizers} from '@/store/optimizer/actions';
import {
  dispatchGetPortfolios,
  dispatchUpdatePortfolio,
  dispatchDeletePortfolio, dispatchGetPortfolioAssets,
} from '@/store/portfolio/actions';
import {readOnePortfolio} from '@/store/portfolio/getters';
import {readOneOptimizer, readOptimizers} from '@/store/optimizer/getters';

@Component
export default class EditPortfolio extends Vue {
  public valid = true;
  public name: string = '';
  public tradableAssetPairs: IAssetBrokerPair[] = [];
  public quoteAssetId: number = null as any;
  public optimizerId: number = null as any;
  public quoteAssets: IAssetBroker[] = [];
  public selected: IAssetBrokerPair[] = [];
  public portfolioAssets: IPortfolioAssetBroker[] = [];
  public timeframes: ITimeframes = {timeframes: {}};
  public dialog: boolean = false;
  public refresh: boolean = false;
  public search = '';
  public ticker: string = null as any;
  public riskFree = {label: 'color', val: 10, color: 'orange darken-3'};
  public headers = [
    {text: 'Logo', sortable: false, value: 'logo', align: 'left'},
    {text: 'Name', sortable: true, value: 'base.asset.name', align: 'left'},
    {text: 'Symbol', sortable: true, value: 'base.asset.symbol', align: 'left'},
    {text: 'Type', sortable: true, value: 'base.asset.type', align: 'left'},
  ];

  public async mounted() {
    await dispatchGetPortfolios(this.$store);
    await dispatchGetOptimizers(this.$store);
    this.quoteAssets = await dispatchGetQuoteAssets(this.$store, {id: this.portfolio!.account.broker.id});
    this.timeframes = await dispatchGetTimeframes(this.$store, {id: this.portfolio!.account.broker.id});
    this.portfolioAssets = await dispatchGetPortfolioAssets(this.$store, {id: this.portfolio!.id});
    this.reset();
  }

  public async getTradableAssetPairs() {
    this.tradableAssetPairs = await dispatchGetTradableAssetPairs(this.$store, {id: this.quoteAssetId});
    if (this.quoteAssetId === this.portfolio!.quote_asset_id) {
      this.selected = [];
      for (const portfolioAsset in this.portfolioAssets) {
        this.selected.push(this.portfolioAssets[portfolioAsset].asset_broker_pair);
      }
    } else {
      this.selected = [];
    }
  }

  public reset() {
    this.name = '';
    this.$validator.reset();
    if (this.portfolio) {
      this.name = this.portfolio.name;
      this.selected = [];
      for (const portfolioAsset in this.portfolioAssets) {
        this.selected.push(this.portfolioAssets[portfolioAsset].asset_broker_pair);
      }
      this.quoteAssetId = this.portfolio!.quote_asset_id;
      this.ticker = this.portfolio!.ticker;
      this.riskFree.val = this.portfolio!.risk_free;
      this.optimizerId = this.portfolio!.optimizer.id;
    }
    this.getTradableAssetPairs();
  }

  public cancel() {
    this.$router.back();
  }

  public async deletePortfolio() {
    await dispatchDeletePortfolio(this.$store, {id: this.portfolio!.id});
    this.$router.push('/main/portfolios');
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedPortfolio: IPortfolioUpdate = {
        name: this.name,
        quote_asset_id: this.quoteAssetId,
        asset_broker_pairs: this.selected,
        ticker: this.ticker,
        risk_free: this.riskFree.val,
        optimizer_id: this.optimizerId,
      };
      await dispatchUpdatePortfolio(this.$store, {id: this.portfolio!.id, portfolio: updatedPortfolio});
      this.$router.push('/main/portfolios');
    }
  }

  get portfolio() {
    return readOnePortfolio(this.$store)(+this.$router.currentRoute.params.id);
  }

  get optimizers() {
    return readOptimizers(this.$store);
  }

  get optimizer() {
    return readOneOptimizer(this.$store)(+this.optimizerId);
  }
}
</script>
