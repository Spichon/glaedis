<template>
  <div class="auth">
    <amplify-authenticator username-alias="email" initial-auth-state="signin">
      <amplify-sign-up username-alias="email" :form-fields.prop="formFields" slot="sign-up"></amplify-sign-up>
    </amplify-authenticator>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {onAuthUIStateChange} from '@aws-amplify/ui-components';
import {dispatchUserLogIn} from '@/store/main/actions';

@Component
export default class Auth extends Vue {
  public formFields = [
    {
      type: 'email',
    },
    {
      type: 'password',
    },
  ];

  public async created() {
    onAuthUIStateChange((authState) => {
      if (authState === 'signedin') {
        dispatchUserLogIn(this.$store);
      }
    });
  }
}
</script>

<style>
.auth {
  margin: 0 auto;
  width: 460px;
}
</style>
