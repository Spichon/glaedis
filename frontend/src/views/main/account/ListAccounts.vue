<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Manage Accounts
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
      <v-btn color="primary" to="/main/accounts/create">Create Account</v-btn>
    </v-toolbar>
    <v-data-table
        :headers="headers"
        :items="accounts"
        :search="search"
        sort-by="Exchange"
        class="elevation-1"
    >
      <template v-slot:item.broker_logo="{ item }">
        <img :class="['mr-2', 'em']"
             :width="70"
             :height="32"
             :src="item.broker.logo">
      </template>
      <template v-slot:item.public_status="{ item }">
        <v-icon v-if="item.public_status" color="green">check</v-icon>
        <v-icon v-else color="red">cancel</v-icon>
      </template>
      <template v-slot:item.private_status="{ item }">
        <v-icon v-if="item.private_status" color="green">check</v-icon>
        <v-icon v-else color="red">cancel</v-icon>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-tooltip top>
          <span>Show</span>
          <v-btn slot="activator" text :to="{name: 'main-accounts-show', params: {id: item.id}}">
            <v-icon>visibility</v-icon>
          </v-btn>
        </v-tooltip>
        <v-tooltip top>
          <span>Edit</span>
          <v-btn slot="activator" text :to="{name: 'main-accounts-edit', params: {id: item.id}}">
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
              <v-btn color="green" text @click="deleteAccount(item.id)">
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
import {readAccounts} from '@/store/account/getters';
import {dispatchDeleteAccount, dispatchGetAccounts, dispatchUpdateAccount} from '@/store/account/actions';

@Component
export default class ListAccounts extends Vue {
  public headers = [
    {
      text: 'Logo',
      sortable: false,
      value: 'broker_logo',
      align: 'left',
    },
    {
      text: 'Name',
      sortable: true,
      value: 'name',
      align: 'left',
    },
    {
      text: 'Exchange',
      sortable: true,
      value: 'broker.name',
      align: 'left',
    },
    {
      text: 'Public access',
      sortable: false,
      value: 'public_status',
      align: 'left',
    },
    {
      text: 'Private access',
      sortable: false,
      value: 'private_status',
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

  get accounts() {
    return readAccounts(this.$store);
  }

  public async deleteAccount(accountId: number) {
    await dispatchDeleteAccount(this.$store, {id: accountId});
  }

  public async mounted() {
    await dispatchGetAccounts(this.$store);
  }
}
</script>
