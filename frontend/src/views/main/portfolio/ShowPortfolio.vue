<template>
  <v-container fluid>
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
            <div class="subheading secondary--text text--lighten-2">Trade_balance</div>
            <div
                class="title primary--text text--darken-2"
                v-if="quoteAssetBalance"
            >{{
                quoteAssetBalance
              }} {{ portfolio.quote_asset.asset.symbol }}
            </div>
            <div
                class="title primary--text text--darken-2"
                v-else
            >0 {{ portfolio.quote_asset.asset.symbol }}
            </div>
          </div>
          <div>
            <v-toolbar light>
              <v-toolbar-title>
                Assets
              </v-toolbar-title>
              <v-spacer></v-spacer>
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
                :items="portfolio.assets"
                :search="search"
                hide-default-footer
                disable-pagination
            >
              <template v-slot:item.logo="{ item }">
                <v-img
                    width="32px"
                    height="32px"
                    :src="'https://s2.coinmarketcap.com/static/img/coins/64x64/'+ item.base.asset.cmc_id   + '.png'"
                ></v-img>
              </template>
              <template v-slot:item.price="{ item }">
                {{
                  (getAssetLastValue(item.symbol)[item.symbol]["current_price"] * 1)
                }} {{ item.quote.asset.symbol }}
              </template>
              <template v-slot:item.change24h="{ item }">
                <v-chip
                    :color="getColor((getAssetLastValue(item.symbol)[item.symbol]['current_price'] * 100 / getAssetLastValue(item.symbol)[item.symbol]['opening_price']) - 100)"
                    dark
                >{{
                    ((getAssetLastValue(item.symbol)[item.symbol]["current_price"] * 100 / getAssetLastValue(item.symbol)[item.symbol]["opening_price"]) - 100).toFixed(2)
                  }} %
                </v-chip>
              </template>
            </v-data-table>
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
  </v-container>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {
  dispatchGetPortfolios,
  dispatchGetQuoteAssetBalance,
} from '@/store/portfolio/actions';
import {dispatchDeletePortfolio, dispatchGetAssetsLastValues} from '@/store/portfolio/actions';
import {readOnePortfolio} from '@/store/portfolio/getters';

@Component
export default class ShowPortfolio extends Vue {
  public headers = [
    {text: 'Logo', sortable: false, value: 'logo', align: 'left'},
    {text: 'Name', sortable: true, value: 'base.asset.name', align: 'left'},
    {text: 'Symbol', sortable: true, value: 'base.asset.symbol', align: 'left'},
    {text: 'Price', sortable: false, value: 'price', align: 'left'},
    {text: 'Change 24H', sortable: false, value: 'change24h', align: 'left'},
  ];
  public dialog: boolean = false;
  public search = '';
  public assetsLastValues: [{}] = [{}];
  public quoteAssetBalance: number = null as any;

  public async mounted() {
    await dispatchGetPortfolios(this.$store);
    this.assetsLastValues = await dispatchGetAssetsLastValues(this.$store, {id: this.portfolio!.id});
    this.quoteAssetBalance = await dispatchGetQuoteAssetBalance(this.$store, {id: this.portfolio!.id});
  }

  public previous() {
    this.$router.back();
  }

  get portfolio() {
    return readOnePortfolio(this.$store)(+this.$router.currentRoute.params.id);
  }

  public async deletePortfolio() {
    await dispatchDeletePortfolio(this.$store, {id: this.portfolio!.id});
    this.$router.push('/main/portfolios');
  }

  public getAssetLastValue(symbol) {
    return this.assetsLastValues.find((s) => s[symbol]);
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
