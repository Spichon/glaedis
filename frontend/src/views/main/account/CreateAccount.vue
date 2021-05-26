<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create Account</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Name" type="string" v-model="name" v-validate="'alpha_dash'"
                          data-vv-name="name" :error-messages="errors.collect('name')" required></v-text-field>
            <v-select
                label="Broker"
                data-vv-name="brokerId"
                data-vv-delay="100"
                v-model="brokerId"
                :items="brokers"
                item-value="id"
                item-text="name"
                v-validate="'required'"
                :error-messages="errors.first('brokerId')"
            >
            </v-select>
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
        <v-btn @click="submit" :disabled="!valid">
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {IAccountCreate} from '@/interfaces';
import {dispatchGetAccounts, dispatchCreateAccount} from '@/store/account/actions';
import {dispatchGetBrokers} from '@/store/broker/actions';
import {readBrokers, readOneBroker} from '@/store/broker/getters';
import {readOneAccount} from '@/store/account/getters';

@Component
export default class CreateAccount extends Vue {
  public valid = false;
  public name: string = '';
  public apiKey: string = '';
  public secretKey: string = '';
  public brokerId: number = null as any;

  public async mounted() {
    await dispatchGetAccounts(this.$store);
    await dispatchGetBrokers(this.$store);
    this.reset();
  }

  public reset() {
    this.brokerId = null as any;
    this.name = '';
    this.apiKey = '';
    this.secretKey = '';
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  get brokers() {
    return readBrokers(this.$store);
  }

  get broker() {
    return readOneBroker(this.$store)(+this.brokerId);
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedAccount: IAccountCreate = {
        name: this.name === '' ? this.broker!.name : this.name,
        broker_id: this.brokerId,
        api_key: this.apiKey,
        secret_key: this.secretKey,
      };
      await dispatchCreateAccount(this.$store, updatedAccount);
      this.$router.push('/main/accounts');
    }
  }
}
</script>
