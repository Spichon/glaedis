<template>
  <v-card>
    <v-toolbar flat>
      <template v-slot:extension>
        <v-tabs v-model="tabs" centered>
          <v-tab :key="1">
            General
          </v-tab>
          <v-tab :key="2">
            Assets
          </v-tab>
          <v-tab :key="3">
            Runs
          </v-tab>
          <v-tab :key="4">
            Transactions
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>
    <v-tabs-items v-model="tabs">
      <v-tab-item>
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Show Portfolio</div>
            <!--        <v-card-actions v-if="portfolio.automation_task">-->
            <!--          <v-btn :disabled="portfolio.account.private_status === false"-->
            <!--                 v-if="portfolio.automation_task.enabled === false" color="green" text @click="startAutomation">-->
            <!--            Start-->
            <!--            <v-icon right>not_started</v-icon>-->
            <!--          </v-btn>-->
            <!--          <v-btn v-else color="orange" text @click="pauseAutomation">-->
            <!--            Pause-->
            <!--            <v-icon right>pause</v-icon>-->
            <!--          </v-btn>-->
            <!--          <v-btn color="red" text @click="deleteAutomation">-->
            <!--            Delete-->
            <!--            <v-icon right>delete</v-icon>-->
            <!--          </v-btn>-->
            <!--        </v-card-actions>-->
            <!--        <v-card-actions v-else>-->
            <!--          <v-btn :disabled="portfolio.account.private_status === false" color="green" text @click="startAutomation">-->
            <!--            Start-->
            <!--            <v-icon right>not_started</v-icon>-->
            <!--          </v-btn>-->
            <!--        </v-card-actions>-->
          </v-card-title>
          <v-card-text>
            <!--        <template v-if="portfolio.automation_task">-->
            <!--          <div class="my-3">-->
            <!--            <div class="subheading secondary&#45;&#45;text text&#45;&#45;lighten-2">Status</div>-->
            <!--            <div-->
            <!--                class="title primary&#45;&#45;text text&#45;&#45;darken-2"-->
            <!--                v-if="portfolio.automation_task.enabled"-->
            <!--            >Running-->
            <!--            </div>-->
            <!--            <div-->
            <!--                class="title primary&#45;&#45;text text&#45;&#45;darken-2"-->
            <!--                v-else-->
            <!--            >Pause-->
            <!--            </div>-->
            <!--          </div>-->
            <!--          <div class="my-3">-->
            <!--            <div class="subheading secondary&#45;&#45;text text&#45;&#45;lighten-2">Repetitions</div>-->
            <!--            <div-->
            <!--                class="title primary&#45;&#45;text text&#45;&#45;darken-2"-->
            <!--                v-if="portfolio"-->
            <!--            >{{ portfolio.automation_task.total_run_count }}-->
            <!--            </div>-->
            <!--            <div-->
            <!--                class="title primary&#45;&#45;text text&#45;&#45;darken-2"-->
            <!--                v-else-->
            <!--            >0-->
            <!--            </div>-->
            <!--          </div>-->
            <!--          <div class="my-3">-->
            <!--            <div class="subheading secondary&#45;&#45;text text&#45;&#45;lighten-2">Last iteration</div>-->
            <!--            <div-->
            <!--                class="title primary&#45;&#45;text text&#45;&#45;darken-2"-->
            <!--                v-if="portfolio.automation_task.last_run_at"-->
            <!--            >{{ portfolio.automation_task.last_run_at | formatDate }}-->
            <!--            </div>-->
            <!--            <div-->
            <!--                class="title primary&#45;&#45;text text&#45;&#45;darken-2"-->
            <!--                v-else-->
            <!--            >-&#45;&#45;&#45;&#45;-->
            <!--            </div>-->
            <!--          </div>-->
            <!--        </template>-->
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
                  <v-icon v-if="portfolio.account.private_status" color="green">check</v-icon>
                  <v-icon v-else color="red">cancel</v-icon>
                </div>
                <div
                    class="title primary--text text--darken-2"
                    v-else
                >-----
                </div>
              </div>
              <div class="my-3">
                <div class="subheading secondary--text text--lighten-2">Optimizer</div>
                <div
                    class="title primary--text text--darken-2"
                    v-if="portfolio"
                >{{ portfolio.optimizer.name }}
                </div>
                <div
                    class="title primary--text text--darken-2"
                    v-else
                >-----
                </div>
              </div>
              <div class="my-3" v-if="portfolio.optimizer.name === 'Max_profit'">
                <div class="subheading secondary--text text--lighten-2">Risk Free</div>
                <div
                    class="title primary--text text--darken-2"
                    v-if="portfolio"
                >{{ portfolio.risk_free + '%' }}
                </div>
                <div
                    class="title primary--text text--darken-2"
                    v-else
                >-----
                </div>
              </div>
              <div class="my-3">
                <div class="subheading secondary--text text--lighten-2">Quotation</div>
                <div
                    class="title primary--text text--darken-2"
                    v-if="portfolio"
                >{{ portfolio.quote_asset.asset.symbol }}
                </div>
                <div
                    class="title primary--text text--darken-2"
                    v-else
                >-----
                </div>
              </div>
              <div class="my-3">
                <div class="subheading secondary--text text--lighten-2">Ticker</div>
                <div
                    class="title primary--text text--darken-2"
                    v-if="portfolio"
                >{{ portfolio.ticker }}
                </div>
                <div
                    class="title primary--text text--darken-2"
                    v-else
                >-----
                </div>
              </div>
              <div class="my-3">
                <div class="subheading secondary--text text--lighten-2">Quote asset Balance</div>
                <div
                    class="title primary--text text--darken-2"
                    v-if="portfolio"
                >{{
                    portfolio.quote_asset_balance
                  }} {{ portfolio.quote_asset.asset.symbol }}
                </div>
                <div
                    class="title primary--text text--darken-2"
                    v-else
                >0 {{ portfolio.quote_asset.asset.symbol }}
                </div>
              </div>
              <div class="my-3">
                <div class="subheading secondary--text text--lighten-2">Used balance</div>
                <div
                    class="title primary--text text--darken-2"
                    v-if="portfolioAssets"
                >{{
                    equityBalance.toFixed(2)
                  }} {{ portfolio.quote_asset.asset.symbol }}
                </div>
                <div
                    class="title primary--text text--darken-2"
                    v-else
                >0 {{ portfolio.quote_asset.asset.symbol }}
                </div>
              </div>
            </template>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="previous">Previous</v-btn>
            <v-btn :to="{name: 'main-portfolios-edit', params: {id: portfolio.id}}">Edit</v-btn>
            <v-btn @click.stop="dialog=true">Delete</v-btn>
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
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-title class="text-h5">
            Assets
          </v-card-title>
          <v-card-text>
            <div>
              <v-toolbar light>
                <v-text-field
                    v-model="search"
                    append-icon="mdi-magnify"
                    label="Search"
                    single-line
                    hide-details
                ></v-text-field>
              </v-toolbar>
              <v-data-table
                  :headers="headers"
                  :items="portfolioAssets"
                  :search="search"
                  hide-default-footer
                  disable-pagination
              >
                <template v-slot:item.logo="{ item }">
                  <v-img
                      width="32px"
                      height="32px"
                      :src="'https://s2.coinmarketcap.com/static/img/coins/64x64/'+ item.asset_broker_pair.base.asset.cmc_id   + '.png'"
                  ></v-img>
                </template>
                <template v-slot:item.price="{ item }">
                  {{ (item.current_price) }} {{ item.asset_broker_pair.quote.asset.symbol }}
                </template>
                <template v-slot:item.change24h="{ item }">
                  <v-chip
                      :color="getColor((item.current_price * 100 / item.opening_price) - 100)"
                      dark
                  >{{
                      ((item.current_price * 100 / item.opening_price) - 100).toFixed(2)
                    }} %
                  </v-chip>
                </template>
              </v-data-table>
            </div>
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-title class="text-h5">
            Runs
          </v-card-title>
          <v-card-text>
            <div>
              <v-toolbar light>
                <v-text-field
                    v-model="searchRun"
                    append-icon="mdi-magnify"
                    label="Search"
                    single-line
                    hide-details
                ></v-text-field>
              </v-toolbar>
              <v-data-table
                  :headers="headersRuns"
                  :items="runs"
                  :search="searchRun"
                  hide-default-footer
                  disable-pagination
              >
                <template v-slot:item.date="{ item }">
                  {{ item.date | formatDate }}
                </template>$
              </v-data-table>
            </div>
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-title class="text-h5">
            Transactions
          </v-card-title>
          <v-card-text>
            <div>
              <v-toolbar light>
                <v-text-field
                    v-model="searchTransaction"
                    append-icon="mdi-magnify"
                    label="Search"
                    single-line
                    hide-details
                ></v-text-field>
              </v-toolbar>
              <v-data-table
                  :headers="headersTransactions"
                  :items="transactions"
                  :search="searchTransaction"
                  hide-default-footer
                  disable-pagination
              >
                <template v-slot:item.date="{ item }">
                  {{ item.date | formatDate }}
                </template>$
              </v-data-table>
            </div>
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {
  dispatchGetPortfolioAssets,
  dispatchGetPortfolios,
} from '@/store/portfolio/actions';
import {dispatchDeletePortfolio, dispatchGetPortfolioEquityBalance} from '@/store/portfolio/actions';
import {dispatchGetRuns} from '@/store/run/actions';
import {dispatchGetTransactions} from '@/store/transaction/actions';
import {readOnePortfolio, readPortfolios} from '@/store/portfolio/getters';
import {IPortfolioAssetBroker} from '@/interfaces';
import {readRuns} from '@/store/run/getters';
import {readTransactions} from '@/store/transaction/getters';

