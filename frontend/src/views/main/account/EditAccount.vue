<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit Account</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form
              v-model="valid"
              ref="form"
              lazy-validation
          >
            <v-text-field label="Name" type="string" v-model="name" v-validate="'alpha_dash'"
                          data-vv-name="name" :error-messages="errors.collect('name')" required></v-text-field>
             <v-text-field label="Api Key" data-vv-name="Api Key" data-vv-delay="100"
                          v-validate="'required|min:4|modulo4'"
                          v-model="apiKey" :error-messages="errors.first('Api Key')"/>
            <v-text-field type="password" prepend-icon="lock" label="Secret Key" data-vv-name="Secret Key"
                          data-vv-delay="100" data-vv-as="secretKey" v-validate="'required|min:4|modulo4'"
                          v-model="secretKey"
                          :error-messages="errors.first('Secret Key')"/>
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
import {IAccountUpdate} from '@/interfaces';
import {dispatchDeleteAccount, dispatchGetAccounts, dispatchUpdateAccount} from '@/store/account/actions';
import {dispatchGetBrokers} from '@/store/broker/actions';
import {readOneAccount} from '@/store/account/getters';
import {readBrokers, readOneBroker} from '@/store/broker/getters';

@Component
export default class EditAccount extends Vue {
  public valid = true;
  public name: string = '';
  public apiKey: string = '';
  public secretKey: string = '';
  public dialog: boolean = false;

  public async mounted() {
    await dispatchGetAccounts(this.$store);
    await dispatchGetBrokers(this.$store);
    this.reset();
  }

  public reset() {
    this.apiKey = '';
    this.secretKey = '';
    this.$validator.reset();
    if (this.account) {
      this.name = this.account.name;
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async deleteAccount() {
    await dispatchDeleteAccount(this.$store, {id: this.account!.id});
    this.$router.push('/main/accounts');
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedAccount: IAccountUpdate = {
        name: this.name === '' ? this.broker!.name : this.name,
        api_key: this.apiKey,
        secret_key: this.secretKey,
      };
      await dispatchUpdateAccount(this.$store, {id: this.account!.id, account: updatedAccount});
      this.$router.push('/main/accounts');
    }
  }

  get account() {
    return readOneAccount(this.$store)(+this.$router.currentRoute.params.id);
  }

  get broker() {
    return readOneBroker(this.$store)(+this.account!.broker.id);
  }

  get brokers() {
    return readBrokers(this.$store);
  }
}
</script>
