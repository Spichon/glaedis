import { IAccount} from '../../interfaces';
import { AccountState} from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setAccounts(state: AccountState, payload: IAccount[]) {
        state.accounts = payload;
    },
    setAccount(state: AccountState, payload: IAccount) {
        const accounts = state.accounts.filter((account: IAccount) => account.id !== payload.id);
        accounts.push(payload);
        state.accounts = accounts;
    },
    removeAccount(state: AccountState, payload: IAccount) {
        const accounts = state.accounts.filter((account: IAccount) => account.id !== payload.id);
        state.accounts = accounts;
    },
};

const { commit } = getStoreAccessors<AccountState, State>('');

export const commitSetAccounts = commit(mutations.setAccounts);
export const commitSetAccount = commit(mutations.setAccount);
export const commitRemoveAccount = commit(mutations.removeAccount);