@Component
export default class ShowPortfolio extends Vue {
  public headers = [
    {text: 'Logo', sortable: false, value: 'logo', align: 'left'},
    {text: 'Name', sortable: true, value: 'asset_broker_pair.base.asset.name', align: 'left'},
    {text: 'Symbol', sortable: true, value: 'asset_broker_pair.base.asset.symbol', align: 'left'},
    {text: 'Price', sortable: false, value: 'price', align: 'left'},
    {text: 'Quantity', sortable: false, value: 'qty', align: 'left'},
    {text: 'Change 24H', sortable: false, value: 'change24h', align: 'left'},
  ];
  public headersRuns = [
    {text: 'Date', sortable: true, value: 'date', align: 'left'},
    {text: 'State', sortable: true, value: 'state', align: 'left'},
    {text: 'Optimizer', sortable: true, value: 'optimizer.name', align: 'left'},
  ];
  public headersTransactions = [
    {text: 'Date', sortable: true, value: 'date', align: 'left'},
    {text: 'Asset', sortable: true, value: 'asset_broker_pair.symbol', align: 'left'},
    {text: 'Qty', sortable: true, value: 'qty', align: 'left'},
    {text: 'Price', sortable: true, value: 'price', align: 'left'},
    {text: 'Side', sortable: true, value: 'side', align: 'left'},
  ];
  public dialog: boolean = false;
  public search = '';
  public searchRun = '';
  public searchTransaction = '';
  public portfolioAssets: IPortfolioAssetBroker[] = [];
  public equityBalance: number = 0;
  public tabs = null;

  public async mounted() {
    await dispatchGetPortfolios(this.$store);
    this.portfolioAssets = await dispatchGetPortfolioAssets(this.$store, {id: this.portfolio!.id});
    await dispatchGetRuns(this.$store, {id: this.portfolio!.id});
    await dispatchGetTransactions(this.$store, {id: this.portfolio!.id});
    this.equityBalance = await this.getEquityBalance();
  }

  public previous() {
    this.$router.back();
  }

  get portfolio() {
    return readOnePortfolio(this.$store)(+this.$router.currentRoute.params.id);
  }

  get runs() {
    return readRuns(this.$store);
  }

  get transactions() {
    return readTransactions(this.$store);
  }

  public async deletePortfolio() {
    await dispatchDeletePortfolio(this.$store, {id: this.portfolio!.id});
    this.$router.push('/main/portfolios');
  }

  public async getEquityBalance() {
    return this.portfolioAssets.reduce((total, obj) => obj.current_price * obj.qty + total, 0);
  }

  public getColor(percent) {
    if (percent < 0) {
      return 'red';
    } else if (percent > 0) {
      return 'green';
    } else {
      return 'orange';
    }
  }
}
</script>
