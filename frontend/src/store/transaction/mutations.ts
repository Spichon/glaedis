import {ITransaction} from '../../interfaces';
import {TransactionState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '../state';

export const mutations = {
    setTransactions(state: TransactionState, payload: ITransaction[]) {
        state.transactions = payload;
    },
};

const {commit} = getStoreAccessors<TransactionState, State>('');

export const commitSetTransactions = commit(mutations.setTransactions);

