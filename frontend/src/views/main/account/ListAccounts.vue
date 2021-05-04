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
    <v-data-table :headers="headers" :items="accounts" :search="search">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td class="justify-center">
          <v-icon v-if="props.item.public_status" color="green">check</v-icon>
          <v-icon v-else color="red">cancel</v-icon>
        </td>
        <td class="justify-center">
          <v-icon v-if="props.item.private_status" color="green">check</v-icon>
          <v-icon v-else color="red">cancel</v-icon>
        </td>
        <td class="justify-center layout px-0">
          <v-tooltip top>
            <span>Show</span>
            <v-btn slot="activator" flat :to="{name: 'main-accounts-show', params: {id: props.item.id}}">
              <v-icon>visibility</v-icon>
            </v-btn>
          </v-tooltip>
          <v-tooltip top>
            <span>Edit</span>
            <v-btn slot="activator" flat :to="{name: 'main-accounts-edit', params: {id: props.item.id}}">
              <v-icon>edit</v-icon>
            </v-btn>
          </v-tooltip>
          <v-tooltip top>
            <span>Delete</span>
            <v-btn slot="activator" flat @click="dialog=true">
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
                <v-btn color="green" text @click="deleteAccount(props.item.id)">
                  Agree
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {Store} from 'vuex';
import {IAccount, IAccountUpdate} from '@/interfaces';
import {readAccounts} from '@/store/account/getters';
import {dispatchDeleteAccount, dispatchGetAccounts, dispatchUpdateAccount} from '@/store/account/actions';

@Component
export default class ListAccounts extends Vue {
  public headers = [
    {
      text: 'Account',
      sortable: true,
      value: 'name',
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
      value: 'id',
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
