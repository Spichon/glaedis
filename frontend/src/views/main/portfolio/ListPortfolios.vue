<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Manage Portfolios
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/portfolios/create">Create Portfolio</v-btn>
    </v-toolbar>
    <v-data-table
        :headers="headers"
        :items="portfolios"
        :search="search"
        sort-by="Name"
        class="elevation-1"
    >
      <template v-slot:item.quote="{ item }">
        <v-img
            width="32px"
            height="32px"
            :src="'https://s2.coinmarketcap.com/static/img/coins/64x64/'+ item.quote_asset.asset.cmc_id+ '.png'"
        ></v-img>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-tooltip top>
          <span>Show</span>
          <v-btn slot="activator" text :to="{name: 'main-portfolios-show', params: {id: item.id}}">
            <v-icon>visibility</v-icon>
          </v-btn>
        </v-tooltip>
        <v-tooltip top>
          <span>Edit</span>
          <v-btn slot="activator" text :to="{name: 'main-portfolios-edit', params: {id: item.id}}">
            <v-icon>edit</v-icon>
          </v-btn>
        </v-tooltip>
        <v-tooltip top>
          <span>Delete</span>
          <v-btn slot="activator" text @click="dialog=true">
            <v-icon>delete</v-icon>
          </v-btn>
        </v-tooltip>
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
              <v-btn color="green" text @click="deletePortfolio(item.id)">
                Agree
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {readPortfolios} from '@/store/portfolio/getters';
import {dispatchDeletePortfolio, dispatchGetPortfolios} from '@/store/portfolio/actions';

@Component
export default class ListPortfolios extends Vue {
  public headers = [
    {
      text: 'Name',
      sortable: true,
      value: 'name',
      align: 'left',
    },
    {
      text: 'Account',
      sortable: true,
      value: 'account.name',
      align: 'left',
    },
    {
      text: 'Quotation',
      sortable: false,
      value: 'quote',
      align: 'left',
    },
    {
      text: 'Actions',
      sortable: false,
      value: 'actions',
      align: 'center',
    },
  ];
  public search = '';
  public dialog: boolean = false;

  get portfolios() {
    return readPortfolios(this.$store);
  }

  public async deletePortfolio(portfolioId: number) {
    await dispatchDeletePortfolio(this.$store, {id: portfolioId});
  }

  public async mounted() {
    await dispatchGetPortfolios(this.$store);
  }
}
</script>
