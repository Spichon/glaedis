<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Show Account</div>
      </v-card-title>
      <v-card-text>
        <template>
          <div class="my-3">
            <div class="subheading secondary--text text--lighten-2">Account</div>
            <div
                class="title primary--text text--darken-2"
                v-if="account"
            >{{ account.name }}
            </div>
            <div
                class="title primary--text text--darken-2"
                v-else
            >-----
            </div>
          </div>
          <div class="my-3">
            <div class="subheading secondary--text text--lighten-2">Public access</div>
            <div
                class="title primary--text text--darken-2"
                v-if="account"
            >
              <v-icon v-if="account.public_status" color="green">check</v-icon>
              <v-icon v-else color="red">cancel</v-icon>
            </div>
            <div
                class="title primary--text text--darken-2"
                v-else
            >-----
            </div>
          </div>
          <div class="my-3">
            <div class="subheading secondary--text text--lighten-2">Private access</div>
            <div
                class="title primary--text text--darken-2"
                v-if="account"
            >
              <v-icon v-if="account.private_status" color="green">check</v-icon>
              <v-icon v-else color="red">cancel</v-icon>
            </div>
            <div
                class="title primary--text text--darken-2"
                v-else
            >-----
            </div>
          </div>
        </template>
      </v-card-text>
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
            :items="availableAssets"
            :search="search"
            sort-by="Exchange"
            class="elevation-1"
        >
          <template v-slot:item.logo="{ item }">
            <v-img
                width="32px"
                height="32px"
                :src="'https://s2.coinmarketcap.com/static/img/coins/64x64/'+ item.cmc_id  + '.png'"
            ></v-img>
          </template>
        </v-data-table>
      </div>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="previous">Previous</v-btn>
        <v-btn :to="{name: 'main-accounts-edit', params: {id: account.id}}">Edit</v-btn>
        <v-btn @click.stop="dialog=true">Delete</v-btn>
      </v-card-actions>
      <v-dialog v-model="dialog" max-width="290">
        <v-card>
          <v-card-title class="headline">
            Delete Account ?
          </v-card-title>
          <v-card-text>
            Are you sure you want to delete the account ? This action is final
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="red" text @click="dialog = false">
              Disagree
            </v-btn>
            <v-btn color="green" text @click="deleteAccount">
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
import {IAccount, IAccountUpdate, IAsset} from '@/interfaces';
import {
  dispatchDeleteAccount,
  dispatchGetAccounts,
  dispatchUpdateAccount,
} from '@/store/account/actions';
import {readOneAccount} from '@/store/account/getters';
import {readBrokers, readOneBroker} from '@/store/broker/getters';
import {dispatchGetBrokers, dispatchGetAvailableAssets} from '@/store/broker/actions';

@Component
export default class ShowAccount extends Vue {
  public headers = [
    {
      text: 'Logo',
      sortable: false,
      value: 'logo',
      align: 'left',
    },
    {
      text: 'Name',
      sortable: true,
      value: 'name',
      align: 'left',
    },
    {
      text: 'Symbol',
      sortable: true,
      value: 'symbol',
      align: 'left',
    },
    {
      text: 'Type',
      sortable: true,
      value: 'type',
      align: 'left',
    },
  ];
  public search = '';
  public dialog: boolean = false;
  public availableAssets: IAsset[] = [];

  public async mounted() {
    await dispatchGetAccounts(this.$store);
    await dispatchGetBrokers(this.$store);
    this.availableAssets = await dispatchGetAvailableAssets(this.$store, {id: this.account!.broker.id});
  }

  public previous() {
    this.$router.back();
  }


  get account() {
    return readOneAccount(this.$store)(+this.$router.currentRoute.params.id);
  }

  get broker() {
    return readOneBroker(this.$store)(+this.account!.broker.id);
  }


  public async deleteAccount() {
    await dispatchDeleteAccount(this.$store, {id: this.account!.id});
    this.$router.push('/main/accounts');
  }
}
</script>
