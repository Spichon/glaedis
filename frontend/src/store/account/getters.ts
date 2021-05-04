import {AccountState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '../state';

export const getters = {
    accounts: (state: AccountState) => state.accounts,
    oneAccount: (state: AccountState) => (accountId: number) => {
        const filteredUsers = state.accounts.filter((account) => account.id === accountId);
        if (filteredUsers.length > 0) {
            return {...filteredUsers[0]};
        }
    },
};

const {read} = getStoreAccessors<AccountState, State>('');

export const readOneAccount = read(getters.oneAccount);
export const readAccounts = read(getters.accounts);
